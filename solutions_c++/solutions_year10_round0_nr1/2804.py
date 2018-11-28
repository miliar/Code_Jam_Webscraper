#include<iostream>
#include<fstream>
using namespace std;
int POW2[31]={1};
void init()
{int i;
for(i=1;i<=30;i++)
{POW2[i]=POW2[i-1]*2;
}
}
int main()
{int T=1,ans;
 int i,N,K;
 ifstream in;
 ofstream out;
 in.open("A-large.in");
 out.open("OUTPUT.txt");
 in>>T;
 init();
for(i=1;i<=T;i++)
{in>>N>>K;
 ans=(((K+1)&(POW2[N]-1))==0);
 if(ans==1)
	 out<<"Case #"<<i<<": ON"<<endl;
 else
	 out<<"Case #"<<i<<": OFF"<<endl;
}
return 0;
}
