#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <queue>
#include <list>
#include <cstring>
#define FOR(i,a,n) for(int i=a;i<=n;i++)
#define REP(i,n) for (int i=0;i<n;i++)
#define FORD(i,n,a) for(int i=n;i>=a;i--)
#define PB push_back
#define MP make_pair
#define xx first
#define yy second
#define Min(a,b) a<b ? a:b
#define Max(a,b) a>b ? a:b
#define p2(a) ((a)*(a))
#define ALL(v) v.begin(),v.end()
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef double dd;
vi l[30];
int t[30];
int slowo[600];
int n,cnt;
void wczytajslowo(void){
    char c;
    memset(slowo,0,sizeof(slowo));
    cnt=0;
    do{
        int nr;
        scanf("%c",&c);
        if(c=='\n')
            break;
        if(c==' ')
            nr=27;
        else
            nr=(int)(c-'a');
        slowo[cnt++]=nr;
    }while(c!='\n');
}
int solve(void){
    wczytajslowo();
    memset(t,0,sizeof(t));
    t[19]=1;
    FORD(i,cnt-1,0){
        int nr=slowo[i];
        //printf("\nnr:%d\n",nr);
        REP(j,l[nr].size()){
            int poz=l[nr][j];
            //printf("%d ",poz);
            t[poz]=(t[poz]+t[poz+1])%10000;
            //printf("%d\n",t[poz]);
        }
    }
    return t[0];

}
void makel(void){
    l[22].PB(0);
    l[4].PB(1);
    l[11].PB(2);
    l[2].PB(3);
    l[14].PB(4);
    l[12].PB(5);
    l[4].PB(6);
    l[27].PB(7);
    l[19].PB(8);
    l[14].PB(9);
    l[27].PB(10);
    l[2].PB(11);
    l[14].PB(12);
    l[3].PB(13);
    l[4].PB(14);
    l[27].PB(15);
    l[9].PB(16);
    l[0].PB(17);
    l[12].PB(18);
}


int main(){
    makel();
    scanf("%d ",&n);
    REP(i,n)
        printf("Case #%d: %04d\n",i+1,solve());
    return 0;
}
