#include <cstdio>
#include <vector>

using namespace std;

int n, m;

vector<int>tab[2];
vector<int>which;
int pos[2];
int move[2];
int next;

void step(int x)
{
	if(move[x]==tab[x].size())
		return;
	
	int target = tab[x][move[x]];
	if(pos[x] == target ){
		if(which[next] == x){		// push the button
			next++;
			move[x]++;
		}
		return;
	}
	if(pos[x] > target)
		pos[x]--;
	if(pos[x] < target)
		pos[x]++;
}

int pro()
{
	int result=0;
	while(move[0]<tab[0].size() || move[1]<tab[1].size()){
	//	printf("0: %d %d %d\n", move[0], pos[0], tab[0][move[0]]);
		//printf("1: %d %d %d\n", move[1], pos[1], tab[1][move[1]]);
		step((which[next]+1)%2);
		step(which[next]);
		result ++;
		//printf("%d\n",result);
	}
	return result;
}
int main()
{
	scanf("%d", &n);
	for(int i=1; i<=n; i++){
		scanf("%d ", &m);
		tab[0].resize(0);
		tab[1].resize(0);
		which.resize(0);
		pos[0]=1;
		pos[1]=1;
		move[0]=0;
		move[1]=0;
		next=0;
		for(int j=0; j<m; j++){
			char c;
			int a, b;
			scanf("%c %d ", &c, &a);
			//printf("%c %d\n", c, a);
			if(c=='O')
				b=0;
			else
				b=1;
			tab[b].push_back(a);
			which.push_back(b);
		}
		printf("Case #%d: %d\n", i, pro());
	}
	
	return 0;
}