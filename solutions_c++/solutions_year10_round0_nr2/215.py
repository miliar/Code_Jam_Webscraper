#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define pi 3.141592653589
#define sqr(x) ((x)*(x))
#define Max(a,b) ((myless(a,b))?(b):(a))
#define Min(a,b) ((myless(a,b))?(a):(b))

using namespace std;

typedef long long ll;
typedef long double ld;

void out(const vector <int> &a)
{
	for (int i=(int)a.size()-1;i>=0;i--)printf("%d",a[i]);
	printf("\n");
}

int dv(int a,int b)
{
	int c=a/b;
	while (b*c>a)c--;
	return c;
}

int md(int a,int b)
{
	return a-dv(a,b)*b;
}

vector <int> norm (vector <int> a)
{
	for (int i=0;i<(int)a.size();i++){
		if (i==(int)a.size()-1){
			if (dv(a[i],10))a.push_back(dv(a[i],10));
			a[i]=md(a[i],10);
		} else {
			a[i+1]+=dv(a[i],10);
			a[i]=md(a[i],10);
		}
	}
	while (a.size()&&a[a.size()-1]==0)a.pop_back();
	return a;
}

vector <int> operator - (const vector <int> &a,const vector <int> &b)
{
	vector <int> c;
	c.resize(max(a.size(),b.size()));
	for (int i=0;i<(int)c.size();i++)c[i]=(i<(int)a.size()?a[i]:0)-(i<(int)b.size()?b[i]:0);
	return norm(c);
}

bool myless (vector <int> a,vector <int> b)
{
	if (a.size()!=b.size())return a.size()<b.size();
	for (int i=(int)a.size()-1;i>=0;i--)if (a[i]!=b[i])return a[i]<b[i];
	return false;
}

vector <int> div2(vector <int> a)
{
	for (int i=(int)a.size()-1;i>0;i--){
		a[i-1]+=(a[i]&1)*10;
		a[i]>>=1;
	}
	a[0]>>=1;
	return norm(a);
}

vector <int> operator * (vector <int> a,int b)
{
	for (int i=0;i<(int)a.size();i++)a[i]*=b;
	return norm(a);
}

vector <int> gcd(const vector <int> &a,const vector <int> &b)
{
	if (a.size()==0)return b;
	if (b.size()==0)return a;
	if (a[0]%2==0){
		if (b[0]%2==0)return gcd(div2(a),div2(b))*2;else return gcd(div2(a),b);
	} else {
		if (b[0]%2==0)return gcd(a,div2(b));else return gcd(Max(a,b)-Min(a,b),Min(a,b));
	}
}

char s[51];
vector <int> a[1000];

int main()
{
	int T;
	scanf("%d",&T);
	for (int I=0;I<T;I++){
		cerr << I+1 << endl;
		int n;
		scanf("%d",&n);
		
		for (int i=0;i<n;i++){
			scanf("%s",s);
			int l=strlen(s);
			reverse(s,s+l);
			a[i].clear();
			for (int j=0;j<l;j++)a[i].push_back(s[j]-'0');
		}
		sort(a,a+n,myless);
		vector <int> T=a[1]-a[0];
		for (int i=1;i<n;i++){
			T=gcd(T,a[i]-a[0]);
		}
		vector <int> TT,ans=a[0];
		for (int i=0;i<50;i++)TT.push_back(0);
		for (int i=0;i<(int)T.size();i++)TT.push_back(T[i]);
		while (!(myless(TT,T))){
			while (!(myless(ans,TT)))ans=ans-TT;
			for (int i=1;i<(int)TT.size();i++)TT[i-1]=TT[i];
			TT.pop_back();
		}
		printf("Case #%d: ",I+1);
		if (ans.size()){
			ans=T-ans;
			for (int i=(int)ans.size()-1;i>=0;i--)printf("%d",ans[i]);
			printf("\n");
		} else printf("0\n");
	}
	return 0;
}
