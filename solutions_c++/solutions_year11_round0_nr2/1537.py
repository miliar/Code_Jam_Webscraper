#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

#define ll long long

int T;
int c,d,n;
char cmb[300][300];
bool op[300][300];
char ans[200];
int sz;
string s;
string q;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int k=1;k<=T;k++){
        memset(cmb,'.',sizeof(cmb));
        memset(op,false,sizeof(op));
        scanf("%d ",&c);
        for (int i=0;i<c;i++){
            cin>>q;
            cmb[q[0]][q[1]]=q[2];
            cmb[q[1]][q[0]]=q[2];
        }
        scanf("%d ",&d);
        for (int i=0;i<d;i++){
            cin>>q;
            op[q[0]][q[1]]=true;
            op[q[1]][q[0]]=true;
        }
        scanf("%d ",&n);
        cin>>s;
        sz=0;
        for (int i=0;i<n;i++){
            ans[sz++]=s[i];
            if (cmb[ans[sz-2]][ans[sz-1]]!='.'){
                ans[sz-2]=cmb[ans[sz-2]][ans[sz-1]];
                sz--;
            }else{
                for (int i=0;i<sz-1;i++)
                    if (op[ans[i]][ans[sz-1]]){
                        sz=0;
                        break;
                    }
            }
        }
        printf("Case #%d: [",k);
        for (int i=0;i<sz;i++)
            if (i!=sz-1) printf("%c, ",ans[i]);
            else printf("%c",ans[i]);
        printf("]\n");
    }
    return 0;
}
