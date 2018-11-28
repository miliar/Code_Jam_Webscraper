#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include<sstream>
//#include <vector>
//#include <map>
//#include <set>
//#include <cstdio>
//#include <queue>
//#include <string.h>
//#include <cstdio>
#pragma comment(linker, "/STACK:167772160")
using namespace std;
typedef long long    Int;
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())
const int inf=1000000000;


string s;
char a[200];

int main()
{
	 freopen("input.txt","r",stdin);
	 freopen("output.txt","w",stdout);
a[97]='y';
a[98]='h';
a[99]='e';
a[100]='s';
a[101]='o';
a[102]='c';
a[103]='v';
a[104]='x';
a[105]='d';
a[106]='u';
a[107]='i';
a[108]='g';
a[109]='l';
a[110]='b';
a[111]='k';
a[112]='r';
a[113]='z';
a[114]='t';
a[115]='n';
a[116]='w';
a[117]='j';
a[118]='p';
a[119]='f';
a[120]='m';
a[121]='a';
a[122]='q';

	int tes;
	scanf("%d\n",&tes);
	FOR(o,1,tes)
	{
		getline(cin,s);
		cout<<"Case #"<<o<<": ";
		FOR(j,0,sz(s)-1)
			if(s[j]==' ')cout<<" ";else
				cout<<a[s[j]];
		cout<<endl;
	}
}