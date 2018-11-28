#include <cstdio>
#include <deque>
#include <stack>
#include <string>

using namespace std;

#define MAX 54
stack<char> row;
char input[MAX];
char grid[MAX][MAX];
int N,K,T;

bool test(int i, int j, int count) {
	bool r=false,c=false,d1=false,d2=false;
	int t;
	for(t=0;t<count;t++)
		if( i+t>=N || grid[i+t][j]!=grid[i][j]) {
			break;
		};
	if(t==count) return true;

	for(t=0;t<count;t++)
		if(j+t>=N || grid[i][j+t]!=grid[i][j]) {
			//c=false;
			break;
		};
	if(t==count) return true;

	for(t=0;t<count;t++)
		if(j+t>=N || i+t>=N || grid[i+t][j+t]!=grid[i][j])
		{
			//d1=false;
			break;
		};
	if(t==count) return true;

	for(t=0;t<count;t++)
		if(j-t<0 || i+t>=N || grid[i+t][j-t]!=grid[i][j])
		{
			//d2=false;
			break;
		};
	if(t==count) return true;

	return false;
}


int main() {
	
	//freopen("A.in","r",stdin);
	freopen("A-large(2).in","r",stdin);freopen("A-large-attempt0.out","w",stdout);
	scanf("%d",&T);

	for(int cs=1;cs<=T;cs++) {
		scanf("%d%d",&N,&K);
		memset(grid,char(126),sizeof(grid));
		for(int i=0;i<N;i++) {
			//for(int j=0;j<N;j++) {
			//	char tmp;
			//	scanf("%c", tmp);
			//	if(tmp!='.')
			//		row.push(tmp);
			scanf("%s",input);
			for(int k=0; input[k]; k++) {
				if(input[k]!='.')
					row.push(input[k]);
			}
			// save each row
			int j=N-1;
			while(!row.empty()) {
				char tmp;
				tmp=row.top();
				row.pop();
				grid[i][j]=tmp;
				j--;
			}
		}
		// search for row/column/diag
		bool Bwin=false, Rwin=false;
		char player;
		for(int i=0;i<N;i++) {
			if(Bwin && Rwin) break;
			for(int j=0;j<N;j++) {
				if(grid[i][j]!=char(126)) {
					if(grid[i][j]=='B' && !Bwin) {
						Bwin=test(i,j,K);
					}
					if(grid[i][j]=='R' && !Rwin) {
						Rwin=test(i,j,K);
					}
				}
			}
		}

		
		printf("Case #%d: ", cs);
		string ans;
		if(Bwin && Rwin)
			ans="Both";
		if(Bwin && !Rwin)
			ans="Blue";
		if(!Bwin && Rwin)
			ans="Red";
		if(!Bwin && !Rwin)
			ans="Neither";
		printf("%s\n",ans.c_str());
			
	}
	return 0;
}