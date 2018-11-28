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
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string>VS;
int a[5];
char b[1001];
char str[1001];
int main(){
	int i,j,ii,n,k,s,sum,ans;
 	freopen("D-small-attempt0.in","r",stdin);
 	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&n);
	for(ii=1;ii<=n;ii++){
		printf("Case #%d: ",ii);
		scanf("%d",&k);
		for(i=0;i<k;i++)a[i]=i;
		scanf(" %s",str);
		s=strlen(str);
		ans=0x7fffffff;
		do{
			for(i=0;i<s;i+=k){
				for(j=i;j<i+k;j++){
					b[j]=str[i+a[j-i]];
				}
			}
			sum=1;
			for(i=1;i<s;i++){
				if(b[i]!=b[i-1])sum++;
			}
			if(ans>sum)ans=sum;
		}
		while(next_permutation(a,a+k));
		printf("%d\n",ans);
	}
	return 0;
}