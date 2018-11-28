#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <iostream>
int T,n,m;
char a[100][100];
using namespace std;
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n",&T); 
	for(int test=1;test<=T;test++){
		scanf("%d %d\n",&n,&m);
		for(int i=1;i<=n;i++){
			for(int j=1;j<=m;j++)
				scanf("%c",&a[i][j]);
			scanf("\n");
		}
		printf("Case #%d:\n",test);

		for(int i=1;i<n;i++){
			for(int j=1;j<m;j++)
				if(a[i][j]=='#'){
					if(a[i+1][j]!='#')   continue;//goto H;
					if(a[i][j+1]!='#')   continue;//goto H;
					if(a[i+1][j+1]!='#') continue;//goto H;
				
					a[i][j]='/'; 
					a[i+1][j]=92;
					a[i][j+1]=92;
					a[i+1][j+1]=47;
				}
		}
		for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
		if(a[i][j]=='#') goto H;
		
		for(int i=1;i<=n;i++){ 
			for(int j=1;j<=m;j++) printf("%c",a[i][j]);
			printf("\n");
		}
		
		continue;
		H:
		puts("Impossible");
	}
}
