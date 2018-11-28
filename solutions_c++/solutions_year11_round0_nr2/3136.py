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
    freopen("binp.in","r",stdin);
    freopen("oup.out","w",stdout);
    int t;cin>>t;
    for(int tc=1;tc<=t;tc++){
        map<string,char> C;
        map<string,int> D;
        int c;cin>>c;
        for(int i=0;i<c;i++){
            string s;cin>>s;
            string tmp,tmp2;tmp+=s[0];tmp+=s[1];tmp2+=s[1];tmp2+=s[0];
            C[tmp]=s[2];
            C[tmp2]=s[2];
        }
        int d;cin>>d;
        for(int i=0;i<d;i++){
            string s;cin>>s;
            string tmp,tmp2;tmp+=s[0];tmp+=s[1];tmp2+=s[1];tmp2+=s[0];
            D[tmp]=1;
            D[tmp2]=1;
        }
        int n;cin>>n;
        string s;cin>>s;
        char ans[10000];
        int len=0;
        for(int i=0;i<n;i++){
            if(len==0){
                ans[len++]=s[i];
                continue;
            }
            string tmp;tmp+=ans[len-1];tmp+=s[i];
            if(C[tmp]){
                ans[len-1]=C[tmp];
                continue;
            }
            int flag=0;
            for(int j=0;j<len && !flag;j++){
                tmp="";tmp+=s[i];tmp+=ans[j];
                if(D[tmp]){
                    len=0;
                    flag++;
                }
            }
            if(!flag){
                ans[len++]=s[i];
            }
        }
        cout<<"Case #"<<tc<<": "<<"[";
        for(int i=0;i<len;i++){
            cout<<ans[i];
            if(i+1<len){
                cout<<", ";
            }
        }
        cout<<"]\n";
    }
}
