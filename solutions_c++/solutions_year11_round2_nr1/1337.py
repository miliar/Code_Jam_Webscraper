#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T;
	int N;
	char* Schedule=0;
	double* WP=0;
	double* OWP=0;
	double* OOWP=0;
	int* All=0;
	int* Win=0;
	int* Oppo=0;
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("Alarge-answer.txt");
	fin>>T;
	for (int i=1;i<=T;i++)
	{
		fin>>N;
		Schedule=new char [N*N];
		WP=new double[N];
		All=new int[N];
		Win=new int[N];
		Oppo=new int[N];
		OWP=new double[N];
		OOWP=new double[N];
		for (int j=0;j<=N-1;j++)
		{			
			for (int k=0;k<=N-1;k++)
			{
				fin>>Schedule[j*N+k];
			}
		}

		for (int j=0;j<=N-1;j++)
		{
			WP[j]=0;
			OWP[j]=0;
			OOWP[j]=0;
			Oppo[j]=0;
		}

		for (int j=0;j<=N-1;j++)
		{
			All[j]=0;
			Win[j]=0;
			for (int k=0;k<=N-1;k++)
			{
				if (Schedule[j*N+k]=='1')
				{
					All[j]++;
					Win[j]++;
				}

				if (Schedule[j*N+k]=='0')
				{
					All[j]++;
				}
			}
			WP[j]=(double)Win[j]/All[j];
		}

		for (int j=0;j<=N-1;j++)
		{
			for (int k=0;k<=N-1;k++)
			{
				if (Schedule[k*N+j]=='1')
				{
					OWP[j]=OWP[j]+(double)(Win[k]-1)/(All[k]-1);
					Oppo[j]++;
				}
				if (Schedule[k*N+j]=='0')
				{
					OWP[j]=OWP[j]+(double)Win[k]/(All[k]-1);
					Oppo[j]++;
				}
			}
			OWP[j]=OWP[j]/Oppo[j];
		}

		for (int j=0;j<=N-1;j++)
		{
			for (int k=0;k<=N-1;k++)
			{
				if (Schedule[k*N+j]=='1')
				{
					OOWP[j]=OOWP[j]+OWP[k];
				}
				if (Schedule[k*N+j]=='0')
				{
					OOWP[j]=OOWP[j]+OWP[k];
				}
			}
			OOWP[j]=OOWP[j]/Oppo[j];
		}
		fout<<"Case #"<<i<<": "<<endl;
		for (int j=0;j<=N-1;j++)
		{
			fout<<0.25*WP[j]+0.5*OWP[j]+0.25*OOWP[j]<<endl;
		}
	}
	return 0;
}