#include<fstream>
#include<iostream>
#include<vector>
#include<set>
#include<string>
#include<iomanip>
#include<sstream>
using namespace std;

ifstream fin("A-small-attempt1.in");
ofstream fout("aout.txt");

#if 1
#define cin fin
#define cout fout
#endif
#define left lt
#define right rt

set<string> fea;

struct node{
	double p;  string f;  bool leaf;
	node(bool le=false):leaf(le){}
	node(double p, string f, double leaf):p(p), f(f), leaf(leaf){}
};
node tre[10000];
int lens;  
string VS[101];
bool left[101], right[101];
string pat;
void ctr(int id, int st, int ed){
//	cout<<st<<","<<ed<<" "<<string(pat.begin()+st, pat.begin()+ed)<<endl;
	istringstream is(string(pat.begin()+st, pat.begin()+ed));
	tre[id].leaf = true;
	for(int i=st; i<ed; i++) if(pat[i]=='(' || pat[i]==')') {tre[id].leaf=false; break;}
	double pp;  is>>pp;  tre[id].p = pp;
	if(tre[id].leaf) return;
	string feat;  is>>feat;  tre[id].f = feat;
	int ln = 1, rn = 0;
	int sst, eed;
	for(int i=st; i<ed; i++) if(pat[i]=='(') {sst = i; break;}
	for(int i=sst+1; i<ed; i++) {
		if(pat[i]=='(') {ln++;}
		else if(pat[i]==')') rn++;
		if(rn==ln){ eed = i; break; }
	}
	pat[eed] = pat[sst] = ' ';
	ctr(id*2, sst+1, eed);
	ln = 1, rn = 0;
	for(int i=eed+1; i<ed; i++) if(pat[i]=='('){sst = i; break;}
	for(int i=sst+1; i<ed; i++){
		if(pat[i]=='(') {ln++;}
		else if(pat[i]==')') rn++;
		if(rn==ln){ eed = i; break; }
	}
	pat[eed] = pat[sst] = ' ';
	ctr(id*2+1, sst+1, eed);
}

double search(int cur){
	if(tre[cur].leaf) return tre[cur].p;
	if(fea.find(tre[cur].f)!=fea.end()) return tre[cur].p*search(cur*2);
	else return tre[cur].p*search(cur*2+1);
}

int main(){
	int N;  cin>>N;
	for(int c=1; c<=N; c++){
		cin>>lens;
		cout<<"Case #"<<c<<": "<<endl;
		
//		for(int i=0; i<lens; i++) VS[i].clear();
		memset(left, 0, sizeof(left));  memset(right, 0, sizeof(right));
		pat = "";
		for(int i=0; i<lens; i++){
			do{getline(cin, VS[i], '\n');}while(VS[i].size()<1);
			pat += VS[i];
		}
//		cout<<pat<<endl;
		int st = 0, ed = pat.size()-1;
		while(pat[st]!='(') st++;   while(pat[ed]!=')') ed--;
		ctr(1, st+1, ed);
/*		for(int i=1; i<20; i++){
			cout<<i<<":"<<endl;
			cout<<tre[i].p<<" "<<tre[i].f<<endl;
		}*/

		int A;  cin>>A;
		for(int a=0; a<A; a++){
			fea.clear();
			string input, feature;  cin>>input;
			int X;  cin>>X;   for(int i=0; i<X; i++) {
				cin>>feature;  fea.insert(feature);
			}
			cout<<showpoint<<fixed<<setprecision(7)<<search(1)<<endl;
		}
	}
}