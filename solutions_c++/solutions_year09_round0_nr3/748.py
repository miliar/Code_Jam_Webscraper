#include <iostream>
#include <string>
using namespace std;

const string s=" welcome to code jam";
const int mod=1000000;
string g;
int test;
int a[21][511];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%i\n",&test);
	for (int tt=1; tt<=test; tt++) {
		getline(cin,g);
		g=" "+g;
		for (int i=0; i<s.size(); i++)
			for (int j=0; j<g.size(); j++)
				a[i][j]=0;
		for (int j=0; j<g.size(); j++)
			a[0][j]=1;
		for (int i=1; i<s.size(); i++)
			for (int j=i; j<g.size(); j++)
				if (s[i]!=g[j]) a[i][j]=a[i][j-1];
				else a[i][j]=(a[i][j-1]+a[i-1][j])%mod;
		printf("Case #%i: ",tt);
		int y=a[s.size()-1][g.size()-1];
		printf("%i%i%i%i", (y/1000)%10, (y/100)%10, (y/10)%10, y%10);
		printf("\n");
	}

	return 0;
}
