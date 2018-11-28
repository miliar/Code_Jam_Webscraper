#include <stdio.h>
#include <vector>
using namespace std;

int n,m;
char board[600][600];
int main() {
	int id=1;int t;scanf("%d",&t);
	while(t--) {
		vector<int>ile;
		vector<int>dl;
		scanf("%d%d",&n,&m);
		int size=min(n,m);
		for(int i=0;i<n;i++) {
			char tmp[100];
			scanf("%s",tmp);
			for(int i2=0;i2<m;i2++) {
				int wart=tmp[i2/4];if(wart<='9'&&wart>='0') wart-='0'; else wart=10+wart-'A';
				board[i][i2]=((wart>>(3-i2%4))&1) + '0';
			}
			board[i][m]=0;
		}
		//for(int i=0;i<n;i++) printf("%s\n",board[i]);
		
		for(int i=size;i>=1;i--) {
			int ileich=0;
			for(int k=0;k<n-i+1;k++) for(int k2=0;k2<m-i+1;k2++) if(board[k][k2]!='#')  {
				int ok=1;
				for(int l=0;l<i&&ok;l++) {
					if(l>0) {
						ok=ok&&board[k+l][k2]!='#'&&board[k+l][k2]!=board[k+l-1][k2];
					}
					for(int l2=1;l2<i;l2++) {
						if(board[k+l][k2+l2]=='#'||board[k+l][k2+l2]==board[k+l][k2+l2-1]) {
							ok=0;
							break;
						}
					}
				}
				if(ok) {
					for(int l=0;l<i;l++) for(int l2=0;l2<i;l2++) board[k+l][k2+l2]='#';
					ileich++;
				}
			}
			if(ileich>0) {
				ile.push_back(ileich);
				dl.push_back(i);
			}
		}
		printf("Case #%d: %d\n",id++,ile.size());
		for(int i=0;i<ile.size();i++) {
			printf("%d %d\n",dl[i],ile[i]);
		}
	}
	return 0;
}
