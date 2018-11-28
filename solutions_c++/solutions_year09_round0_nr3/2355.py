#include <iostream>
#include <string>
using namespace std;
int findstart(int a,int vector[],int len)
{
	int low=1,high=len,mid,x=-1;
	while (low<=high)
	{
		mid = (low+high)/2;
		if (vector[mid]>a)
		{
			x = mid;
			high = mid-1;
		}
		else if (vector[mid]<=a)
			low = mid+1;
	}
	return x;
}
int maxlen;
int result;
int vector[21][600];
int temp[20];
char str[502];
char str1[20];
void dfs(int cx,int prev)
{
	temp[cx] = prev;
	if (cx==19) 
	{
		result++;
/*		for (int i=1;i<=19;i++)
			cout << temp[i] <<" ";
		cout << endl;*/
		return;
	}
	int i;
	int fx = findstart(prev,vector[cx],vector[cx][0]);
	if (fx==-1) return ;
	for (i=fx;i<vector[cx][0];i++)
	{
		dfs(cx+1,vector[cx][i]);
	}
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int n,p,j,i;
	char ss[20]="welcome to code jam";
	
	scanf("%d",&n);
	getchar();
	for (p=1;p<=n;p++)
	{
		gets(str);
		for (i=0;i<19;i++)
		{
			vector[i][0] = 1;
			maxlen = strlen(str);
			for (j=0;j<maxlen;j++)
			{
				if (str[j]==ss[i])
					vector[i][vector[i][0]++] = j;
			}
		}
		result = 0;
		dfs(0,-1);
		printf("Case #%d: %d%d%d%d\n",p,result/1000%10,result/100%10,result/10%10,result%10);
	}
	return 0;
}