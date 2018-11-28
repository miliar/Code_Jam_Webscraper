#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char m[101][101];
double wp[101];
double owp[101];
double oowp[101];
int total[101];
int win[101];
double rpi[101];

void initial();

int main()
{
	int caseNum=1;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int cnt;
	fin >> cnt;//////////
	while(cnt-- > 0)
	{
		int N;
		fin >> N;
		initial();
		for(int i=0;i<N;i++)
		{
			total[i]=0;
			win[i]=0;
			for(int j=0;j<N;j++)
			{
				fin >> m[i][j];
				char c=m[i][j];
				if(c!='.')
					total[i]++;
				if(c=='1')
					win[i]++;
			}
			wp[i]=double((double)win[i]/(double)total[i]);
		}
		for(int i=0;i<N;i++)
		{
			double owpf=0;
			double temp;
			for(int j=0;j<N;j++)
			{
				if(m[i][j]=='1')
					temp=(double)win[j]/(double)(total[j]-1);
				else if(m[i][j]=='0')
					temp=(double)(win[j]-1)/(double)(total[j]-1);
				if(m[i][j]!='.')
					owpf+=temp;
			}
			owp[i]=double(owpf/(double)total[i]);
		}
		for(int i=0;i<N;i++)
		{
			double oowpf=0;
			for(int j=0;j<N;j++)
			{
				if(m[i][j]!='.')
				{
					oowpf+=owp[j];
				}
			}
			oowp[i]=double(oowpf/(double)total[i]);
		}
		fout << "Case #" << caseNum++ << ":" << endl;
		for(int i=0;i<N;i++)
		{
			rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			fout << rpi[i] << endl;
		}

	}
} 

void initial()
{
	for(int i=0;i<101;i++)
	{
		wp[i]=0;
		owp[i]=0;
		oowp[i]=0;
		rpi[i]=0;
	}
}