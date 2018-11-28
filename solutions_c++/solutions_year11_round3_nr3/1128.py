#include <iostream>
#include <vector>
using namespace std;

#define INPUT_FILE "in.txt"
#define OUTPUT_FILE "out.txt"

#define ABS(a) (a<0?-a:a)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,a,b) for(int i=(a); i<=(b); i++)
#define REP(i,n) FOR(i,0,n)
#define SZ(v) ((int)(v).size())
typedef long long ll;

int main()
{
	freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
	
	int T, N;
	int L, H;
	int freqs[10000];
	
    cin >> T;
    for (int t = 0; t < T; t++)
    {
		int res = -1;
        cout << "Case #" << (t+1) << ": ";
		cin >> N >> L >> H;
		REP(n,N)
		{
			cin >> freqs[n];
		}	
		for (ll f=L; f<=H; f++) 
		{
			int n;
			for (n=0;n<N;n++)
			{
				if((f%freqs[n]!=0)&&(freqs[n]%f!=0))
				{
					break;
				}				
			}
			if(n==N)
			{
				res = f;
				break;
			}
		}
		if(res!=-1)
		{
			cout << res << endl;
		}
		else
		{
			cout << "NO" << endl;
		}
    }
	return 0;
}
