#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
using namespace std;


int main()
{
ifstream in;
ofstream out;
in.open("C-large.in");
out.open("OUTPUT.txt");
int T,N;
int sum=0;
int sum_sb=0;
int Min_v=100000000;
int a;

in>>T;
for(int Cas=1;Cas<=T;Cas++){
	in>>N;
	sum=0;sum_sb=0;
	Min_v=100000000;
	for(int i=0;i<N;i++){
		in>>a;
		sum+=a;
		sum_sb^=a;
		if(Min_v>a)Min_v=a;
	}
	out<<"Case #"<<Cas<<": ";
	if(sum_sb!=0)out<<"NO"<<endl;
	else{
		out<<sum-Min_v<<endl;
	}



}




in.close();
out.clear();
out.close();
return 0;
}