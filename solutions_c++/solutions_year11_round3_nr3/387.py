#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
using namespace std;

int num[200]={0};

int main()
{
ifstream in;
ofstream out;
in.open("C-small-attempt0.in");
out.open("OUTPUT.txt");

int T;
int N,L,H;
in>>T;

for(int Case=1;Case<=T;Case++){
in>>N>>L>>H;
for(int i=0;i<N;i++)
in>>num[i];

int check=1;
int ans=0;
for(int d=L;d<=H;d++){
	check=1;
	for(int j=0;j<N;j++){
		if(d%num[j]!=0&&num[j]%d!=0){
			check=0;
			break;
		}
	}
	if(check==1){
		ans=d;
		break;
	}
	
}
if(d>H)
out<<"Case #"<<Case<<": NO"<<endl;
else
out<<"Case #"<<Case<<": "<<ans<<endl;



}

in.close();
out.clear();
out.close();
return 0;
}