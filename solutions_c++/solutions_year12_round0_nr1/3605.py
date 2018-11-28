#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define mpair make_pair
#define pii pair<int,int>
#define MM(a,b) memset(a,b,sizeof(a));
typedef long long lld;
typedef unsigned long long u64;
template<class T> bool up_max(T& a,const T& b){return b>a? a=b,1 : 0;}
template<class T> bool up_min(T& a,const T& b){return b<a? a=b,1 : 0;}
#define maxn

char t[]={
    'y', 'h', 'e', 's', 'o', 'c', 'v',
    'x', 'd', 'u', 'i', 'g', 'l', 'b',
    'k', 'r', 'z',      't', 'n', 'w',
    'j', 'p', 'f',      'm', 'a', 'q'
};
string ch;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,i,j;
    cin>>T;
    getchar();
    for(i=1;i<=T;++i){
        getline( cin, ch );
        printf("Case #%d: ", i);
        for(j=0;j<ch.length();++j){
            if( ' '==ch[j] ) printf(" ");
            else printf("%c", t[ ch[j]-'a' ] );
        }
        puts("");
    }
}
