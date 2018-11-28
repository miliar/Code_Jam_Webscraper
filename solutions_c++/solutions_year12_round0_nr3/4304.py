#include<stdio.h>
#include<string.h>
char tmp[5000],tmp2[5000],tmp3[5000];
bool check(int in,int im)
{
	sprintf(tmp,"%d%d",in,in);
	sprintf(tmp2,"%d",im);
	if(strlen(tmp)!=strlen(tmp2)*2)
		return false;
	int d=strstr(tmp,tmp2)-tmp;
	if(d<strlen(tmp)/2)
	{
		//printf("YES! %d,%d\n",in,im);
		return true;
	}
	return false;
}
void docase()
{
	int in,im,cnt;
	cnt=0;
	scanf("%d %d",&in,&im);
	for(int n=in;n<=im;n++)
		for(int m=n+1;m<=im;m++)
		{
			if(check(n,m))
				cnt++;
		}
	printf("%d\n",cnt);
}
int main()
{
	int in;
	scanf("%d",&in);
	for(int n=0;n<in;n++)
	{
		printf("Case #%d: ",n+1);
		docase();
	}
}
