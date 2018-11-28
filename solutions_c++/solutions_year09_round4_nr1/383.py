#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)

int main(){
	char s[100];
	int T,N;

	scanf("%d",&T);	
	REP(TC,T){
		scanf("%d",&N);
		vector<int> arr;
		REP(i,N){
			scanf("%s",s);
			int len = strlen(s);
			while (len > 0 && s[len-1]=='0') len--;
			arr.push_back(len);
			//printf("%d\n",len);
		}
		int res = 0;
		REP(i,N){
			for (int j=i; j<N; j++){
				if (arr[j]<=i+1){
					for (int k=j; k>i; k--)
						swap(arr[k],arr[k-1]);
					break;
				} else {
					res++;
				}
			}
			assert(arr[i]<=i+1);
			//REP(j,N) printf("%d",arr[j]); printf("res = %d\n",res);
		}
		printf("Case #%d: %d\n",TC+1,res);
	}
}
