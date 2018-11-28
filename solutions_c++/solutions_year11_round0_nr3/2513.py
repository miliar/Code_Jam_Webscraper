#include<fstream>
using namespace std;

void sortArray ( int [] , int );

int main()
{
	int T, N , PatrickSum , value, SeanSum, sum;
	int *Array;
	ifstream in;  ofstream out;
	in.open ( "in.txt" );
	out.open ( "out.txt" );
	in >>T;
	for ( int k=0 ; k < T ; k++ )
	{
		in >> N;
		value = 0;
		Array  = new int [N];
		for ( int i=0 ; i < N ; i++ )
			in >> Array[i]; 
		sortArray ( Array , N);
		for ( int i=N-1 ; i > 0 ; i-- )
		{
			PatrickSum = 0;
			SeanSum = 0;
			sum=0;
			for ( int j=0 ; j < i ; j++ )
				PatrickSum = PatrickSum^Array[j];
			for ( int j=i ; j < N ; j++ )
			{SeanSum = SeanSum^Array[j]; sum+=Array[j];}
			if ( (SeanSum == PatrickSum) )
				value = sum;
		}
		out<<"Case #"<<k+1<<": ";
		if ( value == 0 )
			out<<"NO\n";
		else 
			out<<value<<'\n';
	}
	in.close();
	out.close();
	return 0;
}

void sortArray ( int a[] , int length)
{
	for (int i = 0; i < length-1; i++) 
		{      
		int min = i;      
		for (int j = i + 1; j < length; j ++) 
			{	
			if (a[j] < a[min]) min = j;      
			}
         swap(a[i], a[min]); 
	     }
}