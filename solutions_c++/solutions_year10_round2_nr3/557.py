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
int p[26];
int main()
{
	int tc;
	scanf("%d",&tc);
	p[1]=-1;
	int caseno=1;
	while(tc--){
		int n;
		scanf("%d",&n);
		int tk=n-2;
		int t2k=1<<tk;
		int cnt=0;
		for(int i=0;i<t2k;i++){
		//	memset(p,-1,sizeof(p));
			int pos=0,s=1;
			for(int j=2;j<n;j++,s<<=1){
				if((i&s)!=0){pos++;p[j]=pos;}
				else p[j]=-1;
			}
			p[n]=pos+1;
			//cout<<p[n]<<" "<<p[2]<<endl;
			int st=n;
			while(true){
				st=p[st];
				if(p[st]==-1)break;
			}
			if(st==1){cnt++;}
		}
		cnt%=100003;
		printf("Case #%d: %d\n",caseno++,cnt);
	}
	return 0;
}
