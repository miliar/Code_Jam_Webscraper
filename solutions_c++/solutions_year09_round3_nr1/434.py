#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
typedef long long ll;
#define sz(x) (int)x.size()
main()
{
   int num;
   scanf("%d",&num);
   
   for(int q=0; q < num; q++)
   {
     string str;
     cin>>str;
     
     int m[255]={0};
     int b=0;
     for(int i=0; i < str.length(); i++)
     {
     	if(m[str[i]] != 1)
     	{
     	m[str[i]]=1;
     	b++;
     	}
     }
     if(b==1) b++;
     
    vector<int> v(str.size(),-1);
    
    for(int i=0;i < str.length(); i++)
    {
    	if(str[i] == str[0])
    	v[i]=1;
    }
    
    int i=0;
    for(i=0; i < str.length(); i++)
    if(v[i] == -1)
    break;
    
    char ref=str[i];
    for(i=0;i < str.length(); i++)
    {
    	if(str[i] == ref)
    	v[i]=0;
    }
    
    int c=2;
    for(int i=0; i < str.length(); i++)
    {
      if(v[i] == -1)
      {	
    	for(int j=i; j < str.length(); j++)
    	if(str[i] == str[j])
    	v[j]=c;
    	c++;
      }
    }
    
    ll w=1;
    ll sum=0;
    for(int p=str.length()-1; p >= 0; p--)
    {
      sum=sum+w*v[p];	
      w=w*b;	
    }
     	
   	printf("Case #%d: %lld\n",q+1,sum);
   }

}
