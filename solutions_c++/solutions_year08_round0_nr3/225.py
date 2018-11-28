#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846

int main(int argc, char *argv[])
{
	int i,n;
	double j,k,x1,x2,y1,y2;
	double f,R,t,r,g,answer,theta;
	double inR,inR2,recArea,recAreas;
	char strBuff[256];
	FILE *fp,*fp_out;

	if((fp=fopen("C-Large.in","r"))==NULL)return -1;
	if((fp_out=fopen("C-Large-out.txt","w"))==NULL)return -1;

	fgets(strBuff,256,fp);
	n=atoi(strBuff);
	for(i=0;i<n;i++){
		fscanf(fp,"%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);

		inR=R-t-f;
		if(inR>0 && g>f*2){
			recAreas=0;
			inR2=inR*inR;
			g-=f*2;
			r+=f;
			recArea=g*g;
			for(j=r;j<inR;j+=g+2*r){
				for(k=r;j*j+k*k<inR2;k+=g+2*r){
					if((j+g)*(j+g)+(k+g)*(k+g)<inR2){
						recAreas+=recArea;
					}else{
						if(j*j+(k+g)*(k+g)<inR2){
							if((j+g)*(j+g)+k*k<inR2){
								y1=k+g;
								x1=sqrt(inR2-y1*y1);
								x2=j+g;
								y2=sqrt(inR2-x2*x2);
								recAreas+=g*g-(y1-y2)*(x2-x1)/2;
							}else{
								y1=k;
								x1=sqrt(inR2-y1*y1);
								y2=k+g;
								x2=sqrt(inR2-y2*y2);
								recAreas+=(x1+x2-j*2)*g/2;
							}
						}else{
							if((j+g)*(j+g)+k*k<inR2){
								x1=j;
								y1=sqrt(inR2-x1*x1);
								x2=j+g;
								y2=sqrt(inR2-x2*x2);
								recAreas+=(y1+y2-k*2)*g/2;
							}else{
								x1=j;
								y1=sqrt(inR2-x1*x1);
								y2=k;
								x2=sqrt(inR2-y2*y2);
								recAreas+=(y1-y2)*(x2-x1)/2;
							}
						}
						theta=acos((x1*x2+y1*y2)/inR2);
						recAreas+=inR2*theta/2-inR2*sin(theta/2)*cos(theta/2);
					}
				}
			}
			recAreas*=4;
			answer=(PI*R*R-recAreas)/(PI*R*R);
		}else{
			answer=1.0;
		}

		printf("Case #%d: %f\n",i+1,answer);
		fprintf(fp_out,"Case #%d: %f\n",i+1,answer);
	}
	//printf("Finished!\n");
	fclose(fp);
	fclose(fp_out);
	
	getchar();
}
