#include<iostream>
#include<cmath>
#include<string>
#include<algorithm>
#include<fstream>
#include<vector>
#include<map>
using namespace std;

int main()
{
	ifstream cin("B-large.in");
	
	ofstream cout("B-small.out");
	int T;
	cin>>T;
	int x=1;
	while(T--)
	{
		int C;
		cin>>C;
		map<string,char> nonB;
		for(int i=0;i<C;i++)
		{
			string el;
			cin>>el;
			string sEl = el.substr(0,2);
			if(sEl[0]>sEl[1])
				swap(sEl[0],sEl[1]);
			nonB[sEl]=el[2];
		}
		int D;
		cin>>D;
		map<char,string> opp;
		for(int i=0;i<D;i++)
		{
			string op;
			cin>>op;
			if(opp[op[0]].empty())
			{
				opp[op[0]]="";
				
			}
			opp[op[0]].push_back(op[1]);
			if(opp[op[1]].empty())
			{
				opp[op[1]]="";
				
			}
			opp[op[1]].push_back(op[0]);
		}
		int N;
		cin>>N;
		string list="";
		for(int i=0;i<N;i++)
		{
			char e;
			cin>>e;
			if(list=="")
			{
				list.push_back(e);
				continue;
			}
			string com = "";
			com.push_back(e);
			com+=list[list.size()-1];
			if(com[0]>com[1])
				swap(com[0],com[1]);
			if(nonB[com]!=0)
			{
				list.pop_back();
				list.push_back(nonB[com]);
			}
			else
			{
				for(int j=0;j<list.size();j++)
				{
					if(opp[e].find(list[j])!=list.npos)
					{
						list.clear();
						break;
					}
				}
				if(!list.empty())
					list.push_back(e);
			}
		}
		cout<<"Case #"<<x++<<": [";
		for(int j=0;j<list.size();j++)
		{
			if(j!=list.size()-1)
				cout<<list[j]<<", ";
			else
				cout<<list[j];
		}
		cout<<"]"<<endl;
	}
	return 0;

}
/*
Problem 1: Bot Trust
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
*/