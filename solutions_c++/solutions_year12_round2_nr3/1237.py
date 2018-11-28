#include <stdio.h>
#include <string.h>

#include <vector>

using namespace std;

bool done = false;
int arr[22], n;
vector<int> ra, rb;

void BT(vector<int> &A, vector<int> &B, int sumA, int sumB, int i)
{
	if(sumA == sumB && sumA && (!done || rb.size() > B.size()))
	{
		ra = A; rb = B;
		done = true;
	}
	if(i < n && !done)
	{
		A.push_back(arr[i]);
		BT(A,B,sumA + arr[i],sumB,i + 1);
		A.pop_back();
		B.push_back(arr[i]);
		BT(A,B,sumA,sumB + arr[i],i + 1);
		B.pop_back();
		BT(A,B,sumA,sumB,i + 1);
	}
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("c.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; ++i)
	{
		scanf("%d",&n);
		done = false;
		for(int j = 0; j < n; ++j)
			scanf("%d",&arr[j]);
		vector<int> A,B;
		ra = vector<int>(); rb = vector<int>();
		printf("Case #%d:\n",i);
		BT(A,B,0,0,0);
		if(ra.size() || rb.size()){
		int sa = ra.size(), sb = rb.size();
		for(int j = 0; j < sa - 1; ++j)
			printf("%d ",ra[j]);
		printf("%d\n",ra[sa - 1]);
		for(int j = 0; j < sb - 1; ++j)
			printf("%d ",rb[j]);
		printf("%d\n",rb[sb - 1]);}
		else printf("Impossible\n");
	}
	return 0;
}
		
