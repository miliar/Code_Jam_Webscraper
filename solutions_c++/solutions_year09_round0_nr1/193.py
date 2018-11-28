#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <inttypes.h>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

#define tr(it,s) for(typeof(s.begin())it=s.begin();it!=s.end();++it)
#define rep(i,n) for(int i=0; i<n; ++i)
#define cont(s,u) (s.find(u) != s.end())

const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }


struct TrieNode {
	public:
		char ch;
		map<char, TrieNode*> dic;

		TrieNode(char ch_): ch(ch_) {}

		void add(string word, int pos = 0) {
			if (pos < word.size()) {
				if (!cont(dic,word[pos]))
					dic[word[pos]] = new TrieNode(word[pos]);
				dic[word[pos]]->add(word,pos+1);
			}
		}

		void print(int tab = 0) {
			rep(i,tab) cout << "+";
			cout << ch << endl;
			tr(it, dic) {
				it->second->print(tab+1);
			}
			
		}

		long search(string word, int pos = 0) {
			if (pos == word.size()) return 1;

			vector<char> possible;
			int n_pos;
			if (word[pos] != '(') {
				possible.push_back(word[pos]);
				n_pos = pos + 1;
			} else {
				for (n_pos = pos + 1; word[n_pos] != ')'; n_pos++)
					possible.push_back(word[n_pos]);
				n_pos++;
			}
			long ans = 0;
			rep(i, possible.size()) {
				if (cont(dic,possible[i])) {
					ans += dic[possible[i]]->search(word,n_pos);
				}
			}
			return ans;
		}

		~TrieNode() {
			tr(it, dic)
				delete it->second;
		}
};

int main() {
	int L, D, N;
	string word;

	TrieNode root(' ');

	scanf("%d %d %d", &L, &D, &N);

	rep(i,D) {
		cin >> word;
		root.add(word);
	}

	//root.print();

	rep(i,N) {
		cin >> word;
		cout << "Case #" << i+1 << ": " << root.search(word) << endl;
	}


}
