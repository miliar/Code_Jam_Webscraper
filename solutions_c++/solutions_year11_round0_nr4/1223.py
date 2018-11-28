#include<iostream>
#include<vector>

using namespace std;

int b[10000];
bool u[10000];

int main(){
    freopen("D-large.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc,n,v;
    scanf("%d\n",&tc);
    for(int t=1;t<=tc;t++){
        int res=0;
        scanf("%d\n",&n);
        vector<pair<int,int> > a;
        for(int i=0;i<n;i++){
            scanf("%d",&v);
            a.push_back(make_pair(v,i));
            u[i]=false;
        }
        sort(a.begin(),a.end());
        for(int i=0;i<n;i++)
            b[a[i].second]=i;
        for(int i=0;i<n;i++)
            if(!u[i]){
                int k=0;
                for(int j=i;!u[j];j=b[j]){
                    u[j]=true;
                    k++;
                }
                if(k>1)res+=k;
            }
        printf("Case #%d: %d.000000\n",t,res);
    }
    return 0;
}
