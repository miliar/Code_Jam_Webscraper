#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <map>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <string>
#include <set>
#include <cstring>
using namespace std;
#define For(i,n) for(int i=0;i<n;i++)
#define sFor(i,j,n) for(int i=j;i<n;i++)
#define sz(i) int(i.size())
#define mst(i,n) memset(i,n,sizeof(i))
#define eps 1e-9
#define INF 1e20
#define MOD 1000000007
#define LL long long
#define pi acos(-1)
LL gcd(LL a,LL b){if(a==0)return b;return gcd(b%a,a);}
int main()
{
    int t;
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    scanf("%d\n",&t);
    int ca = 0;
    char trans[]="yhesocvxduiglbkrztnwjpfmaq";
    while(t--){
        char str[1<<10];
        gets(str);
        printf("Case #%d: ",++ca);
        For(i,strlen(str)){
            if(str[i]==' ') printf(" ");
            else printf("%c",trans[str[i]-'a']);
        }
        printf("\n");
    }
    return 0;
}
