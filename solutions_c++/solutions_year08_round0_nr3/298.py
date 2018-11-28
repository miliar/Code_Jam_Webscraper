#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>



void main()
{
	FILE * fileIn = NULL,* fileOut = NULL;
	if (NULL == (fileIn = fopen("d:\\small.in","r")))
	{
		return;
	}
	if (NULL == (fileOut = fopen("d:\\small.out","w")))
	{
		return;
	}
	
	int nCase = 0;
	char line[200];
	fgets(line,200,fileIn);
	sscanf(line,"%d",&nCase);
	double P = 0;
	double f = 0,R = 0,t = 0,r = 0,g = 0;
	double pi = 3.1415926535;
	double sSum;
	
	
	
	
	for (int i = 0;i<nCase;i++)
	{		
		printf("-----Case %d: -----\n",i+1);
		fgets(line,200,fileIn);
		sscanf(line,"%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		t = t+f;
		g = g - 2*f;
		r = r + f;
		if (g<= 0)
		{
			P = 1;
			printf("Case #%d: %.6lf\n",i+1,P);
			fprintf(fileOut,"Case #%d: %.6lf\n",i+1,P);
			continue;
		}
		
		//四分之一圆面积
		sSum = pi*R*R/4;
		
		//
		//苍蝇生存活动面积
		//
		
		//完整正方形面积		
		double sFull = 0;
		
		
		//非完整正方形面积
		double sAdd = 0;
		
		double h = 0;		
		R = R-t;
		h = r;
		while(h<R)
		{		
			int nFull = 0;
			if (h+g<R)
			{
				nFull = (int)((sqrt(R*R - (h+g)*(h+g))+r)/(2*r+g));
				
			}			
			if (nFull<0)
			{
				nFull = 0;
			}
			sFull += nFull * g * g;
			while(nFull*(2*r+g)+r<R)
			{
				double D = 0;
				D = sqrt(R*R - h*h);
				double a = 0,b = 0,c = 0,d = 0;
				double D0 = 0;			
				D0 = nFull*(2*r+g)+r;
				c = D - D0;
				if (c<0)
				{
					c = 0;
				}
				if (c>g)
				{
					c = g;
					d = sqrt(R*R - (D0+g)*(D0+g)) - h;
					if (d<0)
					{
						d = 0;
					}
					
				}
				else
				{
					d = 0;
				}
				
				b = sqrt(R*R - D0*D0) - h;
				if (b< 0)
				{
					b = 0;
				}
				if (b>g)
				{
					b = g;
					a = sqrt(R*R - (h+g)*(h+g))-D0;	
					if (a<0)
					{
						a = 0;
					}
				}
				else
				{
					a = 0;
				}
				
				double l = 0;
				l = sqrt((b-d)*(b-d) + (c-a)*(c-a));
				double sSi = 0;
				sSi = c*b - (b-d)*(c-a)/2;
				double sSan = 0 ,hSan = 0;
				hSan = sqrt(R*R - l*l/4);
				sSan = l*hSan/2;
				double sSanXing = 0;
				//	sSanXing = pi*R*R*(asin(l/2/R)*2/2/pi);
				sSanXing = R*R*asin(l/2/R);
				sAdd += sSanXing - sSan + sSi;
				
				nFull++;
			}
			
			
			
			
			h += g+2*r;
		}
		
		
		
		
		P = 1 - (sFull + sAdd)/sSum;		
		
		printf("Case #%d: %.6lf\n",i+1,P);
		fprintf(fileOut,"Case #%d: %.6lf\n",i+1,P);
	}
	fclose(fileIn);
	fclose(fileOut);
	
}