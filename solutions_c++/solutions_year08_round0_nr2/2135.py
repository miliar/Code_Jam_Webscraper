#include<stdio.h>
#include<vector.h>
#include<algorithm>
FILE *fin,*fout;
int u(char a[3])
{
	if(a[0]=='0')
		return(a[1]-'0');
	return ((a[1]-'0')+(10*(a[0]-'0')));
}
float rec(char a[3],char b[3])
{
	return(u(a)+(((float)u(b))/100));
}
int main()
{
	fin = fopen("B-small-attempt3.in","r");
	fout = fopen("B-small.out","w");
	int N,NA,NB,numA=0,numB=0,t;
 	float turn,tr,om;
	vector<float> tA;//holds the needed in A
	vector<float> tB;//holds the needed in B
	vector<float> eA;//holds the exists in A
	vector<float> eB;//holds the exists in B
	vector<float> stA;//holds the exists in B
	vector<float> stB;//holds the exists in B
	char a[3],b[3];
	a[2]='\0';
	b[2]='\0';
	bool found;
	fscanf(fin,"%d\n",&N);
	for(int z =0;z<N;z++)
	{
		fscanf(fin,"%f\n%d %d\n",&turn,&NA,&NB);
		for(int i=0;i<NA;i++)
		{
			fscanf(fin,"%c%c:%c%c ",&a[0],&a[1],&b[0],&b[1]);
			tA.push_back(rec(a,b));
			fscanf(fin,"%c%c:%c%c\n",&a[0],&a[1],&b[0],&b[1]);
			eB.push_back((rec(a,b)+(turn/100)));
			
		}
		for(int i=0;i<NB;i++)
		{
			fscanf(fin,"%c%c:%c%c ",&a[0],&a[1],&b[0],&b[1]);
			tB.push_back(rec(a,b));
			fscanf(fin,"%c%c:%c%c\n",&a[0],&a[1],&b[0],&b[1]);
			eA.push_back((rec(a,b)+(turn/100)));
		}
		std::sort(tA.begin(), tA.end());
		std::sort(tB.begin(), tB.end());
		for(int x =0;x<tA.size();x++)
		{
			found = false;
			tr=tA[x];
			for(int j=0;j<eA.size();j++)
			{
					if(eA[j]<=tr)
					{
						if(!found)
						{
							found=true;
							om=tA[j];
							t=j;
						}
						else 
						{
							if(tA[j]>om)
							{
								om=tA[j];
								t=j;
							}
						}
					}
			}
			if(!found)
				numA++;
			else
				eA.erase(eA.begin()+t);
			
		}
		for(int x =0;x<tB.size();x++)
		{
			found = false;
			tr = tB[x];
			for(int j=0;j<eB.size();j++)
			{
				if(eB[j]<=tr)
				{
					if(!found)
					{
						found=true;
						om=tB[j];
						t=j;
					}
					else 
					{
						if(tB[j]>om)
						{
							om=tB[j];
							t=j;
						}
					}
				}
			}
			if(!found)
				numB++;
			else
				eB.erase(eB.begin()+t);
		}
		fprintf(fout,"Case #%d: %d %d\n",(z+1),numA,numB);
		tA.clear();
		tB.clear();	
		eA.clear();
		eB.clear();
		numA=0;
		numB=0;	
	}
	return 0;
}
