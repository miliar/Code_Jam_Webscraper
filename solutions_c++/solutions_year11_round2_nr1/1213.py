#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

void cal(char * * r,int n,double * result);

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("..//A-large.in");
	fout.open("..//t2.txt");


	int testNum;
	fin>>testNum;
	for(int i=1;i<=testNum;i++)
	{
		int n;fin>>n;
		char * * r=new char *[n];
		for(int j=0;j<n;j++)
		{
			r[j]=new char[n];
		}
		for(int m=0;m<n;m++)
		{
			for(int k=0;k<n;k++)
				fin>>r[m][k];
		}
		
		cout<<"Case #"<<i<<":"<<endl;
		fout<<"Case #"<<i<<":"<<endl;
		double * result=new double[n];
		cal(r,n,result);
		for(int k=0;k<n;k++)
		{
			cout<<setprecision(10)<<result[k]<<endl;
			fout<<setprecision(10)<<result[k]<<endl;
		}

	}

	return 0;
}

void cal(char * * r,int n,double * result)
{
	double * wp=new double[n];
	double * owp=new double[n];
	double * oowp=new double[n];
	for(int i=0;i<n;i++)
	{
		int totalMatch=0;
		int winMatch=0;
		for(int j=0;j<n;j++)
		{
			if(r[i][j]=='1')
			{
				totalMatch++;
				winMatch++;
			}
			else if(r[i][j]=='0')
			{
				totalMatch++;
			}
		}

		wp[i]=(double)winMatch/(double)totalMatch;
	}

	for(int i=0;i<n;i++)
	{
		int fenMu=0;
		double fenZi=0;
		for(int j=0;j<n;j++)
		{
			if(r[i][j]=='.')
				continue;
			fenMu++;
			int winMatch=0,totalMatch=0;
			for(int k=0;k<n;k++)
			{
				if(k==i || r[j][k]=='.')
					continue;
				if(r[j][k]=='1')
				{
					totalMatch++;winMatch++;
				}
				else
				{
					if(r[j][k]=='0') totalMatch++;
				}
			}
			fenZi+=(double)winMatch/(double)totalMatch;
		}
		owp[i]=fenZi/(double)fenMu;
	}
	

	for(int i=0;i<n;i++)
	{
		int fenMu=0;
		double fenZi=0;
		for(int j=0;j<n;j++)
		{
			if(r[i][j]=='.')
				continue;
			fenMu++;
			fenZi+=owp[j];
		}
		oowp[i]=fenZi/(double)fenMu;
	}
	for(int i=0;i<n;i++)
	{
		//cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
		//fout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
		result[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
	}
}