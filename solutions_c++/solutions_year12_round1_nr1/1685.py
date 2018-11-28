#include <stdio.h>
#include <conio.h>
FILE *fin;
FILE *fout;



int t,count,a,b;
float pUntil[100001];
float exDel[100001];
float exEnter;
int main(int argc, char* argv[])
{
	fin = fopen("A-small2.in","r");
	fout = fopen("A-small2.out","w");
	
	fscanf(fin,"%d",&t);
	for(int i=0;i<t;i++)
	{
		fscanf(fin,"%d %d",&a,&b);
		pUntil[0] = 1;
		for(int j=1;j<=a;j++)
		{
			fscanf(fin,"%f",&(pUntil[j]));
			pUntil[j] = pUntil[j]*pUntil[j-1];
		}
	
			// keep typing 
			float exKeep = pUntil[a]*(b-a+1.0f) + (1.0f -  pUntil[a]) * (b + b - a + 2);
			//printf("%f\n", exKeep);
			// delete n char
			float minExp = exKeep;
			for(int j=0;j<a;j++)
			{
				float correct = pUntil[j]*(a-j+b-j+1) ;
				float wrong = (1.0f -  pUntil[j]) * (a-j+b-j+2+b);
				exDel[j] =  correct + wrong;
				//printf(" %f %f %f\n", correct , wrong,exDel[j]);
				if(exDel[j]<minExp)
					minExp =exDel[j];
			}
			// enter
			exEnter = b+2;
			//	printf("%f \n", exEnter);
			if(exEnter<minExp)
				minExp=exEnter;

		fprintf(fout,"Case #%d: %f\n",i+1,minExp);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}