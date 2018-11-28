#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
 
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second

#define DEBUG 0
#define max_n 1005

int n,pom;
int a,b;
int r[max_n];
int pozx[max_n];
int pozy[max_n];
bool wybrany[max_n];
vector<PII> lam;
VI wys;

int wybierz(){
    int v;
    FOR(i,0,n) if(wybrany[i]==false) v = i;
    FOR(i,0,n) if(wybrany[i]==false && r[i]>r[v]) v=i;
    wybrany[v]=true;
    return v;
}

int znajdzmin(){
    int mini = wys[0];
    int dla = 0;
    FOR(i,0,wys.size()){
        if(wys[i]<mini){
            mini = wys[i];
            dla = i;
        }
    }
    return dla;
}

void update(int x,int y,int r){
    vector<PII> newlam; newlam.clear();
    vector<int> newh; newh.clear();
    FOR(i,0,lam.size()){
        if(lam[i].nd > x && lam[i].st < x){
            newlam.pb(mp(lam[i].st,x)); newh.pb(wys[i]);
            newlam.pb(mp(x,lam[i].nd)); newh.pb(wys[i]);
        }
        else{
            newlam.pb(lam[i]); newh.pb(wys[i]);
        }
    }
    lam = newlam; wys = newh; newlam.clear(); newh.clear();
    FOR(i,0,lam.size()){
        if(lam[i].st < y && lam[i].nd > y){
            newlam.pb(mp(lam[i].st,y)); newh.pb(wys[i]);
            newlam.pb(mp(y,lam[i].nd)); newh.pb(wys[i]);
        }
        else{
            newlam.pb(lam[i]); newh.pb(wys[i]);
        }
    }
    lam = newlam; wys = newh; newlam.clear(); newh.clear();
    FOR(i,0,lam.size()){
        if(lam[i].st >= x && lam[i].nd <=y){
            if(wys[i]<r) wys[i]=r;
        }
    }

}

void wypisz(){
    FOR(i,0,lam.size()){
        printf("%d %d na wys :%d\n",lam[i].st,lam[i].nd,wys[i]);
    }
    printf("\n"); 
}

int main(){
    int Z; scanf("%d",&Z);
    FOR(z,1,Z+1){
        scanf("%d%d%d",&n,&a,&b);
        FOR(i,0,n) scanf("%d",&r[i]);
        FOR(i,0,n) wybrany[i]=false;
        lam.clear(); wys.clear();
        lam.pb( mp(0,a));
        wys.pb(0);
        FOR(i,0,n){
            int v = wybierz();
            int dla = znajdzmin();
            pozx[v] = lam[dla].st;
            pozy[v] = wys[dla];
            update(pozx[v]-2*r[v],pozx[v]+2*r[v],pozy[v]+2*r[v]);
            //wypisz();         
        }

        printf("Case #%d:",z);
        FOR(i,0,n) printf(" %d %d",pozx[i],pozy[i]);
        printf("\n");
        
    }
}
