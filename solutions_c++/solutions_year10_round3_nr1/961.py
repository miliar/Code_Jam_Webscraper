#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
#define f first 
#define s second 

int tt,n,res;
pair<int,int> t[1001];

int main() {
	scanf("%d",&tt);
	for(int cnt = 1; cnt <= tt; ++cnt) {
		scanf("%d",&n);
		res=0;
		for(int i = 0; i < n; ++i) scanf("%d%d",&t[i].f,&t[i].s);
		
		sort(t,t+n);

		for(int a = 0; a < n; ++a) 
			for(int b = a+1; b < n; ++b) 
				if(t[b].s<t[a].s) ++res;	
		printf("Case #%d: %d\n",cnt,res);
	}

}
