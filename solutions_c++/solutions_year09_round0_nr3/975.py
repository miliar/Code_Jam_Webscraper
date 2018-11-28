#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>

using namespace std;

//BEIGINTEMPLATE
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(
typedef long long int64;//NOTES:int64
const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-11;//NOTES:eps
template <class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template <class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
typedef pair<int,int> ipair;//NOTES:ipair
//ENDTMPLATE

const int maxL=505;
const int maxn=20;
string s,t("welcome to code jam");
int f[maxL][maxn];

void solve()
{
	int i,j;
	memset(f,0,sizeof(f));
	for(i=0;i<=s.length();i++)f[i][0]=1;
	for(j=1;j<=t.length();j++)
		for(i=1;i<=s.length();i++)
			if(s[i-1]==t[j-1])f[i][j]=(f[i-1][j]+f[i-1][j-1])%10000;else f[i][j]=f[i-1][j]%10000;
	int ans=f[s.length()][t.length()];
	if(ans/1000==0)printf("0");
	if(ans/100==0)printf("0");
	if(ans/10==0)printf("0");
	printf("%d\n",ans%10000);
}

int main()
{
	//freopen("C-test.in","r",stdin);
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-small-attempt0.out","w",stdout);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int i,testcase;
	char tmp[maxL];
	scanf("%d",&testcase);gets(tmp);
	for(i=1;i<=testcase;i++)
	{
		gets(tmp);
		s=tmp;
		printf("Case #%d: ",i);
		solve();
	}
	fclose(stdout);
//	freopen("CON","r",stdin);
//	system("PAUSE");
	return 0;
}