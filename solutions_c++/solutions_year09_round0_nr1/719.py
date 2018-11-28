#include <iostream>
#include <string>
using namespace std;

int l,d,n;
string s[5001],g;
bool b[20][30];

void null()
{
	for (int i=0; i<20; i++)
		for (int j=0; j<30; j++)
			b[i][j]=0;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cin >> l >> d >> n;
	for (int i=0; i<d; i++)
		cin >> s[i];

	for (int tt=1; tt<=n; tt++) {
		null();
		cin >> g;
		int p=0, t=0;
		for (int i=0; i<g.size(); i++) {
			if (g[i]=='(') t++;
			else if (g[i]==')') t--;
			else b[p][g[i]-'a']=1;
			if (t==0) p++;
		}

		int ss=0;
		for (int i=0; i<d; i++) {
			bool fl=1;
			for (int j=0; j<l; j++)
				if (!b[j][s[i][j]-'a']) fl=0;
			if (fl) ss++;
		}
		printf("Case #%i: %i\n",tt,ss);
	}

	return 0;
}