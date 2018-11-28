#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream> 
#include <fstream> 
#include <algorithm>
#include <queue>

using namespace std;
typedef long long LL;

ofstream out("B.txt");
ifstream in("C-large.in");

const int MAX = 1009;

int g[MAX], R, K, N;
LL num[MAX*10];
int vst[MAX];

void solve()
{
	queue <int> Q;
	memset(num, 0, sizeof(num));
	memset(vst, 0, sizeof(vst));
	for(int i = 0; i < N; i++) Q.push(i); 
	int x, M = 1;
	int s, len;
	while(1)
	{
		x = Q.front();
		if(num[M] + g[x] <= K)
		{
			num[M] += g[x];
			Q.pop(); Q.push(x);	
		}	
		else if(!vst[x]) vst[x] = M ++;
		else
		{
			s = vst[x];
			len = M - s;
			break;	
		}		
	}
	LL sum = 0, ans = 0;
	for(int i = s+1; i <= s + len; i++) sum += num[i];
//	for(int i = 1; i <= M; i++) cout << num[i] << " ";
//	cout << endl;
//	cout << "s = " << s << endl;
//	cout << "len = " << len << endl;
	for(int i = 1; i <= min(s, R); i++) ans += num[i];
	if(R > s)
	{
		M = R - s;
		ans += sum * (M / len);
		for(int i = 1; i <= M % len; i++) ans += num[s+i];			
	}
	out << ans << endl;								
}

int main()
{
	int T;
	in >> T;
	for(int t = 1; t <= T; t++)
	{
		in >> R >> K >> N;
		LL sum = 0;
		for(int i = 0; i < N; i++)
		{
			in >> g[i];
			sum += g[i];			
		}
		out << "Case #" << t << ": ";
		if(sum <= K)
		{ 
			out << sum*R << endl;
			continue;
		}
		solve();		
	}		
	return 0;
}
