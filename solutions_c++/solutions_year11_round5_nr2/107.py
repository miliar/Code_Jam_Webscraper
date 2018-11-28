#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <queue>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <set>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


int num[20005],tmp[20005],keyi[20005];

int main(){
	freopen("B-large(1).in","r",stdin);
	freopen("B-large(1).out","w",stdout);

	int cas,Te=1;
	cin>>cas;
	while( cas-- ){
		int n; cin>>n;
		memset(num,0,sizeof(num));
		for(int i=1;i<=n;i++){
			int val; cin>>val;
			num[val]++;
		}
		printf("Case #%d: ",Te++);
		if( n==0 ){
			puts("0"); continue;
		}
		int ans=1;
		for(int i=2;i<=n;i++){
			memcpy(tmp,num,sizeof(num));
			memset(keyi,0,sizeof(keyi));

			bool suc=true;
			int ke=0;
			for(int j=1;j<=10000 && suc;ke+=keyi[j++]){
				if( tmp[j]==0 ){
					ke=0;
					continue;
				}

				if( tmp[j]<=ke ){
					ke=min(ke,tmp[j]); 
					continue;
				}

				int val=tmp[j]-ke, k;
				for(k=0;k<i;k++){
					if( tmp[j+k]>=val ){
						tmp[j+k]-=val;
					}else{
						suc=false;
					}
				}
				keyi[j+k-1]+=val;

			}
			if( suc ) ans=i;
		}
		printf("%d\n",ans);
	}
}