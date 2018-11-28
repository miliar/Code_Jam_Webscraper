#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int th=0;
	int tm=0;
	int totalcases;
	int na,nb;
	char ign;

	int atrains=0;
	int btrains=0;

	int turnaround;
	int a_ava=0;
	int b_ava=0;
	int *a_arrh;
	int *a_arrm;
	int *a_deph;
	int *a_depm;
	int *b_arrh;
	int *b_arrm;
	int *b_deph;
	int *b_depm;

	ifstream file;
	ofstream file1;

	file.open("B-large.in");
	file1.open("output.txt");

	file>>totalcases;

	for(int i=0;i<totalcases;i++)
	{
		file>>turnaround;
		file>>na;
		file>>nb;
		
		a_arrh=new int[na];
		a_arrm=new int[na];
		a_deph=new int[na];
		a_depm=new int[na];
		b_arrh=new int[nb];
		b_arrm=new int[nb];
		b_deph=new int[nb];
		b_depm=new int[nb];

		for(int j=0;j<na;j++)
		{
			file>>a_deph[j];
			file>>ign;
			file>>a_depm[j];
			file>>a_arrh[j];
			file>>ign;
			file>>a_arrm[j];
			
			for(int l=0;l<turnaround;l++)
			{
				a_arrm[j]++;
				if(a_arrm[j]==60)
				{
					a_arrm[j]=0;
					a_arrh[j]++;
				}
			}
		}

		for(j=0;j<nb;j++)
		{
			file>>b_deph[j];
			file>>ign;
			file>>b_depm[j];
			file>>b_arrh[j];
			file>>ign;
			file>>b_arrm[j];

			for(int l=0;l<turnaround;l++)
			{
				b_arrm[j]++;
				if(b_arrm[j]==60)
				{
					b_arrm[j]=0;
					b_arrh[j]++;
				}
			}
		}


		while(th<=23 && tm<=59)
		{
			for(int k=0;k<na;k++)
			{
				if(a_arrh[k]==th && a_arrm[k]==tm)
				{
					b_ava++;
				}
			}

			for(k=0;k<nb;k++)
			{
				if(b_arrh[k]==th && b_arrm[k]==tm)
				{
					a_ava++;
				}
			}
			
			for(k=0;k<na;k++)
			{
				if(a_deph[k]==th && a_depm[k]==tm && a_ava==0)
				{
					atrains++;
				}
				else
				if(a_deph[k]==th && a_depm[k]==tm && a_ava>=1)
				{
					a_ava--;
				}
			}

			for(k=0;k<nb;k++)
			{
				if(b_deph[k]==th && b_depm[k]==tm && b_ava==0)
				{
					btrains++;
				}
				else
				if(b_deph[k]==th && b_depm[k]==tm && b_ava>=1)
				{
					b_ava--;
				}
			}

			if(tm==59)
			{
				th++;
				tm=0;
			}
			else
			{
				tm++;
			}
		
		}

		th=tm=0;
		file1<<"Case #"<<i+1<<": "<<atrains<<" "<<btrains<<endl;
		atrains=0;
		btrains=0;
		a_ava=0;
		b_ava=0;
	}

	return 0;
}