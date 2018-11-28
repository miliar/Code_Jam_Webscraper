#include<cstdio>
using namespace std;
int v[1005],k2,nrp,nr,t,i,a,b,k=1,j,aux;
void perm(int j){
	aux=j;
	nrp=0;
	if(v[j]==0){
		do{
			j+=k*(j%10);
			j/=10;
			if(j>aux && j<=b){
			v[j]=1;
			++nrp;
			}
		} while(j!=aux);
		if(nrp==1){
			++nr;
		}
		if(nrp==2){
			nr+=3;
		}
	}
}
int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		scanf("%d%d",&a,&b);
		aux=a;
		k=1;
		while(aux!=0){
			aux/=10;
			k*=10;
		}
		k2=k*10;
		nr=0;
		for(j=a;j<=b;++j){
			perm(j);
		}
		printf("Case #%d: ",i);
		printf("%d\n",nr);
		for(int x=1;x<=1004;++x){
			v[x]=0;
		}
	}
	return 0;
}