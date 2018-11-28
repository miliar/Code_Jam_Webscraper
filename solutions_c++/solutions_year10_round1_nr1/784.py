#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

int main()
{

int t;
scanf("%d",&t);

for(int count=0;count<t;count++)
{
int n,kn;
char a[51][51];
char jnk;
scanf("%d %d",&n,&kn);

scanf("%c",&jnk);
	for(int i=0;i<n;i++)
	{
	for(int j=0;j<n;j++)
	{
	scanf("%c",&a[i][j]);
	}
	scanf("%c",&jnk);
	}



// simulate gravity effect

for(int i=0;i<n;i++)
for(int  j=n-1;j>=0;j--)
{
	if(a[i][j]!='.')
	{
	for(int k=j+1; k<n; k++)
	{
		if(a[i][k]!='.') break;
		a[i][k]=a[i][k-1];
		a[i][k-1]='.';
	}
	}
}


int num=0;
char turn;
int resA=0,resB=0;
for(int i=0;i<n;i++)
for(int j=0;j<n;j++)
{
if(a[i][j]=='R') turn='R'; else if(a[i][j]=='B') turn='B'; else continue;
	int num=0;	
	int k;

	
	for(k=j;k<n;k++)
	if(a[i][k]!=turn) break; 

	num=max(num,k-j);

for(k=i;k<n;k++)
	if(a[k][j]!=turn) break; 

	num=max(num,k-i);

	for(k=0;;k++)
	{
	if(!(i+k <n && j+k<n)) break;
	if(a[i+k][j+k]!=turn) break; 
	}

	num=max(num,k);

	for(k=0;;k++)
	{
	if(!(i+k <n && j-k<n)) break;
	if(a[i+k][j-k]!=turn) break; 
	}

	num=max(num,k);

if(num>=kn) if(turn=='R') resA=1; else resB=1;

}

if(resA+resB==0)
printf("Case #%d: Neither\n",count+1);
else if(resA+resB==2)
printf("Case #%d: Both\n",count+1);
else if(resA==1)
printf("Case #%d: Red\n",count+1);
else 
printf("Case #%d: Blue\n",count+1);





}

return 0;
}
