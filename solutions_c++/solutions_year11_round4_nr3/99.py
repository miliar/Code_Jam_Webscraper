#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

long long n;

int pr[2000000];
vector <long long> prm; 

long long find(long long n){
	long long res=0;
	for (int i=0; i<prm.size(); i++){
		long long cur=prm[i];
		if (cur*cur>n) break;

		long long mul=cur*cur;
		while (mul<=n){
			res++;
			mul*=cur;
		}
	}
	return res;
}

void solve(int tst){
	cin>>n;

	printf("Case #%d: ",tst);
	if (n==1LL) cout<<find(n)<<endl; else
		cout<<find(n)+1LL<<endl;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);

	memset(pr,0,sizeof(pr));
	for (int i=2;i<2000000;i++){
		if (!pr[i]){
			int cur=2*i;
			while (cur<2000000){
				pr[cur]=1;
				cur+=i;
			}
		}
	}

	for (int i=2; i<2000000; i++)
		if (!pr[i]) prm.push_back(i);

	for (int tt=1; tt<=tests; tt++){
		solve(tt);
	}

	return 0;
}