//#include <iostream>
//#include <fstream>
//#include <string>
//using namespace std;
//
//
//
//char dict [500];
//
//
//int main(){
//	ifstream in1 ("in1.txt");
//	ifstream in2 ("in2.txt");
//	ofstream out1 ("out1.txt");
//	ofstream out2 ("out2.txt");
//	int T;
//	in1>>T;
//	string s1, s2;
//		getline(in1, s1);
//	for( int i = 0; i < T; i++ ){
//		getline(in1, s1);
//		getline(in2, s2);
//		int len = s1.length();
//		for( int j = 0; j < len; j++ ){
//			if( s1[j]==' ' ) continue;
//			dict[ s1[j] ] = s2[j];
//		}
//	}
//	for( char c = 'a'; c<='z'; c++ ){
//		out1<<c<<" "<< dict[c]<<endl;
//		out2<<'\''<<dict[c]<<"', "<<endl;
//	}
//}

#include <iostream>
#include <fstream>
#include <string>
using namespace std;



char dict []={
'y', 
'h', 
'e', 
's', 
'o', 
'c', 
'v', 
'x', 
'd', 
'u', 
'i', 
'g', 
'l', 
'b', 
'k', 
'r', 
'z', 
't', 
'n', 
'w', 
'j', 
'p', 
'f', 
'm', 
'a', 
'q', 

};




int main(){
	ifstream in1 ("in1.txt");
	ofstream out ("out.txt");
	
	int T;
	in1>>T;
	string s1, s2;
	getline(in1, s1);
	for( int i = 0; i < T; i++ ){
		out<<"Case #"<<i+1<<": ";
		getline(in1, s1);
		int len = s1.length();
		for( int j = 0; j < len; j++ ){
			if( s1[j]==' ' ){
				cout<<' ';
			}
			out<<dict[ s1[j]-'a' ];
		}
		out<<endl;
	}
	
}