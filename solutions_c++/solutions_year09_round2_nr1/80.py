#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <list>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define rep2(i,x,m) for(int i=x;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
int oo = (int) 1e9;
string s;
set<string> st;
int N,n,a;
struct node{
	double p;
	string x;
	node * l;
	node * r;
	void pp(int l1=0){
		rep(i,l1)
			cout<<" ";
		cout<<p;
		if(x.sz){
			cout<<" "<<x<<endl;
			l->pp(l1+1);
			r->pp(l1+1);
		}
		else
			cout<<endl;
	}
};
node * cast(int ind){
	node * ret=new node();
	string temp="";
	int cur=ind+1;
	while(s[cur]=='.' || isdigit(s[cur]))
		temp+=s[cur++];
	ss S(temp);
	S>>ret->p;
	ret->x="";
	if(s[cur]!=')'){
		while(s[cur]!='(')
			ret->x+=s[cur++];
		ret->l=cast(cur);
		cur++;
		int cnt=1;
		while(cnt){
			if(s[cur]=='(')
				cnt++;
			if(s[cur]==')')
				cnt--;
			cur++;
		}
		ret->r=cast(cur);
	}
	return ret;
}
node * root;
double get(node * nn){
	double ret=nn->p;
	if(nn->x.sz){
		if(st.count(nn->x))
			ret*=get(nn->l);
		else
			ret*=get(nn->r);
	}
	return ret;
}
int main() {
//#define SAMPLE
#ifndef SAMPLE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
#ifdef SAMPLE
	freopen("a.txt", "rt", stdin);
#endif
	cin>>N;
	rep(nn,N){
		cout<<"Case #"<<nn+1<<":"<<endl;
		cin>>n;
		string l;
		getline(cin,l);
		s="";
		rep(i,n){
			getline(cin,l);
			s+=l;
		}
		rep(i,s.sz)
			if(s[i]==' ')
				s.erase(s.begin()+i--);
		n=s.sz;
		root=cast(0);
		//root->pp();
		//cout<<s<<endl;
		cin>>n;
		rep(i,n){
			cin>>s;
			cin>>a;
			st.clear();
			rep(j,a){
				cin>>s;
				st.insert(s);
			}
			printf("%.7lf\n",get(root));
		}
	}
	return 0;
}
