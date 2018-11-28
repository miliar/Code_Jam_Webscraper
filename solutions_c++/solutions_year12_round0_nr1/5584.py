#include<iostream>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<string>
#include<set>
#include<map>
#include<algorithm>
#include<math.h>
#include<memory.h>
#include<queue>
//#include<unordered_map>
//#include<unordered_set>
using namespace std;

#define all(a) a.begin(),a.end()
#define mp make_pair
#define li long long
#define db long double
#define pi pair<int,int>
#define vi vector<int>
#define INF (li)1000000007
#define mod (li)2011

void solve();

int main ()
{
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#else
	//freopen("input.txt","r",stdin);
	//freopen("input.txt","r",stdin);
#endif
	int t=30;
	char r[111];
	gets(r);
//	cin>>t;
	while(t--)
	{
		printf("Case #%d: ",30-t);
		solve();
		printf("\n");
	}
	return 0;
}
void solve()
{
	string s1="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	string s2="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	int a[333],b[333];
	a['q']='z';
	a['z']='q';
	a[' ']=' ';
	for(int i=0;i<s1.size();i++)
	{
		a[s1[i]]=s2[i];
		b[s2[i]]=s1[i];
	}
	char aa[111111];
	gets(aa);
	int l=strlen(aa);
	for(int i=0;i<l;i++)
	{
		printf("%c",a[aa[i]]);
	}
}