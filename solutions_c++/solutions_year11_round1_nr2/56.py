#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#define CLEAR(a) memset(a,0,sizeof(a))
#define ABS(a) ((a)>0?(a):-(a))
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
using namespace std;
typedef pair<int,int> pi;
typedef long long int lld;
typedef vector<int> vi;
typedef string ss;
typedef double lf;
typedef long double llf;


pi alg(int n, string words[], string seq, vector<int> &vec){
	if(vec.size() == 0)
		return MP(-1,-1);
	set<pair<vi,int> > cat[27];
	map<int, vi> masks;
	map<int, int> res;
	cat[0].insert(MP(vec,0));
	int index, resultStringIndex, result = -1;
	for(int i=0; i<seq.size(); i++){
		char letter = seq[i];
		for(set<pair<vi,int> > :: iterator it = cat[i].begin(); it != cat[i].end(); it++){
//			printf("(%d) mam vector i res = %d\n",i, it->ND);
//			for(int j=0; j<it->ST.size(); j++)
//				printf("%d ",it->ST[j]);
//			printf("\n");
			if(it->ND > result){
				resultStringIndex = it->ST[0];
				result = it->ND;
			}
			else if(it->ND == result && resultStringIndex > it->ST[0]){
				resultStringIndex = it->ST[0];
			}
			bool exist = false;
			masks.clear();
			res.clear();
			for(int j=0; j<(it->ST).size(); j++){
				index = it->ST[j];
				int mask = 0;
				for(int q=0; q<words[index].size(); q++)
					if(words[index][q] == letter){
						exist = true;
						mask |= (1<<q);
					}
				masks[mask].PB(index);
				res[mask] = it->ND;
			}
			for(map<int, vi> :: iterator it2 = masks.begin(); it2!=masks.end(); it2++)
				cat[i+1].insert(MP(it2->ND, res[it2->ST] + ((it2->ST==0) && exist?1:0)));
		}
	}
//	printf("returnuje %d %d\n",result, resultStringIndex);
	return MP(result, resultStringIndex);
}


string alg(int n, string words[], string seq){
	int retI = 0;
	int result = -1;
	for(int i=1; i<=10; i++){
		vector<int> vec;
		for(int j=1; j<=n; j++)
			if(words[j].size() == i)
				vec.PB(j);
		pi qq = alg(n, words, seq, vec);
		if(qq.ST > result){
			result = qq.ST;
			retI = qq.ND;
		}
		else if(qq.ST == result && retI > qq.ND)
			retI = qq.ND;
	}
	return words[retI];
}

int t, n, m;
string words[100100], seq;
int testNr;

int main(){
	cin >> t;
	while(t--){
		cin >> n >> m;
		for(int i=1; i<=n; i++)
			cin >> words[i];
		cout << "Case #"<< ++ testNr << ":";
		for(int j=1; j<=m; j++){
			cin >> seq;
			cout << " " << alg(n, words, seq);
		}
		cout<<endl;
	}
}
