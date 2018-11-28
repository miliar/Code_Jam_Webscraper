#define MD(x) if (0) {x;}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <sstream>
void MyAssert(int p){ while (!p) printf("error\n"); };
#define O1(S,A,n) MD(cout<<S<<":";for (int i=0; i<n; i++)cout<<A[i]<<" ";cout<<endl;)
#define O2(S,A,n) MD(cout<<S<<"\n";for (int i=0; i<n; i++){for (int j=0; j<n; j++)cout<<A[i][j]<<" ";cout<<endl;})
using namespace std;

struct pt{
	pt *le,*ri;
	double p;
	string s;
};

set<string> name;

pt * build(istringstream &in){
	pt * r= new pt;
	char ch;
	in>>ch>>r->p>>r->s;
	if (r->s==")"){
		r->le = r->ri = NULL;
		return r;
	}
	r->le = build(in);
	r->ri = build(in);

	in>>ch;
	return r;
}

void tra(pt *r){
	if (!r) return;
	cout<<r->s<<" "<<r->p<<":";
	if (r->le) cout<<r->le->s<<" "<<r->ri->s<<" ";
	cout<<endl;
	tra(r->le);
	tra(r->ri);
}

double solve(pt *r, double p){
	p *= r->p;
	if (r->le==NULL) return p;
	if (name.count(r->s)){
		return solve(r->le,p);
	}
	else{
		return solve(r->ri,p);
	}
}


int main(){
	char buf[1000];
	int tc;
	cin>>tc;
	for (int ti=1; ti<=tc; ti++){
		printf("Case #%d:\n",ti);
		int L;
		cin>>L;
		string input;
		gets(buf);
		for (int i=0; i<L; i++){			
			gets(buf);
			string s(buf);
			MD(cout<<"s:"<<s<<endl;)
			for (int j=0; j<s.size(); j++){
				input = input+s[j];
				if (s[j]=='(' || s[j]==')') input = input+" ";
			}			
			MD(cout<<"input:"<<input<<endl;)
		}
		MD(cout<<input<<"\n------------------\n";)
		istringstream in(input);

		pt *r = build(in);
		MD( tra(r) );
		//return 0;
		name.clear();
		int n;
		cin>>n;
		for (int i=0; i<n; i++){
			string s;
			cin>>s;
			int m;
			cin>>m;
			name.clear();
			for (int j=0; j<m; j++){
				cin>>s;
				name.insert(s);
			}			
			printf("%.10lf\n",solve(r,1));
		}

	}
	return 0;
}
