#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

vector <string> d;
int l,p,n,t;
vector <vector <char> > w;

void getpredata(){
	scanf("%d %d %d\n",&l,&p,&n);
	d.resize(p);
	//w.resize(p);
	for (int i=0;i<p;i++){
		getline(cin,d[i]);		
	}
}

void getdata(){
	w.clear();
	string s;
	getline(cin,s);
	vector <char> e;
	for (int i=0;i<s.size();i++){
		e.clear();
		if (s[i]=='('){
			i++;
			for (;s[i]!=')';i++){
				e.push_back(s[i]);
			}
		} else 	e.push_back(s[i]);
		w.push_back(e);
	}
}

int solve(){
	getdata();
	int r=0;
	bool b;
	for (int i=0;i<p;i++){
		b=false;
		for (int j=0;j<l;j++){
			b=false;
			for (int k=0;k<w[j].size() && !b;k++){
				if (d[i][j]==w[j][k]) b=true;
			}
			if (!b) break;
		}
		if (b) r++;
	}
	return r;
}


int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	getpredata();
	for (int i=1;i<=n;i++){
		int r=solve();
		printf("Case #%d: %d\n",i,r);
	}
	return 0;
}