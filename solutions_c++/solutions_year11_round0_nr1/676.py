#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAX 105

int main() {
	vector<int> O, B;
	vector< pair<char, int> > seq;
	int T,n,po,pb,pos,i,kase=1,cur,no,nb,res;
	char ch;
	scanf(" %d",&T);
	while(T--) {
		scanf(" %d",&n);
		O.clear(); B.clear(); seq.clear();
		rep(i,n) {
			scanf(" %c %d",&ch, &pos);
			seq.push_back( make_pair(ch, pos) );
			if(ch == 'O') O.push_back(pos);
			else B.push_back(pos);
		}

		po = pb = 1;
		no = nb = 0;
		res = 0;
		rep(i, seq.size()) {
			if(seq[i].first == 'O') {
				cur = abs(seq[i].second - po) + 1;
				po = seq[i].second;
				res += cur;
				no++;

				if(nb < B.size()) {
					if(abs(B[nb] - pb) <= cur) {
						pb = B[nb];
					}
					else if(pb < B[nb]) {
						pb += cur;
					}
					else pb -= cur;
				}

			}
			else {
				cur = abs(seq[i].second - pb) + 1;
				pb = seq[i].second;
				res += cur;
				nb++;

				if(no < O.size()) {
					if(abs(O[no] - po) <= cur) {
						po = O[no];
					}
					else if(po < O[no]) {
						po += cur;
					}
					else po -= cur;
				}
			}
		}//rep i

		printf("Case #%d: %d\n",kase++,res);
	}
	return 0;
}