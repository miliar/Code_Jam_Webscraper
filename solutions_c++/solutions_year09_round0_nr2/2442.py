// CJ09Watersheds.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{

	int cases;
	cin>>cases;
	for(int caseNumber=0;caseNumber<cases;++caseNumber)
	{
		vector<vector<int>> map;
		vector<vector<pair<int,int>>> towards;
		vector<vector<char>> basins;
		int H,W;
		cin>>H>>W;
		for(int i=0;i<H;++i){
			map.push_back(vector<int>());
			towards.push_back(vector<pair<int,int>>());
			basins.push_back(vector<char>());
			for(int j=0;j<W;++j)
			{
				int input;
				cin>>input;
				map[i].push_back(input);
				towards[i].push_back(make_pair(-1,-1));
				basins[i].push_back(' ');
			}
		}

		for(int i=0;i<H;++i)
			for(int j=0;j<W;++j)
			{
				int smallest=map[i][j];
				pair<int,int> to=make_pair(i,j);
				if(i+1<H)
				{
					if(smallest>=map[i+1][j])
					{
						smallest=map[i+1][j];
						to=make_pair(i+1,j);
					}
				}

				if(j+1<W)
				{
					if(smallest>=map[i][j+1])
					{
						smallest=map[i][j+1];
						to=make_pair(i,j+1);
					}
				}

				if(j-1>=0)
				{
					if(smallest>=map[i][j-1])
					{
						smallest=map[i][j-1];
						to=make_pair(i,j-1);
					}
				}

				if(i-1>=0)
				{
					if(smallest>=map[i-1][j])
					{
						smallest=map[i-1][j];
						to=make_pair(i-1,j);
					}
				}

				if(smallest==map[i][j])
				{
					to=make_pair(i,j);
				}

				towards[i][j]=to;
				
			}

		bool changed=false;
		do{
			changed=false;
			for(int i=0;i<H;++i)
				for(int j=0;j<W;++j)
				{
					pair<int,int> to=towards[i][j];
					pair<int,int> toto=towards[to.first][to.second];
					if(toto.first!=to.first || toto.second!=to.second){
						towards[i][j]=toto;
						changed=true;
					}
				}
		}while(changed);

		char cur='a';

		cout<<"Case #"<<(caseNumber+1)<<":"<<endl;

		for(int i=0;i<H;++i){
			for(int j=0;j<W;++j)
			{
				if(basins[i][j]==' '){
					pair<int,int> to=towards[i][j];
					if(basins[to.first][to.second]==' '){
						basins[to.first][to.second]=cur++;
					}
					basins[i][j]=basins[to.first][to.second];
				}
				cout<<basins[i][j];
				if(j!=W-1)cout<<' ';
				else cout<<endl;
			}
		}



	}
	return 0;
}

