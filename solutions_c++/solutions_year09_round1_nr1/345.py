#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int nmax=12000001;

short int a[11][nmax];

void trans(int x, int b, int aa[200])
{
	while (x>0) {
		aa[0]++;
		aa[aa[0]]=x%b;
		x/=b;
	}
	return;
}

int num(string g)
{
	int t=0;
	for (int i=0; i<g.size(); i++)
		t=t*10+(g[i]-'0');
	return t;
}

bool solve(int x, int b)
{
	if (x>=nmax) return 0;
	if (a[b][x]>0) return ((a[b][x]-1)==0);
	a[b][x]=2;

	int aa[200];
	memset(aa,0,sizeof(aa));
	trans(x,b,aa);
	int sum=0;
	for (int i=1; i<=aa[0]; i++)
		sum+=aa[i]*aa[i];

	if (solve(sum,b)) a[b][x]=1;
	return ((a[b][x]-1)==0);
}

int test;
vector<int> b;
string s;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	for (int i=1; i<nmax; i++)
		a[2][i]=1;

	for (int i=3; i<=10; i++) {
		a[i][1]=1;
		for (int j=2; j<nmax; j++)
			solve(j,i);
	}
	
	scanf("%i\n",&test);
	for (int tt=1; tt<=test; tt++) {
		printf("Case #%i: ",tt);
		getline(cin,s);
		s+=" ";

		string g="";
		b.clear();
		for (int i=0; i<s.size(); i++) {
			if (s[i]==' ') {
				int t=num(g);
				if (t>0) b.push_back(t);
				g="";
			}
			else g+=s[i];
		}

		for (int j=2; j<nmax; j++) {
			bool fl=1;
			for (int i=0; i<b.size(); i++)
				if (a[b[i]][j]!=1) fl=0;
			if (fl) {
				printf("%i\n",j);
				break;
			}
		}
	}

	return 0;
}
