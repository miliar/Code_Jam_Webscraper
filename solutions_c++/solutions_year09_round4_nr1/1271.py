#include <stdio.h>
#include <string.h>
#include <vector>
#include <set>
#include <queue>

using std::queue;
using std::vector;
using std::set;
int n;
char row[50][50];
struct node {
	vector<int> st;
	int num;
};

bool checking(vector<int> &t) {
	for(int i=0;i<n;i++) {
		//printf("%d %d\n",i,t[i]);
		if(t[i] > i+1)
			return false;
	}
	//puts("");
	return true;
}

int main() {
	int t,i,j,ans,c=0;
	
	scanf("%d",&t);
	while(t--) {
		vector<int> s;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			scanf("%s",row[i]+1);
		for(i=1;i<=n;i++) {
			for(j=n;j>0 && row[i][j] == '0';j--);
			s.push_back(j);
		}
		
		/*for(i=0;i<n;i++)
			printf("%d %d\n",i,s[i]);*/
		
		ans = 0;
		queue<node> Q;
		set<vector<int> > state;
		Q.push((node){s,0});
		state.insert(s);
		while(!Q.empty()) {
			node tmp = Q.front();
			//printf("%d\n",tmp.num);
			if(checking(tmp.st)) {
				//puts("AA");
				ans = tmp.num;
				break;
			}
			for(i=0;i<n-1;i++) {
				vector<int> tt = tmp.st;
				int ttt = tt[i];
				tt[i] = tt[i+1];
				tt[i+1] = ttt;
				/*for(j=0;j<n;j++)
					printf("%d ",tt[j]);
				puts("");*/
				if(state.find(tt) == state.end()) {
					//puts("YY");
					state.insert(tt);
					Q.push((node){tt,tmp.num+1});
				}
			}
			Q.pop();
		}
		
		printf("Case #%d: %d\n",++c,ans);
	}
	
	return 0;
}
