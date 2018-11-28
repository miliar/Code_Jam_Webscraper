#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <set>
#include <sstream>
#include <fstream>
#include <map>
#include <algorithm>
#define sqr(a) (a*a)
#define pb push_back
#define fs first
#define sd second
#define debug(a) cout<<#a<<" = "<<a<<endl;
#define all(a) a.begin(),a.end()
#define forn(i,n) for(int i=0;i<n;i++)
using namespace std;

typedef vector<int> vint;
typedef vector<vector<int> > vvint;

const double EPS=1E-10;

inline long long intpow(long long a,long long n){
	long long r=1;
	while (n){
		if (n&1) {
			r*=a;
		} else {
			a*=a;
			n=n>>1;
		}
	}
	return r;
}

inline long long hash(string s){
	long long r=0;
	long long p=1;
	long long m=1777;
	for (int i=0;i<s.size();i++){
		r+=s[i]*p;
		p*=m;
	}
	return r;
}

inline short bit(long long a,int p){//p-й бит
	return (a>>p)&1;
}

inline long long gcd(long long a,long long b){//Наименьший общий делитель
	if (a==b) return a;
	if (a==0) return b;
	if (b==0) return a;
	if (a>b) return gcd(a%b,b); else return gcd(a,b%a);
}


vector <string> splitstring(string s,char* tokens){
	bool b[256];
	memset(b,0,sizeof(b));
	for (int i=0;i<strlen(tokens);i++){
		b[int(tokens[i])]=true;
	}
	vector <string> r;
	string t="";
	for (int i=0;i<s.size();i++){
		if (b[s[i]]){
			if (!t.empty()){
				r.push_back(t);
				t.clear();
			}
		} else {
			t+=s[i];
		}
	}
	if (!t.empty()){
		r.push_back(t);
		t.clear();
	}
	return r;
}

vector <int> kmp(string s,string t){//s-строка, t-текст
									//возвращает массив начальных позиций вхождений(0-индексация)
	string r=s+"\r"+t;				//используем непечатаемый символ \r!
	int sz=r.size();
	int ssz=s.size();
	int tsz=t.size();
	vector <int> p(sz);
	p[0]=0;
	int j;
	for (int i=1;i<sz;++i){
		j=p[i-1];
		while (j>0 && r[i]!=r[j]) j=p[j-1];
		if (r[i]==r[j]) ++j;
		p[i]=j;
	}
	vector <int> ans;
	for (int i=s.size()+1;i<sz;i++){
		if (p[i]==ssz){
			ans.push_back(i-ssz-ssz);
		}
	}
	return ans;
}

void dbgVint(vector <int> a){
	for (int i=0;i<a.size();i++){
		printf("%d ",a[i]);
	}
	printf("\n");
}

void dbgVvint(vector <vector <int> > a){
	for (int i=0;i<a.size();i++){
		dbgVint(a[i]);
	}
}

void dbgVstr(vector <string> a){
	for (int i=0;i<a.size();i++){
		printf("%s\n",a[i].data());
	}
}

int main(){
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int t;
	cin >> t;
	for (int q=0; q<t; q++){
		long long l,p,c;
		cin >> l >> p >> c;
		if (l*c == p){
			printf("Case #%d: %d\n",q+1,0);
			continue;
		}
		long long t=l;
		int k=0;
		while (t<p){
			t*=c;
			if (t<p) k++;
		}
		int y=1;
		int u=0;
		while (y<=k){
			y*=2;
			u++;
		}
		printf("Case #%d: %d\n",q+1,u);
	}
	return 0;
}

