
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <memory.h>
#pragma comment(linker,"/STACK:16777216")

using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define N 100000  
const int oo = int(1e6); 
const double pi = acos(-1.0);
const double eps = 1e-7;

typedef long long ll;
typedef __int64 int64;

int main()
{
    freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
    int test,i,j,prev,a,b,x,y,t,p,res;
   	char s[10]={'0','1','2','3','4','5','6','7','8','9'};	
   
    
	scanf("%d",&test);
	for(t=0;t<test;t++)
	{
	  scanf("%d%d",&a,&b);
      res=0;
      for(i=a;i<=b;i++)
	  {
         x=i; 
         string s1("");
         do
         {
           p=x%10;
           s1=s[p]+s1;
           x/=10;
         }while(x);
         prev=-1;
       	 for(int ii=0;ii<s1.size();ii++)
         {
           string aa=s1.substr(0,ii+1);
	       string bb=s1.substr(ii+1,s1.size()-ii);
	       string st=bb+aa;
	       int n=atoi(st.c_str());
           if(aa.empty() || bb.empty() || n==i)continue;
	       
           if(n<=b && n>i && n!=prev)
           {
             prev=n;
             res++;
           } 
         }
    
      }
	  printf("Case #%d: %d\n",t+1,res);
	}  
	return 0;

}
