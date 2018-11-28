#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <cfloat>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <complex>

using namespace std;

#define pb push_back
#define L(s) (int)((s).end()-(s).begin())
#define rep(i,n) for(int (i)=0;(i)<(n);++(i))
#define all(s) (s).begin(),s.end()
#define pi 3.1415926535897932384626433832795
#define vi vector<int>
#define inf 1000000000
#define ll long long
#define C(a) memset((a),0,sizeof((a)))
#pragma comment(linker, "/STACK:16777216")
vector<char> v;
char ch;
string w="welcome to code jam";
int a[505][20],t,n;
int main()
{	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	scanf("%c",&ch);
	for(int test=1;test<=t;++test)
	{
		v.clear();
		do
		{
			scanf("%c",&ch);
			if (ch!='\n')
				v.pb(ch);
		}while(ch!='\n');
		C(a);
		int n=L(v);
		for(int i=0;i<n;++i)
		{
			if (v[i]==w[0])
				a[i][0]=1;
			for(int k=1;k<=18;++k)
				if (v[i]==w[k])
					for(int j=0;j<i;++j)
						a[i][k]=(a[i][k]+a[j][k-1])%10000;
		}
		int rez=0;
		for(int i=0;i<n;++i)
			rez=(rez+a[i][18])%10000;
		cout<<"Case #"<<test<<": ";
			cout<<rez/1000<<(rez/100)%10<<(rez/10)%10<<rez%10<<endl;
	}
	return 0;
}