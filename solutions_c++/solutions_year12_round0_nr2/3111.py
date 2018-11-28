#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<functional>

#define MAXN 105
#define MAXL 35
using namespace std;

struct st{
	int a,b,c;
	st(int x,int y,int z): a(x),b(y),c(z){ }
	st(): a(0), b(0), c(0) { }
};

int A[MAXN];
st St[MAXL],Nt[MAXL];

void gen()
{
	for(int i=0;i<=10;i++){
		for(int j=i;j<=10;j++){
			if(j-i > 2) break;
			for(int k=j;k<=10;k++){
				if(k-j > 2) break;
				if(k-i > 2) break;
				if(i+j+k > 30) continue;
				
				if(k-j == 2 || k-i == 2 || j-i == 2){
					St[i+j+k] = st(i,j,k);
				}else{
					Nt[i+j+k] = st(i,j,k);
				}
			}
		}
	}
}

int main()
{
	freopen("tc.in","r",stdin);
	freopen("tc.out","w",stdout);
	gen();

	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++){
		int N,S,p,i,j;
		scanf("%d %d %d",&N,&S,&p);
		for(i=0;i<N;i++){
			scanf("%d",&A[i]);
		}

		sort(A,A+N,greater<int>());
		
		int cnt = 0;
		for(i=0;i<N;i++){
			if(Nt[ A[i] ].c >= p) cnt++;
			else if(S > 0 && St[ A[i] ].c >= p){
				cnt++;
				S--;
			}
		}
		
		printf("Case #%d: %d\n",k,cnt);
	}
	return 0;
}