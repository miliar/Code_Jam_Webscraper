#include <cstdio>
#include <vector>

using namespace std;
typedef vector <int> vi;
#define pb push_back
#define rep(i,n) for (int i=0;i<(n);i++)

int main(){
	freopen("mri.in","r",stdin);
	freopen("mri.out","w",stdout);
	int t=0;
	scanf("%d",&t);
	rep(k,t){
		vector <vi> a;
		vector <double> wp;
		vector <vector <double>> twp;//twp[i][j] - wp of i excluding games with j
		vector <double> owp;
		vector <double> oowp;
		int n=0;
		scanf("%d",&n);
		rep(i,n){
			vi temp;
			int all=0;
			int win=0;
			char s[200];
			scanf("%s",s);
			rep(j,n){
				if (s[j]=='.')temp.pb(-1);
				else {
					all++;
					if (s[j]=='1'){
						win++;
						temp.pb(1);
					}else
					temp.pb(0);
				}
			}
			a.pb(temp);

			vector<double> temptwp;
			wp.pb((double)win/(double)all);
			rep(j,n){
				if(temp[j]==-1){
					temptwp.pb(-1.0);
				}else
				if (temp[j]==0){
					double dou = (double)win/(double)(all-1);
					temptwp.pb(dou);
				}else{
					temptwp.pb((double)(win-1)/(double)(all-1));
				}
			}
			twp.pb(temptwp);
		}
		rep(i,n){
			double temp=0;
			int cnt=0;
			rep(j,n){
				if (a[i][j]!=-1){
					temp+=twp[j][i];
					cnt++;
				}
			}
			owp.pb(temp/(double)cnt);
		}
		rep(i,n){
			double temp=0;
			int cnt=0;
			rep(j,n){
				if (a[i][j]!=-1){
					temp+=owp[j];
					cnt++;
				}
			}
			oowp.pb(temp/(double)cnt);
		}
		printf("Case #%d:\n",k+1);
		rep(i,n)
			printf("%.9lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}