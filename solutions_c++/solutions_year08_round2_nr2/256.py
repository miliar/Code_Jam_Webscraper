#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<queue>

using namespace std;

#define MP make_pair
#define PB push_back
#define FT first
#define SD second

int tab[1010];
int prime[100000];
int ile=1;
bool pp[1010];
int c, a, b, p;
int ca=0;
int t;
int u,v;


void un(int x, int y){
	tab[y]=x;
}

int f(int x){
	while(tab[x]!=-1){
		x=tab[x];
	}
	return x;
}

void sito(){
	pp[2]=1;
	prime[0]=2;
	for(int i=3;i<1010;i+=2){
		if(pp[i]==false){
			prime[ile++]=i;
			for(int j=i*i;j<1010;j+=i){
				pp[j]=1;
			}
		}
	}
}


int main(){
	scanf("%d",&c);
	sito();
	while(c--){
		ca++;
		scanf("%d %d %d",&a,&b,&p);
		for(int i=a;i<=b;i++){
			tab[i-a]=-1;
		}
		int s = 0;
		while(prime[s]<p) s++;
		while(prime[s]<=b){
			//printf("%d\n",prime[s]);
			t = (a+prime[s]-1)/prime[s];
			t = t * prime[s];
			v = f(t-a);
			for(int i=t;i<=b;i+=prime[s]){
				u=f(i-a);
				if(u!=v){
					un(v,u);
				}
			}
			s++;
		}
		int ilosc=0;
		for(int i=0;i<=b-a;i++){
			if(tab[i]==-1) ilosc++;
		}
		printf("Case #%d: %d\n",ca,ilosc);
	}
	return 0;
}

