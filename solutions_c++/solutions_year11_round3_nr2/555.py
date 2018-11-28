#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
using namespace std;

const int maxn = 1100000;

typedef __int64 ll;

ll d[maxn],a[maxn],td[maxn];

struct node {
	int save;
	int id;
	bool operator<(const node &b)const {
		return ( save > b.save );
	}
}sd[maxn];

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int i,j,k;

	
	string str;
	int nca;
	int N,C,L;
	ll t;

	cin>>nca;
	for(int cid=1;cid<=nca;cid++){
		
		
		cin>>L;
		scanf("%I64d",&t);
		cin>>N>>C;

		ll ret = 0 , tot = 0;
		d[0]=0;
		for(i=0;i<C;i++){
			scanf("%I64d",&a[i]);
			for(k=0;k*C+i<N;k++)d[ k*C+i + 1 ] = a[i];
			
		}

		

		for(i=1;i<=N;i++){
			tot += d[i]*2;
			td[i] = td[i-1] + d[i]*2 ;
		}

		ret = tot ;

		if( L == 2 ){
			for(i=1;i<N;i++){
				for(j=i+1;j<=N;j++){

					if( i == 4 && j == 6 ){
						k = 1;
					}
					ll tmp = tot;
					if( td[i-1] >= t ){
						//has build
						tmp = tot - d[i] ;
					}
					else if( td[i] > t ){
						//could build in middle 
						tmp = tot - ( d[i] -  (t-td[i-1])/2 ) ;
					}

					if( td[j-1] >= t ){
						//has build
						tmp = tmp - d[j] ;
					}
					else if( td[j] > t ){
						//could build in middle 
						tmp = tmp - ( d[j] -  (t-td[j-1])/2 ) ;
					}

					ret = min( ret , tmp );
				}
			}
		
		}else if( L == 1 ) {
			for(i=1;i<=N;i++){
				if( td[i-1] >= t ){
					//has build
					ret = min( ret , tot - d[i] );
				}
				else if( td[i] > t ){
					//could build in middle 
					ret = min( ret , tot - ( d[i] -  (t-td[i-1])/2 ) );
				}
			}
		}else {
			ret = tot ;
		}

		

		

		/*
		for(i=0;i<N;i++){
			if( ret >= t ){
				break;
			}
			ret += d[i] * 2 ;
			
		}
		
		if( i < N ){
			sort(d+i,d+N);
			for(j=N-1,k=0;j>=i;j--,k++)
			{
				if( k<L ) ret += d[j];
				else ret += d[j]*2;
			}
		}

		*/

		printf("Case #%d: %I64d\n",cid,ret);
		
		
	}

		
}

/*
4
4
.11.
0.00
01.1
.10.


*/