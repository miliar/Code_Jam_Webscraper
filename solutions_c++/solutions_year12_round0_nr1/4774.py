#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<vector>
#include<stack>
#include<sstream>
#include<cstdlib>
#include<algorithm>
using namespace std;
#define si(n) scanf("%d",&n)
#define sf(n) scanf("%f",&n)
#define sl(n) scanf("%lld",&n)
#define lli long long int

char E[]= {'o','u','r','l','a','n','g','e','i','s','m','p','b','t','d','h','w','y','x','f','j','k','v','c','q','z'};
char G[]={'e','j','p','m','y','s','l','c','k','d','x','v','n','r','i','b','t','a','h','w','u','o','g','f','z','q'};


int main()
{
  int t;
  si(t);
  cin.ignore();
  int r=1;
  while(t--)
    {
     
      string GG="";
      getline(cin,GG);
      string res="";
      for(int i=0;i<GG.size();i++)
	if(GG[i]==' ')
	  res+=' ';
	else
	  {
	for(int j=0;j<26;j++)
	  if(GG[i]==G[j])
	    res+=E[j];
	  }
      cout<<"Case #"<<r<<": "<<res<<"\n";
      r++;
    }
  return 0; 

}
