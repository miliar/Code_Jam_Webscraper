#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define mode 10000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int main()
{
	FILE *in;
	in = fopen("input.txt","rt");
	freopen("output.txt", "w+", stdout);
	int N=0;
	int i;
	char str[501];
	for(char ch=fgetc(in); ch!='\n'; N=N*10+ch-'0', ch=fgetc(in));
	REP (t, N)
	{
		cout << "Case #" << (t+1) << ": ";
		VI count(19,0);
		i=0;
		for(char ch=fgetc(in); ch!='\n' && ch!= EOF; str[i]=ch, ch=fgetc(in), i++);
		str[i]='\0';
		for(int p=i-1; p>=0; p--)
		{
			switch (str[p])
			{
			case 'm': 
				{
					count[18]++;
					count[5]=(count[5]+count[6]) % mode;
					break;
				}
			case 'a': 
				{
					count[17]=(count[17]+count[18]) % mode;
					break;
				}
			case 'j': 
				{
					count[16]=(count[16]+count[17]) % mode;
					break;
				}
			case ' ': 
				{
					count[15]=(count[15]+count[16]) % mode;
					count[10]=(count[10]+count[11]) % mode;
					count[7]=(count[7]+count[8]) % mode;
					break;
				}
			case 'e':
				{
					count[14]=(count[14]+count[15]) % mode;
					count[6]=(count[6]+count[7]) % mode;
					count[1]=(count[1]+count[2]) % mode;
					break;
				}
			case 'd': 
				{
					count[13]=(count[13]+count[14]) % mode;
					break;
				}
			case 'o': 
				{
					count[12]=(count[12]+count[13]) % mode;
					count[9]=(count[9]+count[10]) % mode;
					count[4]=(count[4]+count[5]) % mode;
					break;
				}
			case 'c':
				{
					count[11]=(count[11]+count[12]) % mode;
					count[3]=(count[3]+count[4]) % mode;
					break;
				}
			case 't': 
				{
					count[8]=(count[8]+count[9]) % mode;
					break;
				}
			case 'l': 
				{
					count[2]=(count[2]+count[3]) % mode;
					break;
				}
			case 'w': 
				{
					count[0]=(count[0]+count[1]) % mode;
					break;
				}
			}
		}
		cout << setw(4) << setfill('0') << count[0] << endl;
	}	
	return 0;
}
