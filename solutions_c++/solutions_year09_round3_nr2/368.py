#include<cstdio>
#include<cmath>

double pos[600],vel[600];
double X,Y,Z,Vx,Vy,Vz;
int N;

double minT(){
	double a1 = -(X*Vx+Y*Vy+Z*Vz);
	double a2 = Vx*Vx + Vy*Vy+ Vz*Vz;
	//printf("t = %lf//%lf == %lf\n",a1,a2,a1/a2);
	return a1/a2;
}

double minD(double t){
	double aux;
	aux = (X+Vx*t)*(X+Vx*t) + (Y+Vy*t)*(Y+Vy*t) + (Z+Vz*t)*(Z+Vz*t);
	aux = aux/(N*N);
	return sqrt(aux);
}

int main(){
	int i,j,k=1;
	int cases;
	//double X,Y,Z,Vx,Vy,Vz,t,d;
	double t,d;
	scanf("%d\n",&cases);
	while(cases--){
		scanf("%d\n",&N);
		X = Y = Z = Vx = Vy = Vz = 0.00;
		for(i=0;i<N;i++){
			for(j=0;j<6;j++){
				scanf("%lf\n",&pos[j]);
			}
			X+= pos[0];
			Y+= pos[1];
			Z+= pos[2];
			Vx+= pos[3];
			Vy+= pos[4];
			Vz+= pos[5];
		}
		//printf("%lf %lf %lf %lf %lf %lf\n",X,Y,Z,Vx,Vy,Vz);
		if(Vx == 0.0 && Vy == 0.0 && Vz == 0.0)
			t = 0.0;
		else t = minT();
		if (t < 0.0){
			t = 0.0;
		}
		d = minD(t);
		printf("Case #%d: %.8lf %.8lf\n",k++,d,t);
	}
	
}
