#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

#define X first
#define Y second
int casen=1;
#define caseout cout<<"Case #"<<casen++<<": "
typedef pair<int,int> pii;

int doaction(char me,int &cur,vector<int> &v,vector<char> &c){
	if(cur < v[0]) {
		cur++;
		return 0;
	} else if(cur > v[0]){
		cur--;
		return 0;
	} else if(cur == v[0]){
		if(c[0] != me) return 0;
		v.erase(v.begin());
		return 1;
	}
	return -1;
}
void func(){
	char R;
	int N,P;
	cin>>N;
	vector<int> O,B;
	vector<char> nextaction;
	for(int i=0;i<N;i++){
		cin>>R; cin>>P;
		if(R == 'O') O.push_back(P);
		else B.push_back(P);
		nextaction.push_back(R);
	}
	int curO=1,curB=1,tot=0;
	while(nextaction.size()){
		tot++;
		int r=0;
		for(int i=0;i<2;i++){
			if( (i?O:B).size() == 0) continue;
			r += doaction(i?'O':'B', i?curO:curB, i?O:B, nextaction);
		}
		if(r == 1) nextaction.erase(nextaction.begin());
	}
	caseout<<tot<<endl;
}
int main(){
	int T;
	cin>>T;
	for(int iT=0;iT<T;iT++) func();
	return 0;
}
