//operator system:windows xp
//environment:vc++6.0
#include<stdio.h>
void sort1(int a[100],int n)
{
	int k,i,j;
	int t;
	for(i=0;i<n-1;i++)
	{
		k=i;
		for(j=i+1;j<n;j++)
			if(a[j]<a[k])k=j;
			t=a[i];a[i]=a[k];a[k]=t;
	}
}
int main()
{
	int N;
	int i,j,k;
	int T;
	int NA,NB;
	int Astart[100][2],Aend[100][2],Bstart[100][2],Bend[100][2];
	int Akeep,Bkeep;
	int Aneed,Bneed;
	int Alast,Blast;
	int Astart1[100],Aend1[100],Bstart1[100],Bend1[100];
	FILE *fp;
	fp=fopen("c:\\out.txt","w");
	scanf("%d",&N);
	for(i=0;i<N;i++)
	{
        scanf("%d",&T);
		scanf("%d%d",&NA,&NB);
		for( j=0;j<NA;j++)
		{
			scanf("%d:%d%d:%d",&Astart[j][0],&Astart[j][1],&Aend[j][0],&Aend[j][1]);
		//	printf("%d:%d %d:%d",Astart[j][0],Astart[j][1],Aend[j][0],Aend[j][1]);
			Astart1[j]=Astart[j][0]*60+Astart[j][1];
			Aend1[j]=Aend[j][0]*60+Aend[j][1]+T;

		}
		sort1(Astart1,NA);
		sort1(Aend1,NA);
		for( j=0;j<NB;j++)
		{
			scanf("%d:%d%d:%d",&Bstart[j][0],&Bstart[j][1],&Bend[j][0],&Bend[j][1]);
			Bstart1[j]=Bstart[j][0]*60+Bstart[j][1];
			Bend1[j]=Bend[j][0]*60+Bend[j][1]+T;

		}
		sort1(Bstart1,NB);
		sort1(Bend1,NB);
        Akeep=0;
		Aneed=0;
		Alast=0;
		for(j=0;j<NA;j++)
		{
			for(k=0;k<NB;k++)
				if(Bend1[k]>Alast&&Bend1[k]<=Astart1[j])Akeep++;
				if(Akeep>0)Akeep-=1;
				else Aneed++;
				Alast=Astart1[j];
		}
		Bkeep=0;
		Bneed=0;
		Blast=0;
		for(j=0;j<NB;j++)
		{
			for(k=0;k<NA;k++)
				if(Aend1[k]>Blast&&Aend1[k]<=Bstart1[j])Bkeep++;
				if(Bkeep>0)Bkeep-=1;
				else Bneed++;
				Blast=Bstart1[j];
		}

        fprintf(fp,"Case #%d: %d %d\n",i+1,Aneed,Bneed);
	}
	fclose(fp);
	return 0;
}