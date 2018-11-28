#include<iostream>
#include<cstdio>
using namespace std;
const int N = 1005;
int be[N],ed[N],w[N];
double l[N];
int T,tt,s,x,r,n;
double t;
void swap(int &a,int &b){
    int tmp=a; a=b; b=tmp;
}
int main (){
    freopen("A-large.in","r",stdin);
    freopen("Alarge.out","w",stdout);
    cin>>T; tt=0;
    while (T--){
        cin>>x>>s>>r>>t>>n;
        int sum =0;
        for (int i=1;i<=n;i++) {
            cin>>be[i]>>ed[i]>>w[i];
            l[i]=ed[i]-be[i];
            sum+=l[i];
        }
        sum = x-sum; // cout<<sum<<endl;
        if (sum>0){
            n++; w[n]=0;
            l[n]=sum;
        }
        for (int i=1;i<=n;i++)for (int j=i+1;j<=n;j++)
        if (w[j]<w[i]){
            swap(w[i],w[j]);
            swap(l[i],l[j]);
            //swap(ed[i],ed[j]);
        }
        double ans = 0;
        for (int i=1;i<=n;i++){
            //cout<<w[i]<<endl;
            if (t>0){
                if ((w[i]+r)*t>=l[i]){
                    t-=l[i]/(w[i]+r);
                    ans+=l[i]/(w[i]+r);
                } else {
                    ans+=t;
                    ans+=(l[i]-t*(r+w[i]))/(s+w[i]);
                    t=0;
                }
            } else {
                ans+=(l[i])/(s+w[i]);
            }
        }
        printf("Case #%d: %.8llf\n",++tt,ans);
    }

}
