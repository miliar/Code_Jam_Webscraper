#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
#include<map>
using namespace std;

#define MAXC 38
#define MAXD 30
#define MAXN 102

int t, c, d, n;
//char cm[MAXC][4], op[MAXD][3], base[MAXN];
string base;
//char ans[MAXN];
string ans;
map<char, char> op;
map<string, char> cm;
//	{Q, W, E, R, A, S, D, F}
void solve()
{
	for(int i=0; i<n; i++)
	{
		if(ans.empty()) { ans+=base[i]; continue; }
		string t = ans.substr(ans.size()-1);	//??
		t.append(1, base[i]);
		if(cm.find(t) != cm.end())	//?
			ans[ans.size()-1] = cm[t];
		else if(ans.find(op[base[i]], 0) != string::npos)	//ÕÒµ½
			ans.clear();
		else ans+=base[i];
	}
}


void read()
{
	if(!cm.empty()) cm.clear();
	if(!op.empty()) op.clear();
	if(!ans.empty()) ans.clear();
//	scanf("%d", &c);
	cin>>c;
	for(int i=0; i<c; i++)
	{
		string t;
		cin>>t;
		cm[t.substr(0, 2)] = t[2];	//!!
		char ch = t[0];
		t[0] = t[1];
		t[1] = ch;
		cm[t.substr(0, 2)] = t[2];	//!!
	}
//	scanf("%d", &d);
	cin>>d;
	for(int i=0; i<d; i++)
	{
		string t;
		cin>>t;
		op[t[0]] = t[1];
		op[t[1]] = t[0];
	}
//	scanf("%d", &n);
	cin>>n;
	cin>>base;
}
void print()
{
	if(ans.empty()) {cout<<"[]"<<endl; return;}
	for(int i=0; i<(int)ans.size(); i++)
	{
		if(i==0) cout<<'[';
		cout<<ans[i];
		if(i!=ans.size()-1) cout<<", ";
		else cout<<']'<<endl;
	}
}
int main()
{
//	scanf("%d", &t);
	cin>>t;
	for(int i=1; i<=t; i++)
	{
		cout<<"Case #"<<t<<": ";	//+[E, A] \n
		read();
		solve();
		print();
	}
}