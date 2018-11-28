#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{int T,N,S,p,i;
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
 cin>>T;
 for(i=1;i<=T;i++)
    {cin>>N>>S>>p;
     int x,r,P,bx;
     r=P=0;
     while(N--)
        {cin>>x;
         if(x==0)bx=0;
         else bx=(x-1)/3+1;
         if(bx>=p)r++;
         else if((bx==p-1) && x && (x%3!=1))P++;
        }
     P=S>P?P:S;
     cout<<"Case #"<<i<<": "<<r+P<<endl;
    }
    
    return EXIT_SUCCESS;
}
