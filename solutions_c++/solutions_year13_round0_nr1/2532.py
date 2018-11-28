/*
ID: amin_un1
PROG: ride
LANG: C++
*/

/*
my ID
uva = "sir sbu"
codforsec = "sirsbu"
topcoder = "sir_sbu"
usaco = "amin_un1"
*/
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <queue>
#include <cmath>
#include <sstream>
#include <fstream>
#include <string.h>
#include <string>
#include <map>
#include <stack>
#include <set>
#define LL long long
#define Endl endl
#define all(n) (n).begin(), (n).end()
using namespace std;
const LL mod=1000*1000*1000+7LL;
const double EXP = 1e-6;
const int MAX = 100001;
bool mark[4][4];
int main()
{
	//ofstream cout ("test.out");
    //ifstream cin ("test.in");
    //freopen("output.txt", "w", stdout);
    //freopen("input.txt", "a", stdout);
    int tc;
    cin>>tc;
    int t=0;
    while(tc--)
    {
		t++;
    	string str[4];
    	for(int i=0;i<4;i++)
    	{
			cin>>str[i];
		}
		int k=0;// 1 x 2 o 
		for(int i=0;i<4;i++)//X
		{
			int t=0;
			int o=0;
			for(int j=0;j<4;j++)
			{
				if(str[i][j]=='X' || str[i][j]=='T')t++;
				if(str[i][j]=='O' || str[i][j]=='T')o++;
				
			}
			if(t==4)k=1;
			if(o==4)k=2;
		}
		for(int i=0;i<4;i++)
		{
			int t=0;
			int o=0;
			for(int j=0;j<4;j++)
			{
				if(str[j][i]=='X' || str[j][i]=='X')t++;
				if(str[j][i]=='O' || str[j][i]=='T')o++;
			}
			if(t==4)k=1;
			if(o==4)k=2;
		}
		if((str[0][0]=='X' || str[0][0]=='T')&&(str[1][1]=='X' || str[1][1]=='T')&&(str[2][2]=='X' || str[2][2]=='T')&&(str[3][3]=='X' || str[3][3]=='T')) k=1;
		if((str[3][0]=='X' || str[3][0]=='T')&&(str[2][1]=='X' || str[2][1]=='T')&&(str[1][2]=='X' || str[1][2]=='T')&&(str[0][3]=='X' || str[0][3]=='T')) k=1;
		
		if((str[0][0]=='O' || str[0][0]=='T')&&(str[1][1]=='O' || str[1][1]=='T')&&(str[2][2]=='O' || str[2][2]=='T')&&(str[3][3]=='O' || str[3][3]=='T')) k=2;
		if((str[3][0]=='O' || str[3][0]=='T')&&(str[2][1]=='O' || str[2][1]=='T')&&(str[1][2]=='O' || str[1][2]=='T')&&(str[0][3]=='O' || str[0][3]=='T')) k=2;
		
		if(k==0)
		{
			for(int i=0;i<4;i++)
			{
				int p=0;
				for(int j=0;j<4;j++)
				{
					if(str[i][j]!='.')
					p++;
				}
				if(p!=4)
				k=3;
			}
		}
		if(k==1)
		cout<<"Case #"<<t<<": X won"<<endl;
		else if(k==2)
		cout<<"Case #"<<t<<": O won"<<endl;
		else if(k==3)
		cout<<"Case #"<<t<<": Game has not completed"<<endl;
		else
		cout<<"Case #"<<t<<": Draw"<<endl;
	}
	return 0;
}


