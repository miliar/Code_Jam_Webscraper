#include <iostream>
#include <fstream>   // I'm wael matar :D waelsy123@gmail.com
#include <map>
#include <string>
#include <cmath>
#include <utility>
#include <vector>
using namespace std ; 

int main (){

	ifstream in ("t.in") ;
	ofstream out ("t.out") ;
	int test = 1 ;
	int t ;
	in >> t ; 
	for(int ti=0;ti<t;ti++){
		int num = 0 ;
		int n , s , p , x ;
		in >> n >> s >> p ; 
		for(int i =0 ;i<n;i++){ 
			in >> x ;
			if (x/3==0 && (x%3==0 || x%3==1)&&p!=0 ) continue ;
			else if(x/3>=p) num++;
			else if ( x/3==p-1 && x%3>0 ) num++ ;
			else if ( x/3==p-1 && s>0 )  { num++ ;  s--; }
			else if ( x/3==p-2 && (x%3==2) && s>0 )  { num++ ;  s--; }
		}

		out << "Case #" << test << ": " << num << endl; 
		test++ ;
	}//t



	return 0 ;
}
