#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <vector>
#define A (0)
#define B (1)
#define MAXN 500
#define min jskd

using namespace std;

typedef struct {int depart;int arrive;int from;} card;

bool cf(const card abc,const card def) {
	return abc.depart < def.depart;
	}

struct pq_s {
	bool operator() (const int abc,const int def) {
		return abc > def;
		}
	};


	
card jadwal[MAXN];
int a,b,c,d,e,f;
int jml[2];
int min[2];
int jmlcase;
int progress;
int n[2];
card dumi,sugus;


int main() {
	scanf("%d",&jmlcase);
	for (e = 0;e < jmlcase;e++) {
		scanf("%d%d%d\n",&progress,&n[A],&n[B]);
		min[A] = min[B] =jml[A] = jml[B] = 0;
	priority_queue<int,vector<int>,pq_s> pq[2];
	int susu = 0;
	for (a = 0;a < 2;a++) {
		dumi.from = a;
		for (b = 0;b < n[a];b++) {
			c = 0;
			char du = getchar();
			while (du != ':') {
				c *= 10;
				c += (du - '0');
				du = getchar();
				}

			scanf("%d",&d);
			d += (c * 60);
			
			dumi.depart = d;
			getchar();
			//printf("%d\n",d);
			c = 0;
			du = getchar();
			while (du != ':') {
				c *= 10;
				c += (du - '0');
				du = getchar();
				}

			scanf("%d\n",&d);
			d += (c * 60);
			
			dumi.arrive = d;
			//printf("%d\n",d);
			//printf("%d %d\n",dumi.depart,dumi.arrive);
			jadwal[susu] = dumi;
			susu++;
			}
		}
	
	sort(jadwal,jadwal + susu,cf);
	
	for (a = 0;a < susu;a++) {
	//	printf("susu\n");
		sugus = jadwal[a];
		int dari = sugus.from;
		int berangkat = sugus.depart;
	//	printf("%d %d\n",sugus.depart,sugus.arrive);
		//printf("%d\n",berangkat);
		while (!pq[dari].empty()) {
			//printf("top : %d\n",pq[dari].top());
			if (pq[dari].top() > berangkat) break;
			jml[dari]++;
			pq[dari].pop();
			}
		//printf("%d %d\n",dari,jml[dari]);
		pq[(dari + 1) % 2].push(sugus.arrive + progress);
		if (jml[dari] > 0) {
			jml[dari]--;
			continue;
			}
		min[dari]++;
		}
	
	printf("Case #%d: %d %d\n",e + 1,min[0],min[1]);
	
	
	}	
			
		
	return 0;
	}
