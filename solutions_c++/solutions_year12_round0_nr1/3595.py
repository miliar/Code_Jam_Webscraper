#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
int mp[128];
int main()
{
	int i,j;
	int T;
	string str;
	string s1,s2;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	s1="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz";
	s2="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq";
	for(i=0;i<128;i++)
		mp[i]=i;
	for(i=0;i<(int)s1.size();i++)
		mp[(int)s1[i]]=s2[i];
	scanf(" %d ",&T);
	for(i=1;i<=T;i++)
	{
		getline(cin,str);
		for(j=0;j<(int)str.size();j++)
			str[j]=mp[(int)str[j]];
		cout << "Case #" << i << ": " << str << endl;
	}
	return 0;
}
