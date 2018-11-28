#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int MAXM=1000+10;
int a[MAXM];
void solution(int num)
{
	int p,k,m;
	scanf("%d %d %d",&p,&k,&m);
	int i;
	vector<int> a(m);
	for(i=0;i<m;i++)
		scanf("%d",&a[i]);
	sort(a.begin(),a.end(),greater<int>());
	int j,e=0;
	long long res=0;
	for(i=0;i<p&&e<m;i++)
		for(j=0;j<k&&e<m;j++)
			res+=((long long)(i+1))*a[e++];
	printf("Case #%d: ",num+1);
	if(e<m) {printf("Impossible\n");return;}
	cout<<res<<endl;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d",&n);
	int i;
	for(i=0;i<n;i++)
		solution(i);
	return 0;
}
