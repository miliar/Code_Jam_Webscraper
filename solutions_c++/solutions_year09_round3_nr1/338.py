#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <queue>
using namespace std;
char s[256];
long long pow(int a,int p){
    long long ret=1;
    for(int i=0;i<p;i++)ret*=a;
    return ret;
}
int main(){
    int t,no=1;
    scanf("%d",&t);
    char str[128];
    while(t--){
        scanf("%s",str);
        int l=strlen(str);
        memset(s,0,sizeof(s));
        int base=0;
        for(int i=0;i<l;i++){
           if(s[str[i]])continue;
           s[str[i]]=1;
           base++;
        }
        if(base==1)base++;
        for(int i=0;i<256;i++)s[i]=-1;
        s[str[0]]=1;
        int i;
        for( i=1;i<l;i++){
            if(s[str[i]]!=s[str[0]])break;
            s[str[i]]=1;
        }
        if(i<l)s[str[i]]=0;
        int st=2;
        long long ans=0;
        for( i=0;i<l;i++){
            if(s[str[i]]!=-1)ans+=s[str[i]]*pow(base,l-i-1);
            else {
                s[str[i]]=st++;
                ans+=s[str[i]]*pow(base,l-i-1);
            }
            //cout<<ans<<" "<<(int)s[str[i]]<<endl;
        }
        printf("Case #%d: %I64ld\n",no++,ans);
    }
    return 0;
}

