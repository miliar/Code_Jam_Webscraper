#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
#include <algorithm>

using namespace std;

int Num[1001]={0};
int Ord_Num[1001]={0};
double Ex=0;

int cmp( const int &a, const int &b ){
    if( a < b )
       return 1;
    else
       return 0;
}


int main()
{
ifstream in;
ofstream out;
in.open("D-large.in");
out.open("OUTPUT.txt");

int T,N;
in>>T;
for(int Cas=1;Cas<=T;Cas++){
	in>>N;
	Ex=0;
	for(int i=0;i<N;i++){
		in>>Num[i];
		Ord_Num[i]=Num[i];
	}
	sort(Ord_Num,Ord_Num+N,cmp);
	
	for( i=0;i<N;i++){
		if(Num[i]!=Ord_Num[i])Ex+=1;
	}
	out.setf(ios::fixed);
	out.precision(6);

	out<<"Case #"<<Cas<<": "<<Ex<<endl;
}

in.close();
out.clear();
out.close();
return 0;
}