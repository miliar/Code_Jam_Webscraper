#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
typedef long long int64;
typedef long double ld;

const int inf=2000000000;
const ld eps=1e-07;

int a[50][50];
bool opp[50][50];
int kol[50];
vector <int> ans;
int n;

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int t;
	scanf("%d",&t);
	for (int z=1;z<=t;++z){
		int x,y;
		ans.clear();
		for (int i=0;i<50;++i)
			for (int j=0;j<50;++j){
				a[i][j]=-1;
				opp[i][j]=false;
			}
		for (int i=0;i<50;++i)
			kol[i]=0;

		scanf("%d",&y);
		for (int i=0;i<y;++i){
			char c1,c2,c3;
			scanf(" %c %c %c ",&c1,&c2,&c3);
			a[c1-'A'][c2-'A']=c3-'A';
			a[c2-'A'][c1-'A']=c3-'A';
		}
		scanf("%d",&x);
		for (int i=0;i<x;++i){
			char c1,c2;
			scanf(" %c %c ",&c1,&c2);
			opp[c1-'A'][c2-'A']=true;
			opp[c2-'A'][c1-'A']=true;
		}
		scanf("%d",&n);
		int m=0;
		for (int i=0;i<n;++i){
			char c;
			scanf(" %c ",&c);
			ans.pb(c-'A');
			++kol[c-'A'];
			++m;
			if (ans.size()>=2){
				if (a[ans[m-1]][ans[m-2]]>=0){
					--kol[ans[m-1]];
					--kol[ans[m-2]];
					int p=a[ans[m-1]][ans[m-2]];
					--m;
					ans.pop_back();
					ans.pop_back();
					ans.pb(p);
				}
				int last=ans[m-1];
				for (int i=0;i<50;++i)
					if (kol[i]>0 && opp[last][i]){
						ans.clear();
						m=0;
						for (int j=0;j<50;++j)
							kol[j]=0;
						break;
					}
			}
		}
		printf("Case #%d: [",z);
		if (m>0)
			printf("%c",char(ans[0]+'A'));
		for (int i=1;i<m;++i)
			printf(", %c",char(ans[i]+'A'));
		printf("]\n");
	}
	return 0;
}