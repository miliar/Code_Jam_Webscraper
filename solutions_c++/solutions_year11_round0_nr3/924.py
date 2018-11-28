#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

int t;
int n;
int a[3000];

void solve(int testcase){
	scanf("%d",&n);
	for (int i=0; i<n; i++)
		scanf("%d",&a[i]);
	sort(a,a+n);
	int x=0, sum=0;
	for (int i=0; i<n; i++)
		x^=a[i], sum+=a[i];

	printf("Case #%d: ",testcase);
	x==0?printf("%d\n",sum-a[0]):printf("NO\n");
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);

	for (int i=1; i<=t; i++)
		solve(i);	

	return 0;
}