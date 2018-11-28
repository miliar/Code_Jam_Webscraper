#include<iostream>
#include<cstdio>

using namespace std;
#define N 19
#define K 109

int T;
int n,k;

struct Tnode{
	int a;
	int b;
};
Tnode p[N];

void solve(){
	int i;
	int j;
	for(i=0;i<n;i++)
		p[i].a= p[i].b = 0;
	p[0].a = 1;
	
	for(i=1;i<=k;i++){
		for(j=0;j<n;j++){
			if(p[j].a==1){
				p[j].b= 1-p[j].b;
			}
		}
		for(j=1;j<n;j++){
			if(p[j-1].a==1 && p[j-1].b==1)
				p[j].a =1;
			else
				p[j].a = 0;
		}
	}
	
	
	if(p[n-1].a==1 && p[n-1].b==1)
		printf("ON\n");
	else
		printf("OFF\n");
}

int main(){
	freopen("A-small-attempt0.in","r+",stdin);
	freopen("1.out","w+",stdout);
	scanf("%d",&T);
	int i;
	for(i=1;i<=T;i++){
		scanf("%d %d",&n,&k);
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}