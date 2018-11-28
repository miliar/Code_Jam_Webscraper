#include<stdio.h>
#include<string.h>
#include<math.h>
#define err 1e-8
int n;
double posx, posy, posz;
double velx, vely, velz;

void work()
{
		double a0 = posx*posx + posy*posy + posz*posz; 
		double a1 = 2*posx*velx + 2*posy*vely + 2*posz*velz;
		double a2 = velx*velx + vely*vely + velz*velz;
		
		double kx = a1;
		double ky = 2*a2;
		if(fabs(ky)<=err)
		{
			double tm = sqrt(posx*posx + posz*posz + posy*posy) / n;
			double dm = 0;
			printf("%.8lf %.8lf\n",tm,dm);
		}
		else
		{
			double t= -kx/ky;
			
			if(t > 0 )
			{
				double tx = posx + t*velx;
				double ty = posy + t*vely;
				double tz = posz + t*velz;
				double tm = sqrt(tx*tx + ty*ty + tz*tz) / n;
				double temp = sqrt(posx*posx + posz*posz + posy*posy) / n;
				double dm = 0;
				if(tm < temp){
					printf("%.8lf %.8lf\n", tm,t);
				}else{
				 	printf("%%.8lf %.8lf\n", temp,dm);
			  	}
			}
			else
			{
				double tm = sqrt(posx*posx + posz*posz + posy*posy) / n;
				double dm = 0;
				printf("%.8lf %.8lf\n",tm,dm);
			}
					
		}
}

int main()
{
	int tcase;
	freopen("blin.txt", "r", stdin);
	freopen("blout1.txt", "w", stdout);
	scanf("%d",&tcase);
	for(int i = 1; i <= tcase; i++){
		scanf("%d",&n);
		posx = posy = posz  = 0;
		velx = vely = velz = 0;
		double p1, p2, p3, v4, v5, v6;
			
		for(int j = 0; j < n; j++){
			scanf("%lf %lf %lf %lf %lf %lf", &p1,&p2,&p3,&v4,&v5,&v6);
			posx += p1;
			posy += p2;
			posz += p3;
			velx += v4;
			vely += v5;
			velz += v6;
		}
		printf("Case #%d: ",i);
		work();
	}
	return 0;
}

