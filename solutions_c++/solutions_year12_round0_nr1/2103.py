
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <vector>
#include <numeric>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN=100001;
const int INF=0x7FFFFFFF;
const double eps=1e-10;
const double pi=acos(-1.0);

string s1,s2,s3,t1,t2,t3,st;
int ca;
char ch[1000];
int f[300];
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	s1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	s2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	t1="our language is impossible to understand";
	t2="there are twenty six factorial possibilities";
	t3="so it is okay if you want to just give up";
	
	for (int i=0; i<s1.size(); i++) f[s1[i]]=t1[i];
	for (int i=1; i<s2.size(); i++) f[s2[i]]=t2[i];
	for (int i=1; i<s3.size(); i++) f[s3[i]]=t3[i];
	f['z']='q';
	f['q']='z';
	scanf("%d\n",&ca);
	for (int i=1; i<=ca; i++)
	{
		gets(ch);
		st.assign(ch);
		cout<<"Case #"<<i<<": ";
		for (int i=0; i<st.size(); i++) cout<<char(f[st[i]]);
		cout<<endl;
	}
	
	return 0;
}



