#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<map>
using namespace std;

const int INF=1000111222;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

struct Kat {
	map<string,Kat*> dzieci;
	
	int buduj(const vector<string> &v,int poz=0) {
		int vs=v.size(),wynik=0;
		if(poz==vs)
			return 0;
		map<string,Kat*>::iterator it=dzieci.find(v[poz]);
		if(it==dzieci.end()) {
			dzieci[v[poz]]=new Kat();
			++wynik;
		}
		return wynik+dzieci[v[poz]]->buduj(v,poz+1);
	}
	
	void usun() {
		for(map<string,Kat*>::iterator it=dzieci.begin();it!=dzieci.end();++it) {
			//it->second->usun();
			//delete it->second;
		}
	}
};

vector<string> rozbij(string s) {
	vector<string> wynik;
	s+="/";
	int ss=s.size();
	string a;
	for(int i=1;i<ss;++i) {
		if(s[i]=='/') {
			wynik.push_back(a);
			a="";
		} else {
			a+=s[i];
		}
	}
	return wynik;
}

char buf[100003];

int main() {
	int testow;
	scanf("%d",&testow);
	for(int z=1;z<=testow;++z) {
		int wynik=0;
		int n,m;
		scanf("%d%d",&n,&m);
		Kat t;
		for(int i=0;i<n;++i) {
			scanf("%s",buf);
			string temp(buf);
			vector<string> v=rozbij(temp);
			t.buduj(v);
		}
		for(int i=0;i<m;++i) {
			scanf("%s",buf);
			string temp(buf);
			vector<string> v=rozbij(temp);
			wynik+=t.buduj(v);
		}
		t.usun();
		printf("Case #%d: %d\n",z,wynik);
	}
}
