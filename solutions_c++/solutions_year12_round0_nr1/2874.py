#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int per[26];
char A[200];
char B[200];

void Pre_Process (){

	ifstream fin1("A.txt");
	ifstream fin2("B.txt");

	int index = 0;
	char x ;
	char y ;

	while (fin1 >> x ){
		A[index]=x;
		index++;
	}

	index=0;
	fin1.close();
	while ( fin2 >> y ) {
		B[index]=y;
		index++;
	}

	int i ;
	for ( i = 0 ; i < index ; i++ ) 
		if ( ( A[i] <= 'z' ) && (A[i]>='a' ) ){
			per[A[i]-'a']=B[i]-'a';
		}

	int mark[26];
	for ( i = 0 ; i < 26 ; i++ ) 
		mark[i]=0;

	per['z'-'a']='q'-'a';
	char ch1 ;
	char ch2;
	for ( i = 0 ; i < 26 ; i++ ){ 
		//ch1 = 'a'+i;
		//ch2 = 'a'+per[i];
		mark[per[i]]=1;
		//cout << ch1 << " " << ch2 << endl;
	}

	int lost;
	for ( i = 0 ; i < 26 ; i++ ) 
		if ( mark[i] == 0 ) lost = i; 

	per['q'-'a']=lost;

	for ( i = 0 ; i < 26 ; i++ ) {

		ch1 = 'a'+i;
		ch2 = 'a'+per[i];
		//cout << ch1 << " " << ch2 << endl;
	}
}

void Readata(){

	Pre_Process();
	ifstream fin("Input.txt");
	int T;
	fin >> T ;
	int i;
	string str;
	//for ( i = 0 ; i < 26 ; i++ ) 
	//	cout << per[i] << endl;

	//char str[200];
	for ( i = 0 ; i < T+1 ; i++ ){

		//cout << "Case #" << i << ": "; 
		getline(fin,str);

		if ( i != 0 ) {
		cout << "Case #" << i << ": ";
		//cout << str << endl;
		int j ;
		for ( j = 0 ; j < str.length() ; j++ ){
			char ch = str[j]; 
			if (( str[j]<='z') && (str[j]>='a')) 
				 ch = 'a'+per[str[j]-'a'];
			cout << ch;
	} 
	cout << endl;
	}
}
}

int main()
{
	Readata();
	return 0;
}
