#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

#define FORU(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define maxn 52

const long long oo=(long long)1e18;

using namespace std;

int tnum;
char s[1000] , m[]="ynficwlbkuomxsevzpdrjgthaq";

int main(){
freopen("Asmall0.in","r",stdin);
freopen("Asmall0.out","w",stdout);

char d[1000];
FORU(i,0,25) d[m[i]]=i+'a';
d[' ']=' ';

scanf("%d\n",&tnum);
FORU(t,1,tnum){
    FORU(i,0,900) s[i]=0;
    gets(s+1);
    int l=strlen(s+1);
    FORU(i,1,l) s[i]=d[s[i]];
    printf("Case #%d: %s\n",t,s+1);
    }

return 0;
}
