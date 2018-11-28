#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf(" %d",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define inf 1e9
#define pb push_back

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double D;
typedef long long LL;

struct data {
	D v;
	string name;
};

int L,p,yo;
string test,temp;
VS fin;
data M[200];

void formtree(int a) {
	int k,cnt=0;
	D x;
	while(1) {
		if(test[p]=='(') { k=p++; break; }
		p++;
	}
	while(1) {
		if(test[p]!=' ') {
			x=(test[p]-'0');
			break;
		}
		p++;
	}
	p++;
//	cout<<test[p]<<endl;
	p++;
	cnt=0;
	while(1) {
		if(!(test[p]>='0' && test[p]<='9')) break;
		x=(x*10)+(test[p]-'0');
		p++;
		cnt++;
	}
	k=1;
	REP (i,cnt) k*=10;
	x/=k;
	while(1) {
		if(test[p]!=' ') {
			if(test[p]==')') { M[a].v=x; M[a].name="";}
			else {
				while(1) {
					if(test[p]!=' ') break;
				}
				M[a].v=x;
				while(1) {
					if(test[p]>='a' && test[p]<='z') M[a].name.pb(test[p++]);
					else break;
				}
				formtree(2*a);
				formtree(2*a+1);
			}
			break;
		}
		p++;
	}
}

D give(int a) {
//	cout<<a<<endl;
	D ans=M[a].v;
	if(M[a].name=="") return ans;
	if(binary_search(fin.begin(),fin.end(),M[a].name)) {
		return ans*give(a*2);
	}
	else return ans*give(a*2+1);
}

void prob() {
	cout<<"Case #"<<++yo<<":"<<endl;
	fflush(stdout);
	int N,f,q,op;
	D ans;
	string an;
	N=GI;
	REP (i,N) {
		cin>>an;
		fin.clear();
		op=GI;
		REP (i,op) { cin>>an; fin.pb(an); }
		sort(fin.begin(),fin.end());
		printf("%0.7f\n",give(1));
	}
}

int main() {
	int _=GI;
	while(_--) {
		test.clear();
		temp.clear();
		fin.clear();
		L=GI;
		getchar();
		test=temp="";
		REP (i,L) {
			getline(cin,temp,'\n');
			test+=temp;
		}
		p=0;
		REP (i,200) {
			M[i].v=0;
			M[i].name="";
		}	
		formtree(1);
		prob();
	}
	return 0;
}

