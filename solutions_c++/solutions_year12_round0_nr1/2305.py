#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<list>
#include<queue>
#include<set>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

const int MAXN=110;
const int MAXT=100;

char fir[3][MAXN];
char sec[3][MAXN];
int fro[3];
int fse[3];
map<char,char> mapa;

void set_map(){
    mapa.insert(pair<char,char>('q','z'));
    mapa.insert(pair<char,char>('z','q'));
    char c;
    REP(i,3){
        c='p';
        int j=0;
        while (c!='\n'){
            scanf("%c",&c);
            fir[i][j]=c;
            j++;
        }
        fro[i]=j;
    }
    REP(i,3){
        c='p';
        int j=0;
        while (c!='\n'){
            scanf("%c",&c);
            sec[i][j]=c;
            j++;
        }
        fse[i]=j;
    }
    REP(i,3){
        REP(e,fro[i])
            mapa.insert(pair<char,char>(fir[i][e],sec[i][e]));
    }
}

void obsluz(){
    char w[MAXN];
    char c='p';
    int j=0;
    while (c!='\n'){
        scanf("%c",&c);
        w[j]=c;
        j++;
    }
    REP(i,j){
        printf("%c",mapa[w[i]]);
    }
}

int t;

int main(){
    set_map();
    scanf("%d",&t);
    scanf(" ");
    REP(i,t){
        printf("Case #%d: ",i+1);
        obsluz();
    }
}
