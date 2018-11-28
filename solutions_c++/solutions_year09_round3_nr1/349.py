#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
typedef long long ll;
#define sz(x) (int)x.size()
main()
{
   int T;
   scanf("%d",&T);
   
   for(int t=0; t < T; t++)
   {
     string in;
     cin >> in;
     
     int asd[127]={0};
     int b=0;
     for(int i=0; i < sz(in); i++)
     {
     	if(asd[in[i]] == 0)
     	{
     	asd[in[i]]=1;
     	b++;
     	}
     }
     if(b==1)
     b=2;
    vector<int> v(in.size(),-1);
    char ref=in[0];
    for(int i=0;i < sz(in); i++)
    {
    	if(in[i] == ref)
    	v[i]=1;
    }
    
    int i=0;
    for(i=0; i < sz(in); i++)
    if(v[i] == -1)
    break;
    
    ref=in[i];
    for(i=0;i < sz(in); i++)
    {
    	if(in[i] == ref)
    	v[i]=0;
    }
    
    int u=2;
    for(int i=0; i < sz(in); i++)
    {
      if(v[i] == -1)
      {	
    	for(int j=i; j < sz(in); j++)
    	if(in[i] == in[j])
    	v[j]=u;
    	u++;
      }
    }
    
    ll m=1;
    ll sum=0;
    for(int p=sz(in)-1; p >= 0; p--)
    {
      sum=sum+m*v[p];	
      m=m*b;	
    }
     	
   	printf("Case #%d: %lld\n",t+1,sum);
   }

}
