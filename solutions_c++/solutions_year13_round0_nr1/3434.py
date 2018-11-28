#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <string>
#include <vector>
#include <fstream>
#include <map>
using namespace std;
const int INF = -1u>>1;
const double eps = 1e-8;
string str[5];

int main()
{
	int T;
	//ifstream in;
	//in.open("D:\\A-large.in");
	//ofstream out;
	//out.open("D:\\b.out");
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		for(int i=0;i<4;++i) cin>>str[i];
		int na,nb;
		bool flag = false;
		printf("Case #%d:",cas);
		//out<<"Case #"<<cas<<": ";
		for(int i=0;i<4;++i)
		{
			na = 0;nb = 0;
			for(int j=0;j<4;++j)
			{
				if(str[i][j] == 'T')
				{
					na++;
					nb++;
				}
				if(str[i][j] == 'X') na++;
				if(str[i][j] == 'O') nb++;
			}
			if(na == 4) 
			{
				printf("X won\n");
				//out<<"X won"<<endl;
				flag = true;
			}
			else if(nb == 4)
			{
				printf("O won\n");
				//out<<"O won"<<endl;
				flag = true;
			}
		}
		if(flag) continue;
		for(int i=0;i<4;++i)
		{
			na = 0;nb = 0;
			for(int j=0;j<4;++j)
			{
				if(str[j][i] == 'T')
				{
					na++;
					nb++;
				}
				if(str[j][i] == 'X') na++;
				if(str[j][i] == 'O') nb++;
			}
			if(na == 4)
			{
				printf("X won\n");
				//out<<"X won"<<endl;
				flag = true;
			}
			else if(nb == 4)
			{
				printf("O won\n");
				//out<<"O won"<<endl;
				flag = true;
			}
		}
		if(flag) continue;
		na = 0;nb = 0;
		for(int i=0;i<4;++i)
		{
			if(str[i][i] == 'T')
			{
				na++;
				nb++;
			}
			if(str[i][i] == 'X') na++;
			if(str[i][i] == 'O') nb++;
		}
		if(na == 4) 
		{
			printf("X won\n");
			//out<<"X won"<<endl;
			flag = true;
		}
		else if(nb == 4)
		{
			printf("O won\n");
			//out<<"O won"<<endl;
			flag = true;
		}	
		if(flag) continue;
		na = 0;nb = 0;
		for(int i=0;i<4;++i)
		{
			if(str[i][4-i-1] == 'T')
			{
				na++;
				nb++;
			}
			if(str[i][4-i-1] == 'X') na++;
			if(str[i][4-i-1] == 'O') nb++;
		}
		if(na == 4) 
		{
		  printf("X won\n");
			//out<<"X won"<<endl;
			flag = true;
		}
		else if(nb == 4)
		{
			printf("O won\n");
			//out<<"O won"<<endl;
			flag = true;
		}	
		if(flag) continue;
		int ncount = 0;
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;j++)
			{
				if(str[i][j] == '.') ncount++;
			}
		}
		//if(ncount == 0) out<<"Draw"<<endl;
		//else out<<"Game has not completed"<<endl;
		if(ncount == 0)  printf("Draw\n");
		else printf("Game has not completed\n");
	}
  return 0;
}

