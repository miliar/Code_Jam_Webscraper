#include <iostream>
#include <fstream>

using namespace std;

int AA, BB;

int Rotate ( int i ) {

	int index = 0 ;
	int ii = i;
	int A[20];
	int B[40];
	while ( i != 0 ) {
		A[index]=i%10;
		i=i/10;
		index++;
	}


	int j ;

	/*for ( j = 0 ; j < index ; j++ ) 
		cout << A[j] << " " ;
	cout << endl;*/

	for ( j = index-1 ; j>=0 ; j-- ){ 
		B[j]=A[index-1-j];
		B[j+index]=B[j];
	}

	/*for ( j = 0 ; j < 2*index ; j++ ) 
		cout << B[j] << " ";
	cout << endl;*/

	int count = 0;
	int ind = index-1;
	while ( ind >= 0 ) {

		int num=0;
		//cout << ind << " " << ind+index-1 << endl;
		for ( j = ind ; j <= ind+index-1 ; j++ )
			num=num*10+B[j];

		//cout << " num " << num << endl;
		if ( ( num >= AA ) && ( num <= BB ) && ( num != ii )  ) count++;
		ind--; 
	}

	//cout << " Count " << ii << " " << count << endl;
	return count;

	
}
int Count ( int A , int B ) {

	int i ;
	int sum  = 0 ;
	for ( i = A ; i <=B ; i++ ) {
		sum+=Rotate(i);
	}
	sum=sum/2;
	return sum;
}
void Readata(){

	ifstream fin("Input.txt");
	int T;
	fin >> T;
	int i;
	for ( i = 0 ; i < T ; i++ ) {

		//int A , B ;
		fin >> AA >> BB ;
		cout << "Case #" << i+1 <<": "<< Count(AA,BB) << endl;
	}
}
int main()
{
	Readata();
	return 0;
}
