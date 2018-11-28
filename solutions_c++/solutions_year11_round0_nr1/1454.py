#include <cstdio>
#include <cmath>
#include <queue>
#include <algorithm>
#define mp(a,b) make_pair(a,b)

using namespace std;

queue< pair<int,int> > g;
int pos[2];
int cre[2];
int chao(int a){
	return a < 0 ? 0 : a;
}
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	char str[4];
	int casos, n, p;
	scanf("%d",&casos);
	for(int i=1; i<=casos; i++){
		scanf("%d",&n);
		for(int j=0; j<n; j++){
			scanf("%s %d",str,&p);
			if(str[0] == 'O')
				g.push(mp(p,0));
			else
				g.push(mp(p,1));
		}
		
		pos[0] = pos[1] = 1;
		int time = 0;
		int but, rob;
		cre[0] = cre[1] = 0;
		while(!g.empty()){
			but = g.front().first;
			rob = g.front().second;
			g.pop();
			time += chao(abs(but-pos[rob]) - cre[rob]) + 1;
			cre[rob^1] += chao(abs(but-pos[rob]) - cre[rob]) + 1;
			cre[rob] = 0;
			pos[rob] = but;
		}
		
		printf("Case #%d: %d\n",i,time);
	}	
}
