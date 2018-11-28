#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) ((a)*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
};
typedef vector<node> vn ; 
int cases,g;
const int lim=256;
//bool visit[lim];
char comb[256][256];
string opp[256];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
////////////////////////////////////////////
	int i,j,k;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
//	CLS(visit,0);
		CLS(comb,0);
		for(i=0;i<lim;i++)
			opp[i]="";
		printf("Case #%d: ",g+1);
		int c;
		scanf("%d",&c);
		for(i=0;i<c;i++)
		{
			char cstr[10];
			scanf("%s",cstr);
			comb[cstr[0]][cstr[1]]=cstr[2];
			comb[cstr[1]][cstr[0]]=cstr[2];
		}
		int d;
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			char cstr[10];
			scanf("%s",cstr);
			opp[cstr[0]]+=cstr[1];
			opp[cstr[1]]+=cstr[0];
		}
		int n;
		scanf("%d",&n);
		string str;
		string cur="";
		cin >> str;
		for(i=0;i<str.size();i++) {
			bool cleared = 0;
			char x = str[i];
			char l;
			if(cur.size())
				l = cur[cur.size()-1];
			if(cur.size() && comb[l][x]) {
				cur.erase(cur.end()-1);
				cur+=comb[l][x];
			} else {
				for(j=0;j<opp[x].size();j++) {
					if(cur.find(opp[x][j],0)!=-1)
					{
						cur.clear();
						cleared =1;
						break;
					}
				}
				if(!cleared)
					cur+=x;
			}
		}
		//cout << cur <<endl;
		printf("[");
		for(i=0;i<cur.size();i++) {
			if(i!=0)
				printf(", ");
			printf("%c",cur[i]);
		}
		printf("]\n");
	}

	return 0;
}