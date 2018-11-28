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

#define eps 1e-8
#define PI 3.14159265358979323846
#define push_back(a) pb(a)
typedef long long ll;

bool b[12][12];
int a[12][1<<10];
int m,n;
int best;


int main(){
	int T,TT;
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		printf("Case #%d: ",TT);
		scanf("%d%d",&m,&n);
		char ch[20];
		memset(a,0,sizeof(a));
		int i,j,l,k;
		for(i=0;i<m;i++){
			scanf("%s",ch);
			for(j=0;j<n;j++){
				if(ch[j]=='.')
					b[i][j]=1;
				else
					b[i][j]=0;
			}
		}
		for(i=0;i<(1<<n);i++){
			int cnt=0;
			for(j=0;j<n;j++){
				if((i&(1<<j))!=0){
					if(!b[m-1][j])
						break;
					if(j<n-1){
						if((i&(1<<(j+1)))!=0){
							break;
						}
					}
					cnt++;
				}
			}
			if(j==n){
				a[m-1][i]=cnt;
			}
		}
		for(l=m-2;l>=0;l--){
			for(i=0;i<(1<<n);i++){
				int cnt=0;
				for(j=0;j<n;j++){
					if((i&(1<<j))!=0){
						cnt++;
						if(!b[l][j])
							break;
						if(j<n-1){
							if((i&(1<<(j+1)))!=0){
								break;
							}
						}
					}
				}
				if(j!=n)
					continue;
				for(j=0;j<(1<<n);j++){
					if(cnt+a[l+1][j]<=a[l][i])
						continue;
					for(k=0;k<n;k++){
						if((i&(1<<k))!=0){
							if(k>=1){
								if((j&(1<<(k-1)))!=0)
									break;
							}
							if(k<n-1){
								if((j&(1<<(k+1)))!=0)
									break;
							}
						}
					}
					if(k==n){
						a[l][i]=cnt+a[l+1][j];
					}
				}
			}
		}
		best=0;
		for(i=0;i<(1<<n);i++){
			if(a[0][i]>best)
				best=a[0][i];
		}
		printf("%d\n",best);

	}
}