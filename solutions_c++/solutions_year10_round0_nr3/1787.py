#include<cstdio>
#define FOR(a,b) for(int a=0;a<b;++a)

int t[1000];
int mem[3][1000];

int main(){
	int x,z,a,b,c;
	scanf("%d",&z);
	FOR(x,z){
		printf("Case #%d: ",x+1);
		scanf("%d %d %d", &a, &b, &c);
		long long wyn = 0,tmp=0;
		FOR(i,c){scanf("%d",&t[i]); tmp+=t[i]; mem[0][i]=-1;}
		if(tmp<=b){printf("%lld\n",tmp*a); continue;}
		int wsk=0,last;
		while(a--){
			tmp=0;
			last = wsk;
			if(mem[0][wsk]!=x){
				while(tmp+t[wsk]<=b){
					tmp+=t[wsk];
					++wsk;
					if(wsk==c) wsk=0;
				}
				wyn+=tmp;
				mem[0][last]=x;
				mem[1][last]=tmp;
				mem[2][last]=wsk;
			}else{
				wyn += mem[1][last];
				wsk = mem[2][last];
			}
		}
		printf("%lld\n",wyn);
	}
}
// a - ilosc przejazdów, b - pojemnośc kolejki, c - liczba grup
/*
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3

Case #1: 21
Case #2: 100
Case #3: 20

*/
