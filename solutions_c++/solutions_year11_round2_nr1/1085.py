#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <climits>
#define REP(i,n) for(int (i)=0, _n=(n); (i) < (_n); i++)
#define REPD(i,n) for(int (i)=(n-1); i >= 0; i--)
#define FOR(i,a,n) for(int (i)=(a),_n=(n); (i) <= (_n); (i)++)
#define FORD(i,a,n) for(int (i)=(a),_n=(n); (i) >= (_n); (i)--)
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(cs,1,test){
		char grid[200][200];
		double wp[200],owp[200],oowp[200];
		int num[200]={};
		int n;
		scanf("%d",&n);
		REP(i,n)
			scanf("%s",grid[i]);
		
		REP(i,n){
			int win=0;
			REP(j,n){
				if(j==i)continue;
				if(grid[i][j] != '.')
					num[i]++;
				if(grid[i][j]=='1')
					win++;
			}
			wp[i] = 1.0*win/num[i];
			//cerr << "wp " << i << " = " << wp[i] << endl;
		}
		
		REP(i,n){
			double w=0;
			REP(j,n){
				if(j==i || grid[i][j]=='.')continue;
				double win = wp[j]*num[j];
				if(grid[j][i] == '1')win-=1;
				w += (win/(num[j]-1));
			}
			owp[i] = w/num[i];	
			//cerr  << "owp " << i << " = " << owp[i] << endl;
		}
		
		REP(i,n){
			double w=0;
			REP(j,n){
				if(j==i)continue;
				if(grid[i][j]!='.')
					w+=owp[j];	
			}
			oowp[i] = w/num[i];
			//cerr << "oowp " << i << " = " << oowp[i] << endl;
		}
		
		printf("Case #%d:\n",cs);
		REP(i,n)
			printf("%.10lf\n",.25 * wp[i] + .5 * owp[i] + .25*oowp[i]);
	}
	//system("pause");
    return 0;
}
