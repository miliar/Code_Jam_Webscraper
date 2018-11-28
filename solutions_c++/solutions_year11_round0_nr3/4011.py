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
int data[15];
int add(int lh,int rh){
	//십진수로 바꾼것을 출력
	int p[32]={0},q[32]={0};
	int cnt = 0;
	do{
		p[cnt++] = lh % 2;
		lh /= 2;
	}while(lh != 0);
	cnt = 0;
	do{
		q[cnt++] = rh % 2;
		rh /= 2;
	}while(rh != 0);
	int ret[32]={0};
	int ans = 0;
	for(int i = 31;i >= 0; i--){
		ret[i] = p[i]^q[i];
		ans = ans*2 + ret[i];
	}
	return ans;
}

int main(){
	freopen("C-small-attempt1.in","rt",stdin);
	freopen("C-small-attempt1.out","wt",stdout);
	int t,k;
	cin>>t;
	k = 1;
	
	while(t-->0){
		int n;
		cin>>n;
		for(int i = 0 ; i < n;i++)
			scanf("%d",data + i);
		int maxi = -987654321;
		for(int i = 0 ;i < pow(2.0,n);i++){
			//나누어 줄게 0이면 안됨
			int lsum,rsum,cnt=0;
			lsum = rsum = 0;
			int temp = i;
			int ans = 0;
			do{
				if(temp & 1){lsum = add(lsum,data[cnt]); ans+=data[cnt];}
				else	rsum = add(rsum,data[cnt]);
				cnt++;
				temp >>= 1;
			}while(cnt < n);
			if( lsum == rsum && lsum != 0){
				maxi = max(maxi,ans);
			}	
		}
		printf("Case #%d: ",k++);
		if(maxi == -987654321)	cout<<"NO"<<endl;
		else cout<<maxi<<endl;
	}
	return 0;
}


