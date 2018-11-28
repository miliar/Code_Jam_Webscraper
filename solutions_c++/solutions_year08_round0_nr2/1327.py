#include <cstdio>
#include <cstdlib>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <cctype>
using namespace std;
#define ready 1
#define dep 2
struct tev{
	int type;
	int time;
	int par;
	bool operator <(tev par) const {
		if (time!=par.time) return time<par.time;
		return type<par.type;
	}
};
int sc, nsc;
int na, nb, t;
tev ev[1010];
int nev;
void readtime(int &res){
	int h, m;
	scanf(" %d : %d ", &h, &m);
	res=h*60+m;
}
void init(){
	int p;
	int i;
	scanf("%d%d%d", &t, &na, &nb);
	nev=0;
	for(i=1;i<=na;i++){
		readtime(p);
		nev++;
		ev[nev].type=dep;
		ev[nev].par=1;
		ev[nev].time=p;
		readtime(p);
		p+=t;
		nev++;
		ev[nev].type=ready;
		ev[nev].par=2;
		ev[nev].time=p;
	}
	for(i=1;i<=nb;i++){
		readtime(p);
		nev++;
		ev[nev].type=dep;
		ev[nev].par=2;
		ev[nev].time=p;
		readtime(p);
		p+=t;
		nev++;
		ev[nev].type=ready;
		ev[nev].par=1;
		ev[nev].time=p;
	}
}
void solve(){
	int i;
	int resa, resb;
	int na, nb;
	resa=resb=0;
	na=nb=0;
	sort(ev+1, ev+nev+1);
	for(i=1;i<=nev;i++){
		if (ev[i].type==ready){
			if (ev[i].par==1) na++;
			else if (ev[i].par==2) nb++;
		}
		else{
			if (ev[i].par==1){
				if (na==0) resa++;
				else na--;
			}
			else if (ev[i].par==2){
				if (nb==0) resb++;
				else nb--;
			}
		}
	}
	printf("Case #%d: %d %d\n", sc, resa, resb);
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &nsc);
	for(sc=1; sc<=nsc; sc++){
		init();
		solve();
	}
	return 0;
}