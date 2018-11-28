// <-------------------[sWitCHcAsE]---------------------->
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<vector>
#include<map>
#include<cstring>
#include<cassert>
#include<queue>

#define FOR(i,n) for(int i=0;i<n;i++)
#define FORS(i,a,n) for(int i=a;i<n;i++)
#define ERR(x) cerr<<#x<<" "<<x<<endl
#define pb push_back

using namespace std;

typedef vector<int> VI;
typedef long long ll;
typedef long double ld;

map<char,char> mappings;

void update(string normal, string gog) {
	FOR(i,normal.size()) {
		if ( mappings.find(gog[i]) != mappings.end()) {
			if ( normal[i] != mappings[gog[i]]) {
				cerr<<"You got a serious problem Dude\n\n";
			}
		}
		else {
			mappings[gog[i]]=normal[i];
		}
	}
}

string convert(string a) {
	string ret="";
	FOR(i,a.size()) {
		ret+=mappings[a[i]];
	}
	return ret;
}

int main(int argc,char** args) {
	update("our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi");
	update("there are twenty six factorial possibilities","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	update("so it is okay if you want to just give up","de kr kd eoya kw aej tysr re ujdr lkgc jv");
	update("qz", "zq");
	/*FOR(i,26) {
		cout<<"Gog of "<<(char)('a' + i)<<" maps to "<<mappings[('a'+i)]<<endl;
	}*/

	int T, kase=1;
	string inp;
	char buff[145];
	scanf("%d\n",&T);
	while(kase<=T) {
		cout<<"Case #"<<kase<<": ";
		cin.getline(buff, 120);
		inp=string(buff);
		cout<<convert(inp)<<endl;
		kase++;
	}
}
