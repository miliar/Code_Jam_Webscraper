#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
string a[50];
int main(){
	int t_case,t,n,i,j,j0,k,r;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t_case);
	for (t = 1;t <= t_case;t++){
		scanf("%d",&n);
		for(i = 0;i < n;i++)
			cin >> a[i];
		r = 0;
		for (i = 0;i < n;i++){
			for (j = i;j < n;j++){
				for (k = n-1;k >= 0;k--)
					if (a[j][k] > '0')
						break;
				if (k <= i) break;
			}
			for (j0 = j;j0 > i;j0--){
				swap(a[j0],a[j0-1]);
				r++;
			}
		}
		printf("Case #%d: %d\n",t,r);
	}
	fclose(stdout);
}
