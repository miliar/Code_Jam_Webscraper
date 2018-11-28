#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<string>
#include<vector>
#include<queue>

using namespace std;

#define SZ 50
#define min(a , b) (a < b ? a : b)
#define max(a , b) (a > b ? a : b)

typedef __int64 II;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<II> vii;

int arr[SZ][2] , tmp[SZ] , mm;

int dfs(int root){
	if(root >= mm)
		return tmp[root];
	int a = dfs(2*root+1);
	int b = dfs(2*root+2);
	if(tmp[root]) return (a&b);
	return (a|b);
}

int main(){
	freopen("a.in" , "r" , stdin);
	freopen("a.out" , "w" , stdout);
	int test , m  , v , n , i , kase = 1;
	scanf("%d" , &test);
	while(test--){
		scanf("%d%d" , &m , &v);
		vi aa;
		for(i = 0;i<(m-1)/2;i++){
			scanf("%d%d" , &arr[i][0] , &arr[i][1]);
			if(arr[i][1]) aa.push_back(i);
		}
		for( ;i<m;i++){
			scanf("%d" , &arr[i][0]);
			arr[i][1] = -1;
		}
		mm = (m-1)/2;
		int ret = (1<<10);
		n = aa.size();
		int j;
		for(i = 0;i<(1<<n);i++){
			for(j = 0;j<m;j++)
				tmp[j] = arr[j][0];
			for(j = 0;j<n;j++)
				if(i&(1<<j))
					tmp[aa[j]] = tmp[aa[j]]^1;
			int rt = dfs(0);
			if(rt == v){
				j = 0;
				int tt = i;
				while(tt > 0){
					tt = tt&(tt-1);
					j++;
				}
				if(j < ret)
					ret = j;
			}
		}
		if(ret == (1<<10)) printf("Case #%d: IMPOSSIBLE\n" , kase++);
		else printf("Case #%d: %d\n" ,kase++ , ret);
	}
	return 0;
}
