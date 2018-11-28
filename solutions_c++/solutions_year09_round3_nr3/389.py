#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;
#define MAXN 100
int aa[10];
int N;
int ans;
void dummy(int* a,int n){
	int num[105];
	memset (num, 0, sizeof (num));
	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		//cout << aa[a[i]] << " ";
		num[aa[a[i]]] = 1;
		for (int j = aa[a[i]] + 1; j <= N; j++)
		{
			if (num[j] == 0)sum++;
			else break;
		}
		for (int j = aa[a[i]] - 1; j >= 1; j--)
		{
			if (num[j] == 0)sum++;
			else break;
		}
	}
	//cout << endl;
	//cout << sum << endl;
	if (ans > sum)ans = sum;
}
void _gen_perm(int* a,int n,int m,int l,int* temp,int* tag){
	int i;
	if (l==m)
		dummy(temp,m);
	else
		for (i=0;i<n;i++)
			if (!tag[i]){
				temp[l]=a[i],tag[i]=1;
				_gen_perm(a,n,m,l+1,temp,tag);
				tag[i]=0;
			}
}

void gen_perm(int n,int m){
	int a[MAXN],temp[MAXN],tag[MAXN]={0},i;
	for (i=0;i<n;i++)
		a[i]=i+1;
	_gen_perm(a,n,m,0,temp,tag);
}
int main ()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ca = 1;
	int t;
	cin >> t;
	while (t--)
	{
		ans = 999999999;
		int m;
		cin >> N >> m;
		for (int i = 1; i <= m; i++)
			cin >> aa[i];
		gen_perm(m, m);
		printf ("Case #%d: %d\n", ca++, ans);
	}
}