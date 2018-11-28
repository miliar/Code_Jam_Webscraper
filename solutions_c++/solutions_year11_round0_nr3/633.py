#include <iostream>
#include <algorithm>
using namespace std;
const int S_Size = 2097152;
int f[S_Size+1],f1[S_Size+1];
int a[1002];
int s ,n;
void readin()
{
	int i;
	scanf("%d",&n);
	s = 0;
	for(i = 0;i<n;++i)
	{
		scanf("%d",&a[i]);
		s^=a[i];
	}
}
void work(int CaseNum)
{
	int i,j;
	if( s!=0 || n == 1)
	{
		printf("Case #%d: NO\n",CaseNum);
		return;
	}
	int res = 0;
	sort(a,a+n);
	for(i = n-1;i>=1;--i)res+=a[i];
	printf("Case #%d: %d\n",CaseNum,res);	
}
int main()
{
	int tcase;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&tcase);
	int i;
	for(i = 1;i<=tcase;++i)
	{
		readin();
		work(i);
	}
	//fclose(stdin);

}