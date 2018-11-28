#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <cassert>
#include <map>
#include <stack>

#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define REP(I,N) FOR(I,0,N)
#define ALL(A) (A).begin(),(A).end()

#define SQR(x) ((x)*(x))
#define PB(x) push_back(x)

#define PI (acos(-1.0))

using namespace std;

typedef vector<int> VI;
typedef vector< vector<int> > VVI;


int main(){
	freopen("in.txt","rt",stdin);
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int t;
	cin>>t;
	int k = 1;
	while(t-->0){
		int n,i,j,l;
		double wp[100]={0};
		double owp[100]={0};
		double oowp[100]={0};
		int played[100]={0};
		char adjmat[100][100]={0};
		cin>>n;
		REP(i,n) REP(j,n){
			cin>>adjmat[i][j];
			if( adjmat[i][j] != '.') played[i]++;
		}
		//wp구하기
		REP(i,n){
			int win = 0;
			REP(j,n)
				if(adjmat[i][j] == '1') win++;
			wp[i] = (double)win/played[i];
		}
		//owp구하기
		REP(i,n){
			REP(j,n){
				if(i == j) continue;	//같은것을 선택한거
				if(adjmat[i][j] =='.') continue;
				int sum = 0;
				REP(l,n){
					if( adjmat[j][l] == '.') continue;
					if( i == l) continue;
					sum += adjmat[j][l] -'0';
				}
				owp[i] += (double)sum/(played[j]-1);
			}
			owp[i] /= played[i];
		}
		REP(i,n){
			double sum = 0.0;
			REP(j,n){
				if( adjmat[i][j] == '.')continue;
				sum += owp[j];
			}
			oowp[i] = sum/played[i];
		}
		printf("Case #%d:\n",k++);
		REP(i,n){
			printf("%.12f\n",wp[i]*0.25 + owp[i]*0.5 + oowp[i]*0.25);
			//cout<<"as"<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<" "<<endl;
		}
	}
	return 0;
}

