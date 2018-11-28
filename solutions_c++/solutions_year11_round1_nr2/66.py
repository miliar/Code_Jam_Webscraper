#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<vector<int> > orders;

int cmpon=-1;

bool cmp(int i, int j) {
	return orders[cmpon][i] < orders[cmpon][j];
}

vector<string> newwords;
bool cmp1(int i, int j) {
	return newwords[i] < newwords[j];
}

const int dbg=0;

pair<int,int> distinguish(const vector<string>& words, vector<int> subset, const string& seq, int s=0) {
	if(dbg) cout << string(2*s, ' ') << seq[s] << " ";
	if(dbg) for(int i=0; i<subset.size(); i++) cout << words[subset[i]] << " ";
	if(dbg) cout << endl;
	if(s==seq.size()) return make_pair(0, *min_element(subset.begin(), subset.end()));
	if(subset.size()==1) return make_pair(0, subset[0]);
	cmpon=seq[s]-'a';
	sort(subset.begin(), subset.end(), cmp);
	pair<int,int> ret(-1000000,-1);
	for(int i=0; i<subset.size();) {
		int i2;
		for(i2=i; i2<subset.size() && orders[cmpon][subset[i]]==orders[cmpon][subset[i2]]; i2++);
		pair<int,int> tret = distinguish(words, vector<int>(subset.begin()+i, subset.begin()+i2), seq, s+1);
		cmpon=seq[s]-'a';
		if(dbg) cout << string(2*s, ' ') << " splitting on " << seq[s] << " ";
	        if(dbg) for(int j=i; j<i2; j++) cout << words[subset[j]] << orders[cmpon][subset[j]] << " ";
		if(dbg) cout << i << " " << i2 << " " << tret.first << " " << tret.second << endl;
		if(i==0 && i2==subset.size() && orders[cmpon][subset[i]]<=-1) return tret;
		if(orders[cmpon][subset[i]]<=-1) tret.first++;
		if(dbg) cout << string(2*s, ' ') << " splitting on " << seq[s] << " " << i << " " << i2 << " " << tret.first << " " << tret.second << endl;
		if(tret.first > ret.first || (tret.first==ret.first && tret.second<ret.second)) ret=tret;
		//ret = max(ret, tret);
		i=i2;
	}
	if(dbg) cout << string(2*s, '.') << seq[s] << " ";
	if(dbg) for(int i=0; i<subset.size(); i++) cout << words[subset[i]] << " ";
        if(dbg) cout << ret.first << " " << ret.second << endl;
	return ret;
}

int main(void) {
	int T;
	cin >> T;
	//cout << char('z'+1) << endl;
	//cout << char('a'-1) << endl;
	for(int ts=1; ts<=T; ts++) {
		int N,M;
		cin >> N >> M;
		vector<string> words(N);
		for(int i=0; i<N; i++) cin >> words[i];

		orders.clear();
		for(int i=0; i<27; i++) {
			newwords = words;
		       	for(int j=0; j<newwords.size(); j++) for(int k=0; k<newwords[j].size(); k++)
				if(newwords[j][k]!='a'+i) newwords[j][k]='_';
			vector<int> ord(words.size());
			for(int i=0; i<words.size(); i++) ord[i]=i;
			sort(ord.begin(), ord.end(), cmp1);
			vector<int> ord2(words.size());
			for(int i=0; i<words.size();) {
				int wi=i;
				if(newwords[ord[i]]==string(newwords[ord[i]].size(), '_')) wi=-1-i;
				int i2;
				for(i2=i; i2<ord.size() && newwords[ord[i2]]==newwords[ord[i]]; i2++) {
					ord2[ord[i2]]=wi;
				}
				i=i2;
			}
			//for(int i=0; i<words.size(); i++) cout << words[i] << " " << newwords[i] << " " << ord[i] << " " << ord2[i];
			//cout << endl;
			orders.push_back(ord2);
		}

		cout << "Case #" << ts << ":";
		for(int m=0; m<M; m++) {
			string seq;
			cin >> seq;
			seq = '{' + seq;
			if(dbg) cout << seq << endl;
			vector<int> subset(N);
			for(int i=0; i<N; i++) subset[i]=i;
			cout << " " << words[distinguish(words, subset, seq).second];
		}
		cout << endl;
	}
}
