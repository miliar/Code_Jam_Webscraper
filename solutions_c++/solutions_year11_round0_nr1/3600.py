#include<iostream>
#include<cmath>
#include<string>
#include<algorithm>
#include<fstream>
#include<vector>
using namespace std;

int main()
{ifstream cin("A-large.in");
	int T;
	cin>>T;
	int x=1;
	
	ofstream cout("A-small.out");
	while(T--)
	{
		int N,t=0;
		cin>>N;
		
		vector<pair<char,int> > seq;
		for(int i=0;i<N;i++)
		{
			pair<char,int> p;
			cin>>p.first;
			cin>>p.second;
			seq.push_back(p);
		}
		int blueP = 1;
		int orangeP = 1;
		for(int i=0;i<N;i++)
		{
			if(seq[i].first=='O')
			{

				int firstB = 0;
				for(int j=i+1;j<N;j++)
				{
					if(seq[j].first=='B')
					{
						firstB=j;
						break;
					}
				}

				while(orangeP<seq[i].second)
				{
					orangeP++;
					t++;
					if(seq[firstB].second>blueP)
						blueP++;
					else if(seq[firstB].second<blueP)
						blueP--;

				}
				while(orangeP>seq[i].second)
				{
					orangeP--;
					t++;
					if(seq[firstB].second>blueP)
						blueP++;
					else if(seq[firstB].second<blueP)
						blueP--;

				}
				t++;
				if(seq[firstB].second>blueP)
					blueP++;
				else if(seq[firstB].second<blueP)
					blueP--;
			}
			else
			{

				int firstB = 0;
				for(int j=i+1;j<N;j++)
				{
					if(seq[j].first=='O')
					{
						firstB=j;
						break;
					}
				}
				while(blueP<seq[i].second)
				{
					blueP++;
					t++;
					if(seq[firstB].second>orangeP)
						orangeP++;
					else if(seq[firstB].second<orangeP)
						orangeP--;

				}
				while(blueP>seq[i].second)
				{
					blueP--;
					t++;
					if(seq[firstB].second>orangeP)
						orangeP++;
					else if(seq[firstB].second<orangeP)
						orangeP--;

				}
				t++;
				if(seq[firstB].second>orangeP)
					orangeP++;
				else if(seq[firstB].second<orangeP)
					orangeP--;
			}

		}
		cout<<"Case #"<<x++<<": "<<t<<endl;

	}
	return 0;
}