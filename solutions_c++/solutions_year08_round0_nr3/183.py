#include <stdio.h>
#include <string.h>
#include <Math.h>
#include <stdlib.h>

double ncut(double pR,double pv)
{
	double res1;
	
	res1 = pR * pR - pv * pv;
	if(res1<0)
	{
		printf("ncut less than zero\n");
		exit(0);
	}
	res1 = sqrt(res1);
	
	return res1;
}

double curve(double pR, double psx, double psy, double pex, double pey)
{
	double ang1, ang2, ang3, res1,dist1, diffx, diffy, shrtdist, bigarea, trgarea, diffarea, innerarea;
	
	diffx = pex - psx;
	diffx = diffx * diffx;
	
	diffy = pey - psy;
	diffy = diffy * diffy;
	
	dist1 = diffx + diffy;
	dist1 = 0.5 * sqrt(dist1);
	
	shrtdist = pR * pR - dist1 * dist1;
	shrtdist = sqrt(shrtdist);
	
	ang1 = acos(psy/pR);
	ang2 = acos(pey/pR);
	
	ang3 = ang1 - ang2;
	
	if(ang3 < 0)
		ang3 = ang3 * -1.0;
	
	ang3 = ang3 / (2.0 * M_PI);
	
	bigarea = M_PI * pR * pR * ang3;
	trgarea = dist1 * shrtdist;
	diffarea = bigarea - trgarea;
	innerarea = 0.5 * sqrt(diffx) * sqrt(diffy);
	
	res1 = innerarea + diffarea;
	
	return res1;
}

double blcut(double pR, double psx, double psy, double pex, double pey)
{
	double ty,tx, res1;
	
	tx = ncut(pR,psy);
	ty = ncut(pR,psx);
	res1 = curve(pR,psx, ty, tx, psy);
	
	/*
	printf(",%f,%f\n",psx,psy);
	printf(",%f,%f\n",psx,pey);
	printf(",%f,%f\n",pex,pey);
	printf(",%f,%f\n",pex,psy);
	printf(",%f,%f\n",psx,ty);
	printf(",%f,%f\n",tx,psy);
	 */
	
	return res1;
}

double btcut(double pR, double psx, double psy, double pex, double pey)
{
	double tx1,tx2, res1;
	
	tx1 = ncut(pR,psy);
	tx2 = ncut(pR,pey);
	res1 = curve(pR,tx1, psy, tx2, pey);
	res1 = res1 + (tx2-psx) * (pey - psy);
	
	/*
	printf(",%f,%f\n",psx,psy);
	printf(",%f,%f\n",psx,pey);
	printf(",%f,%f\n",pex,pey);
	printf(",%f,%f\n",pex,psy);
	printf(",%f,%f\n",tx1,psy);
	printf(",%f,%f\n",tx2,pey);
	*/
	return res1;
}

double lrcut(double pR, double psx, double psy, double pex, double pey)
{
	double ty1,ty2, res1;
	
	ty1 = ncut(pR,psx);
	ty2 = ncut(pR,pex);
	res1 = curve(pR,psx, ty1, pex, ty2);
	res1 = res1 + (pex - psx) * (ty2 - psy);
	
	/*
	printf(",%f,%f\n",psx,psy);
	printf(",%f,%f\n",psx,pey);
	printf(",%f,%f\n",pex,pey);
	printf(",%f,%f\n",pex,psy);
	printf(",%f,%f\n",psx,ty1);
	printf(",%f,%f\n",pex,ty2);
	*/
	return res1;
}

double trcut(double pR, double psx, double psy, double pex, double pey)
{
	double tx,ty, res1;
	
	tx = ncut(pR,pey);
	ty = ncut(pR,pex);
	
	res1 = curve(pR,tx,pey,pex,ty);
	res1 = res1 + (tx-psx)*(pey-psy) + (pex-tx)*(ty-psy);
	
	/*
	printf(",%f,%f\n",psx,psy);
	printf(",%f,%f\n",psx,pey);
	printf(",%f,%f\n",pex,pey);
	printf(",%f,%f\n",pex,psy);
	printf(",%f,%f\n",tx,pey);
	printf(",%f,%f\n",pex,ty);
	*/
	return res1;
}

int main(int argc, char **argv)
{
	int cCnt;
	int i,j,k,l;
	double vf, vR1, vt, vr2, vg, pR, tex, tey, dist1, dist2, total, ty,tx,res1,tmx,tmy;
	
	scanf("%d",&cCnt);
	for(i=0;i<cCnt;i++)
	{
		scanf("%lf",&vf);
		scanf("%lf",&vR1);
		scanf("%lf",&vt);
		scanf("%lf",&vr2);
		scanf("%lf",&vg);
		
		//printf("%f,%f,%f,%f,%f\n",vf,vR1,vt,vr2,vg);
		
		ty = vr2;
		pR = vR1 - vt - vf;
		res1 = 0;
		
		if(vg - 2.0 * vf > 0)
		{
			
			tmy = ty + vf;
			tmy = tmy * tmy;
			while(ty+vf< pR)
			{
				tx = vr2;
				tey = ty + vg - vf;
				tmx = tx + vf;
				tmx = tmx * tmx;
				while(tmy + tmx<pR*pR)
				{
					tex = tx + vg - vf;
					dist1 = sqrt(tex * tex + tey * tey);
					if(dist1<pR)
					{
						res1 += (vg - 2.0 * vf) * (vg - 2.0 * vf);
						
						/*
						printf("toot,0,0\n");
						printf(",%f,%f\n",tx+vf,ty+vf);
						printf(",%f,%f\n",tx+vf,tey);
						printf(",%f,%f\n",tex,tey);
						printf(",%f,%f\n",tex,ty+vf);*/
					}else{
						dist1 = sqrt((tx+vf) * (tx+vf) + tey * tey);
						dist2 = sqrt(tex * tex + (ty+vf) * (ty+vf));
						if(dist1<pR && dist2<pR)
						{
							//printf("trrt,0,0\n");
							res1 += trcut(pR,tx+vf,ty+vf,tex,tey);
							//printf("%f\n",res1);
						}else if(dist2<pR)
						{
							//printf("lrrt,0,0\n");
							res1 += lrcut(pR,tx + vf,ty+vf,tex,tey);
							//printf("%f\n",res1);
						}else if(dist1<pR)
						{
							//printf("btrt,0,0\n");
							res1 += btcut(pR,tx + vf,ty+vf,tex,tey);
							//printf("%f\n",res1);
						}else{
							//printf("blrt,0,0\n");
							res1 += blcut(pR,tx + vf,ty+vf,tex,tey);
							//printf("%f\n",res1);
						}
					}
					
					tx = tx + vg + 2.0 * vr2;
					tmx = tx + vf;
					tmx = tmx * tmx;
				}
				ty = ty + vg + 2.0 * vr2;
				tmy = ty + vf;
				tmy = tmy * tmy;
			}
		}
		//printf("total%f\n",(M_PI * vR1 * vR1));
		res1 = res1 * 4.0;
		total = 1.0 - res1 / (M_PI * vR1 * vR1);
		printf("Case #%d: %f\n", i+1, total);
	}
}

