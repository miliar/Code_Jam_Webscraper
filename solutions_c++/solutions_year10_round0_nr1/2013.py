#include <fstream>
#include <string>

using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");
const int MNAX = 100;

int a[MNAX+2];
int main(){
	memset(a,0,sizeof(int)*(MNAX+2));
	int test, t;
	fin>>test;
	for (t=1;t<=test;++t){
		string ans = "ON";
		int n,k;
		fin>>n>>k;
		int i = 1;
		while (k>0){
			a[i] = k%2;
			k /= 2;
			++i;
		}
		--i;
		if (n>i) ans = "OFF";
		else{
			for (int j=1;j<=n;++j){
				if (a[j]==0){
					ans = "OFF";
					break;
				}
			}
		}
		fout<<"Case #"<<t<<": "<<ans<<'\n';
	}
	return 0;
}