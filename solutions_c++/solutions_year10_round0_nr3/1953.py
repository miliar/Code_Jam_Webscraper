#include <fstream>
#include <string>

using namespace std;
ifstream fin("C-large.in");
ofstream fout("C-large.out");
const int MNAX = 1000;

long long a[MNAX+2];
long long sum[MNAX+2];
long long next[MNAX+2];
int main(){
	long long test, t;
	fin>>test;
	for (t=1;t<=test;++t){
		memset(sum,0,sizeof(long long)*(MNAX+2));
	
		long long ans = 0;
		long long r,k,n,i;
		fin>>r>>k>>n;
		for (i=1;i<=n;++i){
			fin>>a[i];
		}
		for (long long beg=1;beg<=n;++beg){
			bool bl = true;
			for (i=beg;i<=n;++i){
				sum[beg]+=a[i];
				if (sum[beg]>k){
					sum[beg]-=a[i];
					next[beg]=i;
					bl = false;
					break;
				}
			}
			if (bl==true){
				for (i=1;i<beg;++i){
					sum[beg]+=a[i];
					if (sum[beg]>k){
						sum[beg]-=a[i];
						next[beg]=i;
						bl = false;
						break;
					}
				}
			}
			if (bl==true){
				next[beg] = beg;
			}
		}
		
		long long kk = 1;
		for (i=1;i<=r;++i){
			ans += sum[kk];
			kk = next[kk];
		}

		fout<<"Case #"<<t<<": "<<ans<<'\n';
	}
	return 0;
}