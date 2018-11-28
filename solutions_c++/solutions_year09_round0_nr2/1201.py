#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-large";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

int mas[111][111];
int c=0;
int col[111][111];

int go(int x, int y)
{
	if (col[x][y]) return col[x][y];
	vector <pair <int, int> > ad;
	ad.push_back(make_pair(mas[x-1][y],1));
	ad.push_back(make_pair(mas[x][y-1],2));
	ad.push_back(make_pair(mas[x][y+1],3));
	ad.push_back(make_pair(mas[x+1][y],4));
	sort(all(ad));
	if (ad[0].first<mas[x][y])
	{
		int res;
		if (ad[0].second==1)	res=go(x-1,y);
		if (ad[0].second==2)	res=go(x,y-1);
		if (ad[0].second==3)	res=go(x,y+1);
		if (ad[0].second==4)	res=go(x+1,y);
		col[x][y]=res;
		return res;
	} else
	{
		c++;
		col[x][y]=c;
		return c;
	}
}


int main()
{
   init();


	int t;
	scanf("%d\n",&t);
	for (int cas=1;cas<=t;cas++)
	{
		memset(mas,1,sizeof(mas));
		memset(col,0,sizeof(col));
		c=0;
		int h,w;
		scanf("%d%d\n",&h,&w);
		for (int i=1;i<=h;i++)
		for (int j=1;j<=w;j++)
			scanf("%d",&mas[i][j]);

		for (int i=1;i<=h;i++)
		for (int j=1;j<=w;j++) if (!col[i][j])
			go(i,j);
		printf("Case #%d:\n",cas);
		
		for (int i=1;i<=h;i++)
		{
			for (int j=1;j<=w;j++)
			{
				if (j!=1) printf(" ");
				printf("%c",'a'+col[i][j]-1);
			}
			printf("\n");
		}	
	}
	




   return 0; 
}
