#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
using namespace std;

const int maxn = 1100000;
const double eps = 1e-7;

double pos[maxn];
int N,C,D;

bool check(double cost ){
	int i,j,k;
	double pre ,cur;
	for(i=0;i<N;i++){

		if( i == 0 ){
			//first node ,go left;
			cur = pos[i] - cost ;
		}else {
			
			if(  pre + D <= pos[i]  ){
				//walk left;
				cur = pos[i] - cost ;
				if( pre + D > cur ){
					//can't walk through
					cur = pre + D;
				}
			}else {
				//walk right;
				cur = pre + D;
				//can't reach 
				if( pos[i] + cost < cur )return false;
			}

		
		}

		pre = cur ;
	}

	return true;
}

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int i,j,k;

	
	string str;
	int nca;

	cin>>nca;
	for(int cid=1;cid<=nca;cid++){
		cin>>C>>D;
		
		int v;
		double p;
		N=0;

		for(i=0;i<C;i++){
			cin>>p>>v;
			for(j=0;j<v;j++)
			{
				pos[N++]=p;
			}
		}

		double ret = 0,l=0.0, r = 1e13 ;

		while( fabs(l-r)>eps )
		{
			ret = ( l + r ) / 2 ;
			if( check(ret) ) r = ret ;
			else l=ret ;
		}
		

		printf("Case #%d: %.12lf\n",cid,ret);
		
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