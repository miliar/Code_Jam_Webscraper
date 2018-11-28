#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>

using namespace std;

typedef vector<int> VI;
typedef vector< VI > VVI;
typedef long long LL;
const int INF = 1000000001;
typedef pair<int, int> PII;
typedef vector< PII > VPII;
typedef vector< VPII > VVPII;

#define FOR(x,b,e) for(int x=b; x<=(e);++x)
#define FORD(x,b,e) for(int x=b; x>=(e);--x)
#define REP(x,n) for(int x=0;x<(n);++x)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

typedef pair<int,char> PIC;
typedef vector< PIC > VPIC;

int round()
{
	int M;
	cin>>M;
	
	VPIC arr(M);
	VPIC arrO;
	VPIC arrB;
	char turn = 0;
	int O_id = 0,B_id = 0;
	int O_pos = 1, B_pos = 1;
	REP(i,M)
	{
		int b; char r;
		cin>>r>>b;
		arr[i] = PIC(b,r);
		if(r=='B')
			arrB.PB(PIC(b,r));
		else
			arrO.PB(PIC(b,r));
	}
	int cnt = 0;
	while(turn<arr.size())
	{
		cnt++;
		bool did = false;
		if(B_id<arrB.size())
		{
			if(B_pos==arrB[B_id].ST)
			{
				if(arr[turn].ND == 'B')
				{
					did = true;	
					turn++;
					B_id++;
				}

			}
			else if(B_pos<arrB[B_id].ST)
			{
				B_pos++;
			}
			else
			{
				B_pos--;
			}
		}
		if(O_id<arrO.size())
		{
			if(O_pos==arrO[O_id].ST)
			{
				if(arr[turn].ND == 'O' && !did)
				{
					did = true;	
					turn++;
					O_id++;
				}
			}
			else if(O_pos<arrO[O_id].ST)
			{
				O_pos++;
			}
			else
			{
				O_pos--;
			}
		}
	
	}
	cout<<cnt;
	//REP(i,M)
	//{
	//	cout<<arr[i].ND<<arr[i].ST;
	//}
	return 0;

}

int main() {
	int N;
	cin>>N;
	FOR(i,1,N)
	{
		cout<<"Case #"<<i<<": ";
		round();
		cout<<endl;
	}
	return 0;
}
