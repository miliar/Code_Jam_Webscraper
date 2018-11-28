// Author : Team Heisenbug
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <cstring>
#include <sstream>
using namespace std;

#define F first
#define S second
#define mp make_pair
#define pb push_back
typedef vector<int> VI;
typedef vector<VI> VII;
typedef pair<int,int> PII;
typedef long long LL;
set < pair<int,int> > SET;
int main() {
	int T;
	scanf("%d",&T);
	for(int cno=1;cno<=T;cno++) {
		SET.clear();
		int A,B;
		int cnt = 0;
		scanf("%d %d",&A,&B);
		for(int n=A;n<B;n++) {
				stringstream T;
				T<<n;
				string ST = T.str();
				for(int i=1;i<ST.size();i++){
					//Everything before i becomes a part of the number, after i becomes another
					if(ST[i] != '0') {
						int m = 0;
						for(int j=i;j<ST.size();j++) {
							m = m * 10 + (ST[j]-'0');
						}
						for(int j=0;j<i;j++) {
							m = m * 10 + (ST[j]-'0');
						}

						if(n<m && m<=B) {
							SET.insert(mp(n,m));
						}
					}
				}
		}
		printf("Case #%d: %d\n",cno,SET.size());
	}
	return 0;
}

