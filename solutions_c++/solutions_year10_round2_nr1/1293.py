#include<iostream>
#include<vector>
using namespace std;
struct vertex {
vector<string> next;
vector<int> num;
};
vertex qq;
vector<vertex> t;
int sv;
void add(const string &s)
{
int v=0,i,j;
string ss;
for(i=0;i<s.length();i++)
{
if(s[i]!='/')
{
ss+=s[i];
}
if(s[i]=='/' && i>0)
{
for(j=0;j<t[v].next.size();j++)
{
if(ss==t[v].next[j])
{
goto l;
}
}
t[v].next.push_back(ss);
t[v].num.push_back(sv);
t.push_back(qq);
t[sv].next.clear();
t[sv].num.clear();
sv++;
l:;
v=t[v].num[j];
ss="";
}
}
}
int counter(const string &s)
{
int v=0,i,j,k=0;
string ss;
for(i=0;i<s.length();i++)
{
if(s[i]!='/')
{
ss+=s[i];
}
if(s[i]=='/' && i>0)
{
for(j=0;j<t[v].next.size();j++)
{
if(ss==t[v].next[j])
{
goto l;
}
}
for(j=i;j<s.length();j++)
{
if(s[j]=='/')
{
k++;
}
}
return k;
l:;
v=t[v].num[j];
ss="";
}
}
return 0;
}
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int tim,ti,n,m,i,j,sum;
string sr;
cin>>tim;
for(ti=1;ti<=tim;ti++)
{
sum=0;
t.clear();
t.push_back(qq);
sv=1;
cin>>n>>m;
for(i=1;i<=n;i++)
{
cin>>sr;
add(sr+'/');
}
for(i=1;i<=m;i++)
{
cin>>sr;
sum+=counter(sr+'/');
add(sr+'/');
}
cout<<"Case #"<<ti<<": "<<sum<<endl;
}
return 0;
}
/*
struct vertex {
	int next[K];
	bool leaf;
};

memset (t[0].next, 255, sizeof t[0].next);
sz = 1;


vertex t[NMAX+1];
int sz;
void add_string (const string & s) {
	int v = 0;
	for (size_t i=0; i<s.length(); ++i) {
		char c = s[i]-'a'; // в зависимости от алфавита
		if (t[v].next[c] == -1) {
			memset (t[sz].next, 255, sizeof t[sz].next);
			t[v].next[c] = sz++;
		}
		v = t[v].next[c];
	}
	t[v].leaf = true;
}       


// set::count
#include <iostream>
#include <set>
using namespace std;

int main ()
{
  set<int> myset;
  int i;

  // set some initial values:
  for (i=1; i<5; i++) myset.insert(i*3);    // set: 3 6 9 12

  for (i=0;i<10; i++)
  {
    cout << i;
    if (myset.count(i)>0)
      cout << " is an element of myset.\n";
    else 
      cout << " is not an element of myset.\n";
  }

  return 0;
}


*/