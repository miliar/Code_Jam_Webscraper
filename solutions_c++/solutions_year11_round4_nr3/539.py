#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
#include <math.h>
using namespace std;

int prime[1000002]={0};

int main()
{
ifstream in;
ofstream out;
double Num;
in.open("C-small-attempt0.in");
out.open("OUTPUT.txt");

int T;
in>>T;

for(int Case=1;Case<=T;Case++){
in>>Num;
double nn=log(Num);
if((int)Num==1){
out<<"Case #"<<Case<<": "<<0<<endl;
continue;
}
int ans=1;
double t=2,tt=0;
do{	
	if(prime[int(t)]){
		t+=1;
		continue;

	}
	for(int i=int(t+t);i<=sqrt(Num);i+=t)prime[i]=1;
	
	tt=log(t);
	if(nn/tt-1<0)break;
	ans+=(int)floor(nn/tt-1);
	t=t+1;

}while(tt<=nn/2);
out<<"Case #"<<Case<<": "<<ans<<endl;




}

in.close();
out.clear();
out.close();
return 0;
}