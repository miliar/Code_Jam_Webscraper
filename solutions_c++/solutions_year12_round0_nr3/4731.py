#include<set>
#include<utility>
#include<cmath>
#include<iostream>
#include<cstdio>
using namespace std;

set < pair<int,int> >st;

int a,b,dig;

int dg(int n)
{ if(!n)return 0;
return 1+dg(n/10);
}


int rst(int n,int d,int e)
{    int t=(int)pow(10.0,d);
    int a=n%t,b=n/t;
    return a*pow(10.0,e) +b;
}



int main()
{
    int t,i,k=1;
    cin>>t;
    
    while(t--)
    {
              cin>>a>>b;
              
              for(i=a;i<b;i++)
              {
              int x=dg(i),m;
         dig=x;
       x--;
       while(x>0)
  { m=rst(i,x,dig-x);
   if(m>i && m<=b)st.insert(make_pair(i,m));
    x--;
  }
              }
              
              printf("Case #%d: %d\n",k++,st.size());
              st.clear();
    }
  
  return 0;
}  
              
    
    


  
  
    
