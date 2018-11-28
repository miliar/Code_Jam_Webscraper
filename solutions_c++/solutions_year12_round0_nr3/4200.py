#include <iostream>
#include <fstream>   // I'm wael matar :D waelsy123@gmail.com
#include <map>
#include <string>
#include <cmath>
#include <utility>
#include <vector>
using namespace std ; 
int min(int a, int b ) {
	if(a<b) return a ;
	return b ;
}

int max(int a ,int b ){
	if(a>b) return b ; 
	return a ;
} 

int main (){

	ifstream in ("t.in") ;
	ofstream out ("t.out") ;
	int test = 1 ;
	int t ; 
	in >> t ;
	for(int ti=0;ti<t;ti++){
		map < vector <int>   , bool> mm ;

		int  n  , m ;
		int num = 0 ;
		in >> n >> m ;
		int N=log10(double(n) ) +1 ;
		for(int j = n ; j<m;j++){
			for(int i = 1 ; i<=N; i++){
				int temp1 =  j / pow(10.0,i) ;
				long temp2 =  j%int (pow(10.0,i)) * pow(10.0,N-i) + temp1 ;
				//pair <int,int > tp ;
				//out << temp2  << endl; 
				vector <int> tp(2) ;
				tp[0]=min(temp2,j) ;
				tp[1]=max(temp2,j) ;
				//tp = make_pair (min(temp2,j) , max(temp2,j) );
				if(  temp2 <= m && temp2 >= j && temp2 != j ){
					num++ ;
					mm[tp] = 1 ;
					//out << j << "  " << temp2 << endl;  
				}
			}//i
		}//j

		if(num!=0 && n >=1000) { num-- ; }
		out << "Case #" << test << ": " << num << endl; 
		test++ ;
	}//t



	return 0 ;
}
