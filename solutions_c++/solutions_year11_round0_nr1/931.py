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

int n;
int t;

void solve(int testcase){
	scanf("%d",&n);

	int cur1=1, cur2=1;
	int prev1=0, prev2=0;
	int res=0;
	for (int i=0; i<n; i++){
		string s;
		cin>>s;
		int x;
		scanf("%d",&x);

		if (s=="O"){
			int dst=abs(cur1-x);
			cur1=x;
			res+=max(dst-prev2,0)+1;
			prev1+=max(dst-prev2,0)+1;
			prev2=0;
		} else
		{
			int dst=abs(cur2-x);
			cur2=x;
			res+=max(dst-prev1,0)+1;
			prev2+=max(dst-prev1,0)+1;
			prev1=0;
		}
	}
	printf("Case #%d: %d\n",testcase,res);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);

	for (int i=1; i<=t; i++)
		solve(i);	

	return 0;
}