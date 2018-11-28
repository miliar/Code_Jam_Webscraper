#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define eps 1e-8
using namespace std;

bool operator <(pair<int,int> a, pair<int, int> b){
	return (a.first<b.first && a.second<b.second);
}

int main(){
	//freopen("A-large(3).in","r",stdin);
	//freopen("out5.txt","w",stdout);
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		int k;
		cin>>k;
		int c=0;
		pair<int,int> p[1004];
		for(int i=0;i<k;i++){
			int a,b;
			cin>>a>>b;
			p[i]=make_pair(a,b);
		}
		sort(p,p+k);
		for(int i=0;i<k;i++){
			for(int j=i+1;j<k;j++){
				if ((p[i].first<p[j].first && p[i].second>p[j].second) || (p[i].first<p[j].first && p[i].second>p[j].second)) c++;
			}
		}
		
		printf("Case #%d: %d\n",i,c);

	}
	return 0;
}

