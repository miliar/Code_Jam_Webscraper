#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;

typedef pair<char,char> PCC;

int par[ 110];
map<PCC,char> combine;
map<PCC,bool>opposed;

void print ( int kase, string yes) {
 	cout <<"Case #"<<kase<<": ";
	cout << "[";
	if (yes.size() > 0 ) cout << yes[0];
	for (int i = 1; i < yes.size(); i++) cout<<", " <<yes[i]; cout <<"]";
	cout <<"\n";
 	return ;
}

void Clear() {
	combine.clear(); opposed.clear();
	memset(par, -1, sizeof(par));
}

void makeCombine(int N) {
	string in;
	for (int i =0; i < N ;i++) {
		cin >> in;
		combine[ make_pair(in[0],in[1]) ] = in[2];
		combine[ make_pair(in[1],in[0]) ] = in[2];
	}
	return;
}

void makeOpposed(int N) {
	for (int i = 0; i < N; i++) {
		string in; cin >> in;
		opposed [make_pair(in[0], in[1])] = opposed [make_pair(in[1], in[0])] = true;
	}
}

string processInput(int N) {
	string in; cin >> in;
	string ret = "";
	int pos = 0;
	for (int i = 0; i < N;i++) {
		//cout << "### "<<pos << " " << ret << "\n";
		char curr = in [i];
		if (pos > 0) {
			PCC tmp = make_pair(ret[pos-1], curr);
			if (combine.count(tmp) > 0) {
				ret [pos-1] = combine[tmp];
				continue;
			}
			tmp = make_pair(curr, ret[pos-1]);
			if (combine.count(tmp) > 0){ 
				ret [pos-1] = combine[tmp]; 
				continue;
			}
			for (int j = 0 ; j < pos; j++) {
				tmp = make_pair(ret[j], curr);
				if (opposed[tmp]) { pos = 0; break;}
				tmp = make_pair(curr, ret[j]);
				if (opposed[tmp]) { pos = 0; break;}
			}
			if (pos == 0) continue;
			if (ret.size() > pos) ret[pos]= curr; 
			else ret += curr;
			pos += 1;
		}
		else {
			if (ret.size() > pos) ret [0] = curr;
			else ret += curr;
			pos += 1;
		}
	}
	//cout << ret <<"\t"<<pos<<"\n";
	return ret.substr(0,pos);
}

int main() {
 	freopen ("B-large.in","r",stdin);
 	freopen("B-large.out","w",stdout);
 	int T ,kase = 0; 
 	for ( scanf("%d",&T) ; T ;T-- ) {
		Clear();
		int C,D,N; 
		cin >> C; makeCombine(C);cin>>D;makeOpposed(D); cin >> N;
		print(++kase, processInput(N));
		
	}
	return 0;
}
