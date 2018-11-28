#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back


int main(){
	int tc, n, r, c;
	char s[60][60];
	scanf("%d",&tc);
	REP(t,tc){
		scanf("%d%d",&r,&c);
		REP(i,r)scanf("%s",s[i]);
		for(int i=0;i<r-1;i++){
			for(int j=0;j<c-1;j++){
				if(s[i][j]=='#'){
					if(s[i+1][j]=='#'&&s[i+1][j+1]=='#'&&s[i][j+1]=='#'){
						s[i][j]='/';
						s[i+1][j]='\\';
						s[i][j+1]='\\';
						s[i+1][j+1]='/';
					}
				}
			}
		}
		bool f=true;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(s[i][j]=='#'){
					f=false;
					break;
				}
			}
		}		
		printf("Case #%d:\n",t+1);
		if(!f)puts("Impossible");
		else{
			REP(i,r)printf("%s\n",s[i]);
		}
	}
	return 0;
}
