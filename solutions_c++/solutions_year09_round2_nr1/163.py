#define DBiG
// Grzegorz Guspiel
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
using namespace std;

#ifdef DBG
#define R(x) cout<<x<<endl
#else
#define R(x)
#endif
#define REP(i,n) for(int (i)=0; (i)<(n); (i)++)
#define FOR(i,b,e) for(int (i)=(b); (i)<=(e); (i)++)

typedef double treal;

const int maxn=100000;
char buf[maxn];
char buf2[maxn];
int pos;
vector<string> feats;

struct tani {
	string feat;
	treal w;
	tani* l;
	tani* r;
	tani(): l(0), r(0) {
		while(buf[pos]!='(') pos++;
		pos++;
		sscanf(buf+pos, "%lf", &w);
		while(buf[pos]!=')'&&!(buf[pos]>='a'&&buf[pos]<='z')) pos++;
		R("value "<<w);
		if(buf[pos]==')') {
			pos++; return;
		}
		sscanf(buf+pos,"%s", buf2);
		feat=buf2;
		R("option "<<feat);
		l=new tani;
		r=new tani;
		while(buf[pos]!=')') pos++;
		pos++;
	}
	bool hasfeat(string s) {
		REP(i,feats.size()) if(feats[i]==s)  return 1;
		return 0;
	}
	treal prob() {
		if(l) {
			if(hasfeat(feat)) return w*l->prob();
			else return w*r->prob();
		} 
		return w;
	}
};

string anis;
string anim;
tani* root;

void get_data() {
	anis="";
	int cnt; scanf("%d\n", &cnt);
	while(cnt--) {
		fgets(buf, maxn, stdin);
		anis+=buf;
		strcpy(buf,anis.c_str());
		pos=0;
	}
		root = new tani;
}

int main() {
	int z; scanf("%d\n", &z);
	REP(zz,z) {
		get_data();
		int anc; scanf("%d\n", &anc);
		printf("Case #%d:\n", zz+1);
		while(anc--) {
			fgets(buf, maxn, stdin);
			feats.clear();
			istringstream ss;
			string stri=buf;
			ss.str(stri);
			string noth;
			ss>>noth;
			int cnt; ss>>cnt;
			while(cnt--) {
				string sa; ss>>sa;
				feats.push_back(sa);
			}
			printf("%.8lf\n", root->prob());
		}
	}
}
