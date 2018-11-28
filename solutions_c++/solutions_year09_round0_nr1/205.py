#include <iostream>
#include <fstream>
#include <string>
#include <queue>

using namespace std;


int L, D, N;

class DictLetter {
public:
	DictLetter() {
		for(int i = 0; i < 26; i ++) {
			this->next[i] = 0;
		}
	}

	DictLetter *next[26];
};

class Dict {
public:
	Dict() {
		wTree = new DictLetter();
	}

	void addWord(string word) {
		DictLetter* h = wTree;
		for(int i = 0; i < L; i ++) {
			int v = word[i] - 'a';
			if(!h->next[v]) {
				h->next[v] = new DictLetter();
			}
			h = h->next[v];
		}
	}

	int matchPattern(string p) {
		queue<DictLetter*> *q = new queue<DictLetter*>;
		queue<DictLetter*> *nq = new queue<DictLetter*>;
		queue<DictLetter*> *tq;
		q->push(wTree);
		int ind = 0;
		string s;
		for(int i = 0; i < L; i ++) {
			s.clear();
			if(p[ind] == '(') {
				ind ++;
				while(p[ind] != ')') {
					s.push_back(p[ind]);
					ind ++;
				}
			} else {
				s.push_back(p[ind]);
			}
			ind ++;
			
			while(!q->empty()) {
				DictLetter *l = q->front();
				q->pop();
				for(unsigned int j = 0; j < s.size(); j ++) {
					if(l->next[s[j] - 'a'])
						nq->push(l->next[s[j] - 'a']);
				}
			}

			tq = q; q = nq; nq = tq;
		}
		return q->size();
	}

private:
	DictLetter *wTree;
};

int main() {

//	ifstream fin("A-small.in");
//	#define cin fin
	cin >> L >> D >> N;
	Dict* dict = new Dict();
	string str;
	for(int i = 0; i < D; i ++){
		cin >> str;
		dict->addWord(str);
	}
	for(int i = 1; i <= N; i ++){
		cin >> str;
		cout << "Case #" << i << ": " << dict->matchPattern(str) << endl;
	}
	return 0;
}
