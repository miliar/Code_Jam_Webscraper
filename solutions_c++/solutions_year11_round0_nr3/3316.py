#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<malloc.h>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<list>
#include<string>
#include<map>
#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SS ({int x;scanf("%d",&x);x;})
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

vector<int> C;
int ans;
void solve(int id,int a,int b,int c,int d)
{
    if(id==C.size()){
        if(a==b && c!=0 && d!=0){
            ans=max(max(c,d),ans);
        }
        return;
    }
    solve(id+1,a^C[id],b,c+C[id],d);
    solve(id+1,a,b^C[id],c,d+C[id]);
}
int main()
{
    freopen("inp.in","r",stdin);
    freopen("oup.out","w",stdout);
    int t;cin>>t;
    for(int tc=1;tc<=t;tc++){
        int n;cin>>n;
        C.clear();
        ans=0;
        for(int i=0;i<n;i++){
            int x;cin>>x;
            C.PB(x);
        }
        solve(0,0,0,0,0);
        cout<<"Case #"<<tc<<": ";
        if(ans==0){
            cout<<"NO\n";
        }
        else{
            cout<<ans<<endl;
        }
    }
}
