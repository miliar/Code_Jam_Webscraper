#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#define P_NEVER				0
#define P_WHEN_SURPRISING	1
#define P_ALWAYS			2

unsigned difference(int a, int b)
{
	int ret=a-b;
	if(ret<0)
		ret*=-1;
	return ret;
}

int isP(int score, int p)
{
	int triplet[3];
	triplet[0]=score/3;
	triplet[1]=(score-triplet[0])/2;
	triplet[2]=score-triplet[0]-triplet[1];

	int imax=0;
	for(int i=0;i<3;i++)
	{
		if(triplet[i]>triplet[imax])
			imax=i;
	}

	if(triplet[0]+triplet[1]+triplet[2]!=score)
		triplet[imax]++;

	int imin=0;
	for(int i=1;i<3;i++)
	{
		if(triplet[i]<triplet[imin])
			imin=i;
	}

	if(difference(triplet[imax],triplet[imin])>1)
	{
		int iother=0;
		triplet[imin]++;
		if(imax==0||imin==0)
		{
			if(imax==1||imin==1)
				iother=2;
			else
				iother=1;
		}
		if(imax==1||imin==1)
		{
			if(imax==2||imin==2)
				iother=0;
		}
		if(triplet[iother]>triplet[imin])
			triplet[iother]--;
		else
			triplet[imax]--;
	}
	
	if(triplet[imax]>=p)
		return P_ALWAYS;


	if(triplet[imax]+1>=p&&triplet[imax])
		return P_WHEN_SURPRISING;

	return P_NEVER;
}

int main()
{
	int T;
	char buf[256];
	int len;
	FILE *fin,*fout;
	fopen_s(&fin,"C:/input.in","r");
	fopen_s(&fout,"C:/output.txt","r+");

	fscanf(fin,"%d ",&T);

	for(int nCase=1;nCase<=T;nCase++)
	{
		int N,S,p,ti[100];
		int total=0;
		fscanf(fin,"%d %d %d ",&N,&S,&p);

		for(int i=0;i<N;i++)
		{
			fscanf(fin,"%d ",&ti[i]);
		}

		for(int i=0;i<N;i++)
		{
			int result=isP(ti[i],p);
			switch(result)
			{
			case P_NEVER:
				continue;
			case P_WHEN_SURPRISING:
				if(!S)
					continue;
				S--;
			case P_ALWAYS:
				total++;
			}
		}

		if(nCase==1)
			fprintf_s(fout,"Case #%d: %d",nCase,total);
		else
			fprintf_s(fout,"\nCase #%d: %d",nCase,total);
	}
	fclose(fin);
	fclose(fout);
}