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
int n,sz,g,h,m,i,j,c,T,pos1,pos2,i1,i2;
vector<int> a;
vector< vector<int> > k;
vector<bool> hod;

int main(){
	freopen("input.in","r",stdin);
	freopen("input.out","w",stdout);
	char ch;
	scanf("%d",&T);
	bool b=true;
	for(int t=0;t<T;t++){
		scanf("%d",&n);
		a.resize(n);
		c=0;
		for(i=0;i<n;i++){
			scanf("%d",&a[i]);
			c+=a[i];
		}
		sort(a.begin(),a.end());
		b=true;
		for(i=0;i<n && b;i++){
			g=0;
			for(j=0;j<n && b;j++)
				if(i^j)
					g^=a[j];
			if(g==a[i]){
				printf("Case #%d: %d\n",t+1,c-a[i]);
				b=false;
				break;
			}
		}
		if(b)printf("Case #%d: NO\n",t+1);
		
	}
	
return 0;
}

//Powered by [KawigiEdit] 2.0!