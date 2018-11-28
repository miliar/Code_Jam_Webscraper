#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int nroft,nrTeam,WIN[105],NR[105],mat[103][103];
	double ma,nrma;
	double WP[105],OWP[105],OOWP[105];
	char x;
	ifstream fin("RPI.in");
	ofstream fout("RPI.out");	
	fin>>nroft;
	for(int kk=1;kk<=nroft;kk++)
	{
		fin>>nrTeam;
		memset(WIN ,0, sizeof(int[105]));
		memset(NR ,0, sizeof(int[105]));
		memset(WP ,0, sizeof(double[105]));
		memset(OWP ,0, sizeof(double[105]));
		memset(OOWP ,0, sizeof(double[105]));
		memset(mat ,-1, sizeof(int[103][103]));
		for(int orf=1;orf<=nrTeam;orf++)
			for(int rr=1;rr<=nrTeam;rr++)
			{
				fin>>x;
				switch (x)
				{
					case '1':
						WIN[orf]=WIN[orf]+1;
						NR[orf]++;
						mat[orf][rr]=1;
						break;
					case '0':
						NR[orf]++;
						mat[orf][rr]=0;
						break;
				}
					WP[orf] = double(WIN[orf])/NR[orf];
			}
			for(int i=1;i<=nrTeam;i++){
				ma=0;
				nrma=0;
				for(int j=1;j<=nrTeam;j++)
				{	if(mat[j][i]==0)
					{
						ma=ma+double(WIN[j])/(NR[j]-1);
						nrma++;
					}
					if(mat[j][i]==1)
					{
						ma=ma+double(WIN[j]-1)/(NR[j]-1);
						nrma++;
					}
				}
				OWP[i]=ma/nrma;
			}
				for(int i=1;i<=nrTeam;i++)
				{
				ma=0;
				nrma=0;
				for(int j=1;j<=nrTeam;j++)
				{
					if(mat[i][j]==0 || mat[i][j]==1)
					{
						ma=ma+OWP[j];
						nrma++;
					}
				}
				OOWP[i]=ma/nrma;
				}
					
		fout<<"Case #"<<kk<<":"<<endl;
		for(int pp=1;pp<=nrTeam;pp++)
			fout<<0.25*WP[pp]+0.5*OWP[pp]+0.25*OOWP[pp]<<endl;		
	}
	fout.close();
	fin.close();
	return 0;
}
