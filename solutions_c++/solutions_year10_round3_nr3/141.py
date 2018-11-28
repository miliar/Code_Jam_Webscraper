#include <cstdio>
#include <cstdlib>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <cctype>
using namespace std;
int nsc, sc;
int h, w;
int board[1010][1010];
bool getbit(int n, int bit){
	return (n&(1<<bit))!=0;
}
void init(){
	scanf("%d %d", &h, &w);
	memset(board, 0, sizeof(board));
	for(int i=0; i<h; i++){
		for(int j=0; j<w/4; j++){
			char c;
			int num;
			scanf(" %c ", &c);
			if (isalpha(c)){
				num=10+c-'A';				
			}
			else{
				num=c-'0';
			}
			for(int k=0; k<4; k++)
				if (getbit(num, k))

					board[i][j*4+3-k]=2;
				else 
					board[i][j*4+3-k]=1;
		}
	}
}
list<int> sizes;
list<int> cnts;
bool chess(int i, int j, int size){
	if (i+size-1>=h || j+size-1>=w) return false;
	for(int ii=i; ii<i+size; ii++){
		if (board[ii][j]==0) return false;
		if (ii>i && board[ii][j]==board[ii-1][j]) return false;
		for(int jj=j+1; jj<j+size; jj++)
			if (board[ii][jj]==0 || board[ii][jj-1]==board[ii][jj]) return false;
	}
	return true;
}
void cutboard(int i, int j, int size){
	for(int ii=0; ii<size; ii++){
		for(int jj=0; jj<size; jj++)
			board[i+ii][j+jj]=0;
	}
}
void incvalue(int &a){
	a++;
}
void solve(){
	sizes.clear();
	cnts.clear();
	while (true){
		int best=0;
		int besti, bestj;
		for(int i=0; i<h; i++)
			for(int j=0; j<w; j++){
				int l=1;
				int r=min(w,h);
				int tmp=0;
				while (l<=r){
					int mid=(l+r)/2;
					if (chess(i,j,mid)){
						l=mid+1;
						tmp=mid;
					}
					else
						r=mid-1;
				}
				if (best<tmp){
					best=tmp;
					besti=i;
					bestj=j;
				}
			}
		if (best>0){
			cutboard(besti, bestj, best);
			if (sizes.size()==0){
				sizes.push_back(best);
				cnts.push_back(1);
			}
			else if (*(sizes.rbegin())==best){
				int acc=*(cnts.rbegin());
				incvalue(*(cnts.rbegin()));
				int now=*(cnts.rbegin());
				now=now;
				
			}
			else{
				sizes.push_back(best);
				cnts.push_back(1);
			}
		}
		else break;
	}
	printf("Case #%d: %d\n", sc, sizes.size());
	for(list<int>::iterator esize=sizes.begin(),
		ecnt=cnts.begin(); esize!=sizes.end(); esize++, ecnt++){
		printf("%d %d\n", *esize, *ecnt);
	}

}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &nsc);
	for(sc=1; sc<=nsc; sc++){
		init();
		solve();
	}
	return 0;
}