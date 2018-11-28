#include<iostream>
#include<cstdio>
#include<string.h>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

int t,n,s,p,a;

int main(){
    cin >> t;
    for(int cas=1;cas<=t;cas++){
        cin >> n >> s >> p;
        int ans=0;
        for(int i=0;i<n;i++){
            cin >> a;
            int b=a/3,c=a%3;
            if(c==0){
                if(b>=p) ans++;
                else if(b==p-1&&s>0&&b>=1){
                    ans++;
                    s--;
                }
            }
            if(c==1){
                if(b>=p-1) ans++;
            }
            if(c==2){
                if(b>=p-1) ans++;
                else if(b==p-2&&s>0){
                    ans++;
                    s--;
                }
            }
        }
        printf("Case #%d: ",cas);
        cout << ans << endl;
    }
    return 0;
}
