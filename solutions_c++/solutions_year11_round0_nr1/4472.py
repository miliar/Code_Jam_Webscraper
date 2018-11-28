#include <vector>
#include <map>
#include <iostream>

using namespace std;

map< char,vector<int> > v;
map<char,vector<int>::iterator> it;
vector<char> seq;
map<char, int> pos;

char other(char r){
	return r == 'O' ? 'B' : 'O';
}

void walk(char r){
	if(*it[r] > pos[r]) pos[r]++;
	if(*it[r] < pos[r]) pos[r]--;
}

int main(int argc, char *argv[]){
	int T, N;
	char r;
	int p;

	vector<int> vo;
	vector<int> vb;
	v['O'] = vo;
	v['B'] = vb;
	
	cin >> T;
	for (int t = 1; t <= T; t++){
		cin >> N;
		v['O'].clear();
		v['B'].clear();
		seq.clear();
		pos['O'] = 1;
		pos['B'] = 1;
		while (N--){
			cin >> r >> p;
			v[r].push_back(p);
			seq.push_back(r);
		}
		int sec = 0;
		it['O'] = v['O'].begin();
		it['B'] = v['B'].begin();
		vector<char>::iterator s = seq.begin();
		while(s != seq.end()){
			sec++;
			walk(other(*s));
			if (*it[*s] == pos[*s]) {it[*s]++; s++;}
			else walk(*s);
		}
		cout << "Case #" << t << ": " << sec << endl;
	}
}
