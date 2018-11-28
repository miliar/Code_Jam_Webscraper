#include <stdio.h>
#include <algorithm>

using namespace std;

int n;
FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");
int a[1002];
int sum;

void input()
{
	int i;

	sum=0;
	fscanf(in,"%d ",&n);
	for(i=1 ; i<=n ; i++)
	{
		fscanf(in,"%d ",&a[i]);
		sum+=a[i];
	}
	sort(a+1,a+1+n);
}
void process()
{
	int i;
	int k=0;

	for(i=1 ; i<=n ; i++)
		k=k^a[i];

	if(k==0)
		fprintf(out,"%d\n",sum-a[1]);
	else
		fprintf(out,"NO\n");
}
int main()
{
	int i,t;

	fscanf(in,"%d ",&t);

	for(i=1 ; i<=t ; i++)
	{
		input();
		fprintf(out,"Case #%d: ",i);
		process();
	}
	return 0;
}