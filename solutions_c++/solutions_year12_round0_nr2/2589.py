#include <iostream>
using namespace std;

#define _for(i,x,n) for(int i=x;i<n;i++)

int main(){
    int T;
    cin>>T;
    _for(tt,1,T+1){
        int N,S,P,res=0,surp=0;
        cin>>N>>S>>P;
        _for(i,0,N){
            int v,x,y,z;
            cin>>v;
            if(v%3==0){
                x=y=z=v/3;
                if(x>=P || y>=P || z>=P)
                    res++;
                else{
                    y=x-1;
                    z=x+1;
                    if(y<0 || z>10) continue;
                    if(x>=P || y>=P || z>=P)
                        surp++;
                }
            }
            else if(v%3==1){
                x=y=v/3;
                z=x+1;
                if(x>=P || y>=P || z>=P)
                    res++;
                else{
                    x--;
                    y++;
                    if(x<0) continue;
                    if(x>=P || y>=P || z>=P)
                        surp++;
                }
            }
            else{
                x=v/3;
                y=x+1;
                z=x+1;
                if(x>=P || y>=P || z>=P)
                    res++;
                else{
                    y=x;
                    z=x+2;
                    if(z>10) continue;
                    if(x>=P || y>=P || z>=P)
                        surp++;
                }
            }
        }
        cout<<"Case #"<<tt<<": "<<res+min(S,surp)<<endl;
    }
}
