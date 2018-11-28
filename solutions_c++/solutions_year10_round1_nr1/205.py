#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <strstream>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int i,j,k,l,m,n,ri,repeat,r,b;
char s[62][62],c;

int check(int x,int y,int dx,int dy,char c){
	int i,j,t=0;
	while(x>=0&&x<n&&y>=0&&y<n&&s[x][y]==c){
		t++;
		x+=dx;
		y+=dy;
	}
	if(t==k)return 1;
	else return 0;
}

int main()
{
        freopen("A-large.in","r",stdin);
        //freopen("x.txt","r",stdin);
        freopen("w.txt","w",stdout);
        scanf("%d",&repeat);
        for(ri=1;ri<=repeat;ri++){
			printf("Case #%d: ",ri);
			scanf("%d%d",&n,&k);
			getchar();
			for(i=0;i<n;i++){
				gets(s[i]);
			}
			for(i=0;i<n;i++){
				j=n-1;
				while(j>=0){
					while(s[i][j]!='.'&&(j>=0))j--;
					m=j;
					if(j<0)break;
					while(s[i][j]=='.'&&(j>=0))j--;
					if(j<0)break;
					l=j;
					c=s[i][m];
					s[i][m]=s[i][j];
					s[i][j]=c;
					j=m;
				}
			}
			r=b=0;
			for(i=0;i<n;i++)
				for(j=0;j<n;j++)
					if(s[i][j]=='R'&&(check(i,j,1,0,s[i][j])||check(i,j,0,1,s[i][j])||check(i,j,1,1,s[i][j])||check(i,j,-1,1,s[i][j])))
						r=1;
					else 
					if(s[i][j]=='B'&&(check(i,j,1,0,s[i][j])||check(i,j,0,1,s[i][j])||check(i,j,1,1,s[i][j])||check(i,j,-1,1,s[i][j])))
						b=1;

			if(r==1&&b==0)
				printf("Red\n");
			else if(r==0&&b==1)
				printf("Blue\n");
			else if(r==0&&b==0)
				printf("Neither\n");	
			else 
				printf("Both\n");	
				

		}
}

