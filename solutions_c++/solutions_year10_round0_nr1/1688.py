#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cassert>
#include <cstring>
#include <queue>
#define vvi vector<vector<int> > 
#define pii pair<int,int>
#define vpii vector<vector<pair<int,int> > > 
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;
int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--!=0){
		int n,k;
		scanf("%d%d",&n,&k);
		int st=1<<n;
		k%=st;
		bool ok=true;
		if(k!=st-1)ok=false;
		/*
		for(int i=0;i<n;i++,st<<=1){
			if((k&st)==0){ok=false;break;}
		}
		*/
		if(!ok)printf("Case #%d: OFF\n",caseno);
		else printf("Case #%d: ON\n",caseno);
		caseno++;
	}
	return 0;
}