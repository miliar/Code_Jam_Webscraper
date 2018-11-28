#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;
int N;
char memo[11][1000000];
char flag[11][1000000];
int base[12], bi = 0;
string s;
int f(int base, int n)
{
	if(flag[base][n]) return memo[base][n];
	flag[base][n] = 1;
	if(n == 1) return memo[base][n] = 1;
	int t = n, sum = 0;
	while(t)
	{
		sum += (t % base) * (t % base);
		t /= base;
	}
	return memo[base][n] = f(base, sum);
}
void init()
{
	//memset(flag, 0, sizeof(flag));
	int k, i;
	for(k = 2; k <= 10; k++)
	{

		for(i = 2; i < 100000; i++)
		{
			memo[k][i] = f(k, i);
			//if(i == 3) 
			//	cout<<char(memo[k][i] + '0')<<endl;
		}
	}
}
int main()
{
//	freopen("A-small-attempt0.in", "r", stdin);
	freopen("in.txt", "r", stdin);
//	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	init();
	int Case;
	cin>>N;
	cin.ignore();
	for(Case = 1; Case <= N; Case++)
	{
		getline(cin, s);
		//cout<<s<<endl;
		istringstream istr(s);
		int b;
		bi = 0;
		while(istr>>b) base[bi++] = b;
		int i, k;
		for(i = 2; i < 1000000; i++)
		{	
			int ret = 1;
			for(k = 0; k < bi; k++)
				ret &= memo[base[k]][i];
			if(ret) break;
		}
		cout<<"Case #"<<Case<<": "<<i<<endl;
		//printf("Case #%d: %d\n", Case, i);
	}
	return 0;
}