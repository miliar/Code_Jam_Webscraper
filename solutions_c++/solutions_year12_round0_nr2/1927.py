#include<iostream>
#include<cstring>
#include<cstdlib>
using namespace std;

int T,t,N,S,P,ans,g;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;t=0;
    while (T--) {
          t++;ans=0;
          cin>>N>>S>>P;
          for (int i=0;i<N;i++){
              cin>>g;
              if (g%3==0) {
                 if (g/3>=P) ans++;
                 else if ((S>0)&&(g/3+1>=P)&&(g/3-1>=0)) {S--;ans++;}
              } else if (g%3==2) {
                if (g/3+1>=P) ans++;
                else if ((S>0)&&(g/3+2>=P)) {S--;ans++;}
              } else if (g/3+1>=P) ans++;
          }
          cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
