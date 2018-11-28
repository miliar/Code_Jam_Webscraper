#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <math.h>

using namespace std;

map<int,int> mp;

int good(int a,int b){
	if (a==b) return 0;
	if (a<b) swap(a,b);
	int bord=ceil(2.0*a/(sqrt(5.0)+1));
	int l=bord, r=bord+a-1;
	if (b<l||b>r) return 1;
	return 0;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);

	for (int tt=1; tt<=t; tt++){
		mp.clear();
		int a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		long long res=0;
		for (int i=a1; i<=a2; i++){
			int l=ceil(2.0*i/(sqrt(5.0)+1));
			int r=l+i-1;

			int a[5];
			a[1]=b1, a[2]=b2, a[3]=l, a[4]=r;
			sort(a+1,a+5);
			int c[5];
			int v=0;
			for (int i=1; i<=4; i++)
				if (a[i]>=b1&&a[i]<=b2&&a[i]>=l&&a[i]<=r) 
					v++, c[v]=a[i];
			int pr=0;
			if (v!=0) pr=c[v]-c[1]+1;
			res+=(long long)(b2-b1+1-pr);
		}

		printf("Case #%d: ",tt);
		cout<<res<<endl;
	}

	return 0;
}