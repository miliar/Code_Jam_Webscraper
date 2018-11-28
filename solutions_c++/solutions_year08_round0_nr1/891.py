#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<vector>
using namespace std;
const int Max=100000000;
int Ans[100][1000];
int main()
{
	//string filein("test.txt");
	string filein("A-large.in");
	//string filein("A-small-attempt0.in");
	string fileout("Anslarge.txt");
	ifstream fin;
	fin.open(filein.c_str());
	ofstream fout;
	fout.open(fileout.c_str());
	string word;
	int Case;
	stringstream strint;
	getline(fin,word,'\n');
	strint<<word;
	strint>>Case;
	cout<<"Case: "<<Case<<endl;
	for(int i=1;i<=Case;i++)
	{
		//Case #1: 1
		fout<<"Case #"<<i<<": ";
		vector<string>Search;
		vector<string>Data;
		int S,Q;
		strint.clear();
		getline(fin,word,'\n');
		strint<<word;
		strint>>S;
		for(int j=0;j<S;j++)
		{
			getline(fin,word,'\n');
			//cout<<word<<endl;]
			Search.push_back(word);
		}
		getline(fin,word,'\n');
		strint.clear();
		strint<<word;
		strint>>Q;
		for(int j=0;j<Q;j++)
		{
			getline(fin,word,'\n');
			//cout<<word<<endl;
			Data.push_back(word);
		}
		for(int j=0;j<100;j++)
		{
			for(int k=0;k<1000;k++)
			{
				Ans[j][k]=Max;
			}
		}
		if(Q==0)
		{
			fout<<0<<endl;
			continue;
		}
		for(int j=0;j<S;j++)
		{
			if(Search[j]==Data[Q-1])
			{
				Ans[j][Q-1]=Max;
			}
			else
			{
				Ans[j][Q-1]=0;
			}
		}
		for(int j=Q-2;j>=0;j--)
		{
			for(int k=0;k<S;k++)
			{
				if(Search[k]==Data[j])
					Ans[k][j]=Max;
				else
				{
					Ans[k][j]=min(Max,Ans[k][j+1]);
					for(int m=0;m<S;m++)
					{
						if(m!=k&&Ans[m][j+1]+1<Ans[k][j])
						{
							Ans[k][j]=Ans[m][j+1]+1;
						}
					}
				}
			}
		}
		int finans=Max;
		for(int j=0;j<S;j++)
		{
			if(Ans[j][0]<finans)
				finans=Ans[j][0];
		}
		fout<<finans<<endl;

	}
	return 0;
}