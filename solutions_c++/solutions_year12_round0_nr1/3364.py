#include <iostream>
#include <string>

using namespace std;

string a[4]=
{
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv",
	"zqey"
};

string b[4]=
{
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up",
	"qzoa"
};

char d[256];
int T;
string s;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	for(int i=0; i<4; ++i)
		for(int j=0; j<a[i].size(); j++)
			d[a[i][j]]=b[i][j];
	cin>>T;
	getline(cin, s);
	for(int i=0; i<T; i++)
	{
		getline(cin, s);
		printf("Case #%d: ", i+1);
		for(int j=0; j<s.size(); j++)
		{
			cout<<d[s[j]];
		}
		cout<<endl;
	}

	fclose(stdout);
}