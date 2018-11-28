#include<cstdio>
#include<cmath>
#include<cstring>
#include<iostream>
using namespace std;
int abs(int x){
    if(x>0)return x;
    else return -x;
}
int main(){
    int T,cas,n,i,j;
         //  freopen ("A-large.in","r",stdin);
          //freopen ("AAL.out","w",stdout);
     cin>>T;
    for(cas=1;cas<=T;cas++){

        cin>>n;
        int j=0,k=0,t,p[112],pre[112];
        char s[112][2];
       //   cout<<n<<endl;
        for(i=0;i<n;i++){
            cin>>s[i]>>p[i];
        //    cout<<s[i]<<" "<<p[i]<<endl;
        }
        memset(pre,-1,sizeof(pre));
        for(i=n-1;i>=0;i--){
            if(s[i][0]=='B')
            for(j=i-1;j>=0;j--){
                if(s[i][0]==s[j][0]){
                    pre[i]=j;
                    i=j+1;
                    break;
                }
            }
        }
        for(i=n-1;i>=0;i--){
            if(s[i][0]=='O')
            for(j=i-1;j>=0;j--){
                if(s[i][0]==s[j][0]){
                    pre[i]=j;
                    i=j+1;
                    break;
                }
            }
        }
        /*
        for(i=0;i<n;i++){
            cout<<pre[i]<<endl;
        }
        */
        int tm[112];
        for(i=0;i<n;i++){
            if(i==0){
                tm[i]=p[i];
            }
            else if(pre[i]==-1){
                tm[i]=max(tm[i-1]+1,p[i]);
            }
            else {
                tm[i]=max(tm[i-1]+1,tm[pre[i]]+abs(p[pre[i]]-p[i])+1);
            }
        }
        printf("Case #%d: ",cas);
        cout<<tm[n-1]<<endl;
    }

}


