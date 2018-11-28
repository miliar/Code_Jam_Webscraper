#include<iostream>
#include<cstring>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
    int i,T;
    
    cin>>T;
    for (i=1;i<=T;i++)
    {
              int N,S,p;
              int a=0,b=0,t=0;
              cin>>N>>S>>p;
              while(N--) 
              {
                        cin>>t;
                        
                        if (t%3==0) 
                        {
                                         if (t/3>=p) a++;
                                         else if (t/3+1==p && t/3-1>=0 && t/3+1<=10) b++;
                        }
                        
                        else if (t%3==1) {if (t/3+1>=p) a++;}
                        
                        else
                        {
                                         if (t/3+1>=p) a++;
                                         else if (t/3+2==p && t/3+2<=10) b++;
                        }        
                          
              }
              a+=(b<S?b:S);
              cout<<"Case #"<<i<<": "<<a<<endl;
    }
	return 0;
}

