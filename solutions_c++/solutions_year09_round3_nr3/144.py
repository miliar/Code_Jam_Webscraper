#include <vector>
#include <list>
#include <map>
#include <set>
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
using namespace std;



int c[111][111];


int main()
{

    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int C=1;
    while(T--){
        int L,n,a[1000];memset(a,0,sizeof(a));
	scanf("%d %d",&L,&n);
		for(int i=1;i<=n;i++)
			scanf("%d",&a[i]);
		a[++n]=L+1;
	
		memset(c,0,sizeof(c));
		for(int r=2;r<=n;r++){
			for(int i=0;i<n-r+1;i++){
				int j=i+r;
				for(int k=i+1;k<j;k++){
					int t=c[i][k]+c[k][j]+a[j]-a[i]-2;
					if(c[i][j]){
						c[i][j]=c[i][j] < t ? c[i][j]:t;
					}
					else c[i][j]=t;
		
				}
			//	printf("%d %d %d\n",i,j,c[i][j]);
			}
		}
        printf("Case #%d: %d\n",C,c[0][n]);
        C++;
    }

    return 0;
}










