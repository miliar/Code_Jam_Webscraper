#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
using namespace std;

const int maxn = 1100;
const int maxm = 1000100;
int c[maxn];
int f[2][maxm];

int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1_b.out","w",stdout);
	int i,j,k;

	int n;
	string str;
	int nca;

	cin>>nca;
	for(int cid=1;cid<=nca;cid++){
		cin>>n;
		
		int cur = 0;

		memset(f,-1,sizeof(f));
		f[cur][0]=0;

		int totm = 0;
		int totr = 0;
		for(i=0;i<n;i++){
			cin>>c[i];
			totr += c[i];
			totm = totm ^ c[i];
		}
		
		/*
			int max_m = 0;
			
			for(i=0;i<n;i++){
				int pre = cur ;
				cur = 1-cur ;
				int tmp_m = max_m ;
				if( f[pre][0] == -1 ) f[pre][0] = 0;
				for(j=0;j<=max_m;j++)if(f[pre][j]!=-1){
					int t = j ^ c[i];
					if( t > tmp_m ) tmp_m = t;
					//if( t > totm ) continue ;
					if( (f[cur][t] < f[pre][j] + c[i] ) ) {
						f[cur][t] = f[pre][j] + c[i];
					}
				}

				max_m = tmp_m;

			}
			
			int ret = -1;
			for(i=0;i<=max_m;i++){
				if( (i^totm) == i && f[cur][i]!=-1 && f[cur][i] != totr )
				{
					ret = f[cur][i] > ret ? f[cur][i] : ret ;

				}
			}

		
		*/

		int ret = -1;
		int m = 1<<n ;
		for(i=1;i<m-1;i++){
			k=i;
			int c1=0,c2=0,w1=0,w2=0;
			for(j=0;j<n;j++){
				if(k%2){ c1^=c[j]; w1 += c[j]; }
				else { c2^=c[j];w2 += c[j] ;}
				k/=2;
			}

			if( c1 == c2 ){
				ret = max(ret,max(w1,w2));
			}
		}

		printf("Case #%d: ",cid);
		if( ret == -1 )cout<<"NO"<<endl;
		else cout<<ret<<endl;
	}
}