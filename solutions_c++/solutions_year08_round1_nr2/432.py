#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<vector>
#include<cmath>
#include<iomanip>
using namespace std;
int x[3],y[3];
int a[3];
int fla[2000];
	int cus[2000][2000];
int main(){
	//string filein("test.txt");
	//string filein("A-small(2).in");
	string filein;
	//filein="A-small.in";
	//filein="A-large.in";
	filein="B-small-attempt0.in";
	string fileout;
	//fileout="Anslarge.txt";
	fileout="Anstest.txt";
	//fileout="Anssmall.txt";
	ifstream fin;
	fin.open(filein.c_str());
	ofstream fout;
	fout.open(fileout.c_str());
	string word;



	int two[12];
	two[0]=1;
	
	for(int i=1;i<12;i++)
		two[i]=2*two[i-1];
	int Case;
	fin>>Case;
	int N,M;
	for(int i=1;i<=Case;i++)
	{
		memset(fla,0,sizeof(fla));
		memset(cus,-1,sizeof(cus));
		fout<<"Case #"<<i<<": ";
		fin>>N>>M;
		int T;
		for(int j=0;j<M;j++)
		{
			fin>>T;
			for(int k=0;k<T;k++)
			{
				int a,b;
				fin>>a>>b;
				cus[j][a-1]=b;
			}
		}
		//
		int Ans=10000;
		int reco[2000];
		for(int j=0;j<two[N];j++)
		{
			for(int k=0;k<N;k++)
			{
				fla[k]=(j&two[k])>>k;
			}
			int tmp=0;
			for(int k=0;k<N;k++)
			{
				if(fla[k]==1)
					tmp++;
			}
			
			bool succ=true;
			for(int k=0;k<M;k++)
			{
				bool satis=false;
				for(int l=0;l<N;l++)
				{
					if(cus[k][l]==fla[l])
					{
						satis=true;
						break;
					}
				}
				if(!satis)
				{
					succ=false;
					break;
				}
			}
			if(succ)
			{
				if(tmp<Ans)
				{
					Ans=tmp;
					for(int p=0;p<N;p++)
					{
						reco[p]=fla[p];
					}
				}
			}
		}
		if(Ans==10000)
		{
			fout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			for(int q=0;q<N;q++)
			{
				fout<<reco[q]<<' ';
			}
			fout<<endl;
		}

	}
	return 0;
}