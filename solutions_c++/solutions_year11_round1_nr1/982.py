#include<iostream>
using namespace std;
int main()
 { long long n,d,g,c=0,f,i,x,w,l,tw,tl,t;
   cin>>t;
   while(t--)
    { cin>>n>>d>>g;f=0;c++;
      if(n<100){
                  for(i=1;i<=n;i++)
                    {x=i*d;if(x%100==0){w=x/100;l=i-w;tw=i*g;tl=i*100-tw;if(tl>=l && tw>=w){f=1;break;} }
                    }
                }
      else
        { w=d;l=100-w;tw=100*g;tl=100*(100-g);if(tl>=l && tw>=w)f=1;
        }                
      if(f==0) cout<<"Case #"<<c<<": Broken"<<endl;
      else cout<<"Case #"<<c<<": Possible"<<endl;
      }
      return 0;
      }
