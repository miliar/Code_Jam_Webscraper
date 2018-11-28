#include<stdio.h>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<algorithm>

using namespace std;
int p0[3],v[3];
double xx[3];

int vet(int u[3],int w[3]){
	int resp=0,i;
	for(i=0;i<3;i++)
		resp += u[i]*w[i];
	return resp;
}

double norma(double u[3]){
	int i;
	double soma=0;
	
	for(i=0;i<3;i++)
		soma += u[i]*u[i];
		
	return sqrt(soma);
}

int main(){

	int i,j,T,count,n,x,y,z,vx,vy,vz;
	double t,tmin,dmin;
	
	scanf("%d ",&T);
	int tot = T;
	while(T--){
		scanf("%d",&n);
		p0[0] = p0[1] = p0[2] = 0;
		v[0] = v[1] = v[2] = 0;
		for(i=0;i<n;i++){
			scanf("%d %d %d %d %d %d",&x,&y,&z,&vx,&vy,&vz);
			p0[0] += x;
			p0[1] += y;
			p0[2] += z;
			v[0] += vx;
			v[1] += vy;
			v[2] += vz;
		}
		
		t = vet(p0,v);
		int aux = vet(v,v);
		if(aux != 0)
			t /= vet(v,v);
		
		t = -t;
		
		
		if(t < 0)
			tmin = 0;
		else
			tmin = t;
			
		
		for(i=0;i<3;i++)
			xx[i] = (double)p0[i] + tmin*v[i];
			
		dmin = norma(xx)/n;

		
		
		printf("Case #%d: %.8f %.8f\n",tot-T,dmin,tmin);
	}

	return 0;
}
