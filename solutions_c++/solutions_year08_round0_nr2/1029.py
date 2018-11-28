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

using namespace std;

struct _train{

	int dep;
	int arr;
};

_train Atrain[101];
_train Btrain[101];
bool Acheck[101];
bool Bcheck[101];

typedef int (*compfn)(const void*, const void*);	

int compare1(struct _train *a , struct _train *b){

	if(a->arr > b->arr)
		return 1;
	else if(a->arr < b->arr)
		return -1;
	else
		return 0;
}

int compare2(struct _train *a , struct _train *b){

	if(a->dep > b->dep)
		return 1;
	else if(a->dep < b->dep)
		return -1;
	else
		return 0;
}

int main(){

	int Aans , Bans;
	int testcase;
	int turn , NA , NB , a , b , c , d;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d",&testcase);

	for(int i=1;i<=testcase;i++){
		Aans = Bans = 0;

		for(int j=0;j<101;j++){			//initialize
			Acheck[j] = Bcheck[j] = 0;
		}

		scanf("%d\n%d %d",&turn,&NA,&NB);

		for(int j=0;j<NA;j++){
			scanf("%d:%d %d:%d",&a,&b,&c,&d);

			Atrain[j].dep = a*60+b;
			Atrain[j].arr = c*60+d;
		}

		for(int j=0;j<NB;j++){
			scanf("%d:%d %d:%d",&a,&b,&c,&d);

			Btrain[j].dep = a*60+b;
			Btrain[j].arr = c*60+d;
		}

		qsort(Atrain,NA,sizeof(struct _train),(compfn)compare1);
		qsort(Btrain,NB,sizeof(struct _train),(compfn)compare2);

		for(int j=0;j<NA;j++){
			Aans++;
			for(int k=0;k<NB;k++){

				if(!Bcheck[k] && Atrain[j].arr + turn <= Btrain[k].dep){
					Bans--;
					Bcheck[k] = 1;
					break;
				}
			}
		}

		qsort(Atrain,NA,sizeof(struct _train),(compfn)compare2);
		qsort(Btrain,NB,sizeof(struct _train),(compfn)compare1);

		for(int j=0;j<NB;j++){
			Bans++;
			for(int k=0;k<NA;k++){

				if(!Acheck[k] && Btrain[j].arr + turn <= Atrain[k].dep){
					Aans--;
					Acheck[k] = 1;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",i,Aans,Bans);

	}
	return 0;
}