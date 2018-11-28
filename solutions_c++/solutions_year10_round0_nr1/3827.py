# include <iostream>
# include <math.h>
# include <string.h>
int output[10001];
long N,K;
long tmp;
int T;
char s[10];
using namespace std;
int main()
{
	int ctr;
	cin>>T;
//processing goes in here
	for(ctr=0;ctr<T;ctr++)
	{
	      cin>>N>>K;
	      tmp=pow(2,N);
	      if((K+1)%tmp==0)
	         output[ctr]=1;
	      else
	         output[ctr]=0;
	}
//printing output
//Case #1: OFF
for(ctr=0;ctr<T;ctr++)
{
      if(output[ctr]==1)
        strcpy(s,"ON");
      else
        strcpy(s,"OFF");
      cout<<"Case #"<<(ctr+1)<<":"<<" "<<s<<"\n";
}
      
}
