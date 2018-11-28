#include<stdio.h>

#define MAX 1005

int par[MAX];

int gcd(int x,int y){
	int r;
	while(1){
		r = x%y;
		if(!r)	return y;
		x=y;
		y=r;
	}
}

int s[MAX],k;

int root(int x){
	s[k++] = x;
	if(par[x]==x)
		return x;
	return root(par[x]);
}
	int a,b,p;

void Union(int i,int j){
	int ri,rj;
	k=0;

	ri = root(i);
	for(k--;k>=0;k--)
		par[s[k]] = ri;
	
	k = 0;
	rj = root(j);
	for(k--;k>=0;k--)
		par[s[k]] = rj;

	par[ri] = rj;

//	for(i=a;i<=b;i++)
//		printf(">>> %d %d\n",i,par[i]);
}

char ss[MAX];
int np,pr[MAX];

void gen(){
	int i,j;

	np = 1;
	pr[0] = 2;

	for(i=3;i*i<MAX;i+=2){
		if(!ss[i]){
			pr[np++] = i;
			for(j=i*i;j<MAX;j+=2*i)
				ss[j] = 1;
		}
	}
	for(;i<MAX;i+=2)
		if(!ss[i])
			pr[np++] = i;

//	printf(">> %d\n",np);
}

int main(){

	int N,T;
	int i,j,l;//,g;

	gen();

	scanf("%d",&T);

	for(N=1;N<=T;N++){
		
		scanf("%d%d%d",&a,&b,&p);

		for(i=a;i<=b;i++)
			par[i] = i;

		for(i=a;i<=b;i++)
			for(j=i+1;j<=b;j++){

				for(l=np-1;l>=0 && pr[l]>=p;l--){
					if(i%pr[l]==0 && j%pr[l]==0)
						break;
				}

				if(l>=0 && pr[l] >= p)
					Union(i,j);

/*				g = gcd(i,j);
				if(p==2 && g%2==0){
					Union(i,j);
					continue;
				}

				while(g%2==0)
					g/=2;

				for(l=1;l<np && pr[l]*pr[l] <= g;l++){
					
				}*/
//				for(l=0;l<np;l++)
				//if(gcd(i,j) >= p)
				//	Union(i,j);
			}

		j = 0;
		for(i=a;i<=b;i++)
			if(par[i]==i)
				j++;

		printf("Case #%d: %d\n",N,j);
	}

	return 0;
}