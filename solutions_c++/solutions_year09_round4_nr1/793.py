#include <cstdlib>
#include <cstdio>
#include <cmath>

int n;
int T[50];
int N[50];
char c;
int num;
int re;
int tmp;
int po;
int kier;

int main(){
	int d;
	scanf("%d", &d);
	for(int z=1; z<=d; z++){
		scanf("%d\n", &n);
		for(int i=0; i<n; i++){
			T[i]=0;
			for(int j=0; j<n; j++){
				scanf("%c", &c);
				if(c=='1') T[i]=j;
			}
			scanf("%c", &c);
		}

		//for(int i=0; i<n; i++) printf("%d ", T[i]);
		//printf("\n");
		
		num=0;
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
				if(T[j]<=i){N[j]=i; T[j]=n+1; break;}
		
		//for(int i=0; i<n; i++) printf("%d ", N[i]);
		//printf("\n");
		re=0;
		for(int i=n-1; i>=0; i--)
			for(int j=0; j<n; j++){
				if(N[j]==i){
					po=j;
					while(po!=i){
						re++;
						tmp=N[po];
						N[po]=N[po+1];
						N[po+1]=tmp;
						po++;
					}
				} 
			}
		printf("Case #%d: %d\n", z, re);
	}
}
