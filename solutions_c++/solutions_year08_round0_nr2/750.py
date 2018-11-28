#include <stdio.h>
#include <string.h>
const int MAX = 2000;
/*
2
5
3 2
09:00 12:00
10:00 13:00
11:00 12:30
12:02 15:00
09:00 10:30
2
2 0
09:00 09:01
12:00 12:02
*/

void sort(int* a, int c)
{
	int t;
	for(int i=1;i<c;i++)
		for(int j=i-1;(j>=0)&&(a[j+1]<a[j]);j--)
		{
			t = a[j+1];
			a[j+1] = a[j];
			a[j] = t;
		}
}
int solve(int* depatures, int* arrivals, int dc, int ac, int T)
{
	sort(depatures,dc);
	sort(arrivals,ac);
	int MAXLevel = 0;
	int Current = 0;
	int i=0,j=0;
	while (i<dc) {
		if (j==ac) { //Only depatures left
			if( (dc-i)>Current ) // Available trains insufficient
				MAXLevel += ((dc-i) - Current);
			break;
		}

		if (arrivals[j]+T <= depatures[i]){ ///New train will arrive first
			j++; Current++;
		}else {					//A train is going to depart
			i++;Current--;
			if (Current < 0) { Current = 0; MAXLevel++; }
				
		}
	}
	return MAXLevel;
}

int main(void){
	FILE* fin = fopen("train.in","rt");
	FILE* fout = fopen("train.out","wt");

	int N;
	fscanf(fin,"%d",&N);
	for(int i=0;i<N;i++){
		int T,cA,cB,t1,t2,t3,t4;
		int AD[200],AA[200],BD[200],BA[200];
		memset(AD,0,sizeof(AD));memset(AA,0,sizeof(AA));memset(BD,0,sizeof(BD));memset(BA,0,sizeof(BA));
		fscanf(fin, "%d\n", &T);
		fscanf(fin, "%d %d\n", &cA, &cB);
		for(int j=0;j<cA;j++) {
			fscanf(fin,"%d:%d %d:%d\n",&t1,&t2,&t3,&t4);
			AD[j] = t1*60+t2;AA[j] = t3*60+t4;
		}
		for(int j=0;j<cB;j++) {
			fscanf(fin,"%d:%d %d:%d\n",&t1,&t2,&t3,&t4);
			BD[j] = t1*60+t2;BA[j] = t3*60+t4;
		}

		fprintf(fout,"Case #%d: %d %d\n",i+1, 
											solve(AD,BA,cA,cB,T),
											solve(BD,AA,cB,cA,T));

	}

	fclose(fin);
	fclose(fout);
}