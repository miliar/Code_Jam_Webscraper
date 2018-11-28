#include <cstring>
#include <iostream>

#define show(x) cerr<<#x<<'='<<x<<endl
using namespace std;
const int MAXN=1000+10;

bool isMarked[MAXN];
int pow10[10], A, B, ans;
int len(int x) {
	int l=0;
	while (x) {
		l++;
		x/=10;
	}
	return l;
}
int main() {
	pow10[0]=1;
	for (int i=1; i<10; ++i)
		pow10[i]=pow10[i-1]*10;
	int t;
	cin>>t;
	for (int k=0; k<t; ++k) {
		cin>>A>>B;
		memset(isMarked, false, sizeof(isMarked));
		ans=0;
		for (int i=A; i<=B; ++i) {
			if (!isMarked[i]) {
				int l=len(i), x, valid=0, temp=i;
				for (int j=0; temp; ++j, temp/=10)
					if (temp%10) {
						x=(i%pow10[j+1])*pow10[l-j-1]+i/pow10[j+1];
						if (A<=x&&x<=B&&!isMarked[x]) {
							valid++;
							isMarked[x]=true;
						}
					}
				ans+=valid*(valid-1)/2;
			}
		}
		cout<<"Case #"<<k+1<<": "<<ans<<endl;
	}
	return 0;
}
