#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;

int main() {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int test;scanf("%d",&test);
	for(int no=1;no<=test;++no){
		printf("Case #%d: ",no);
		int n;
		scanf("%d", &n);
		int s = 0;
		vector<int> a;a.push_back(0);
		for(int i=0;i<n;++i){
			int x;scanf("%d",&x);
			a.push_back(x);
			if(x != i+1) ++ s;
		}
		printf("%d\n",s);
	}
}
