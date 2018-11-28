#include<iostream>
#include<set>
#include<utility>
#include<cmath>
#include<cstdio>
using namespace std;

set < pair<int,int> >s;

int a,b,dig;

int digit(int n)
{ if(!n)return 0;
return 1+digit(n/10);
}


int reset(int n,int d,int e)
{    int t=(int)pow(10.0,d);
    int a=n%t,b=n/t;
    return a*pow(10.0,e) +b;
}

int fn(int n)
{ int x=digit(n)-1,m;
  dig=x+1;
  while(x>0)
  { m=reset(n,x,dig-x);
    if(m>n && m<=b)s.insert(make_pair(n,m));
    x--;
  }
}

int main()
{
    int t,i,j=1;
    cin>>t;
    //cout<<reset(100,2,1);
    while(t--)
    {
              cin>>a>>b;
              
              for(i=a;i<b;i++)fn(i);
              printf("Case #%d: %d\n",j++,s.size());
              s.clear();
    }
  //system("pause");
  return 0;
}  
              
    
    


  
  
    
