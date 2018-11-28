#include <iostream>
#include <cstring>

using namespace std;

int n,s,p;
int t;
int c[110];
int d=1;

int main()
{
    cin>>t;
    while(t--){
        cin>>n>>s>>p;
        for(int i=0;i<n;i++) cin>>c[i];
        int ans=0;
        for(int i=0;i<n;i++){
            int base = c[i]/3;
            if(c[i]%3==0){
                if(base>=p) ans++;
                else if(s>0 && base> 0 && base+1 >=p){
                    ans++;
                    s--;
                }
            }else if(c[i]%3==1){
                if(base>=p || (base+1)>=p) ans++;
                else if(s>0 && base+1 >=p){
                    ans++;
                    s--;
                }
            }else if(c[i]%3==2){
                if(base>=p || (base+1)>=p) ans++;
                else if(s>0 && base+2 >=p){
                    ans++;
                    s--;
                }
            }
        }
        cout<<"Case #"<<d<<": "<<ans<<endl;
        d++;
    }
    return 0;
}
