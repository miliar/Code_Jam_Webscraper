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

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;cin>>t;
    for(int tcase=1;tcase<=t;tcase++){
        cout<<"Case #"<<tcase<<": ";
        int n,l,h;
        cin>>n>>l>>h;
        vector<int> v;
        for(int i=0;i<n;i++){
            int x;cin>>x;
            v.PB(x);
        }
        int mf=0;
        while(l<=h && !mf){
            int flag=0;
            for(int i=0;i<n && !flag;i++){
                int a=min(v[i],l),b=max(v[i],l);
                if(b%a!=0)
                    flag++;
            }
            if(!flag){
                cout<<l<<endl;
                mf++;
            }
            l++;
        }
        if(!mf){
            cout<<"NO\n";
        }
    }
}
