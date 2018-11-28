#include <cstring>
#include <iostream>

#define X first
#define Y second
#define show(x) cerr<<#x<<'='<<x<<endl
using namespace std;
const int MAXN=1000+10;
typedef pair<int, int> pii;
pii lev[MAXN];
int n, rem, stars, ans;
char mark[MAXN];

int main() {
	int T;
	cin>>T;
	for (int testnum=0; testnum<T; ++testnum) {
		memset(mark, 0, sizeof(mark));
		cin>>n;
		for (int i=0; i<n; ++i)
			cin>>lev[i].X>>lev[i].Y;
		rem=n; stars=0; ans=0;
		bool isbad=true;
		while (rem&&isbad) {
			isbad=false;
			bool f=true;
			while (f) {
				f=false;
				for (int i=0; i<n; ++i) 
					if (mark[i]==0&&lev[i].Y<=stars) {
						mark[i]=2;
						stars+=2;
						ans++;
						rem--;
						isbad=f=true;
					}
					else if (mark[i]==1&&lev[i].Y<=stars) {
						mark[i]=2;
						stars+=1;
						ans++;
						rem--;
						isbad=f=true;
					}
			}
			int maxb=-1, ind;
			bool find=false;
			for (int i=0; i<n; ++i)
				if (mark[i]==0&&lev[i].X<=stars&&maxb<lev[i].Y) {
					isbad=find=true;
					ind=i;
					maxb=lev[i].Y;

				}
			if (find) {
				mark[ind]=1;
				stars+=1;
				ans++;
			}
		}
		if (rem) 
			cout<<"Case #"<<testnum+1<<": "<<"Too Bad"<<endl;
		else
			cout<<"Case #"<<testnum+1<<": "<<ans<<endl;

	}
	return 0;
}
