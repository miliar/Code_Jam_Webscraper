//{{{
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <valarray> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <memory> 
#include <new> 
#include <iterator> 
#include <limits> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
#include <cctype> 
using namespace std;
//}}}

int cnt[3][3];
int main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		int n;
		long long A,B,C,D,X,Y,M;
		cin>>n>>A>>B>>C>>D>>X>>Y>>M;
		memset(cnt,0,sizeof(cnt));
		for(int i=0;i<n;i++){
			cnt[X%3][Y%3]++;
			X=(A*X+B)%M;
			Y=(C*Y+D)%M;
		}
		long long ret=0;
		for(int i=0;i<9;i++)if(cnt[i/3][i%3]){
			long long I=cnt[i/3][i%3]--;
			for(int j=0;j<9;j++)if(cnt[j/3][j%3]){
				long long J=cnt[j/3][j%3]--;
				for(int k=0;k<9;k++)if(cnt[k/3][k%3]){
					long long K=cnt[k/3][k%3];
					if((i/3+j/3+k/3)%3==0&&(i%3+j%3+k%3)%3==0)
						ret+=I*J*K;
				}
				cnt[j/3][j%3]++;
			}
			cnt[i/3][i%3]++;
		}
		printf("Case #%d: ",t);
		cout<<ret/6<<endl;
	}
	
scanf("%*s");
	return 0;
}
