#include<cstdio>
#include<cstring>
int main()
{
int nT,t,i,j,len,base;
bool used[128];
char str[61];
int map[128];
int now;
unsigned long long result;
scanf("%d",&nT);
for(t=1;t<=nT;++t)
	{
	memset(used,false,sizeof(used));
	base=0;
	scanf("%s",str);
	len=strlen(str);
	for(i=0;i<len;++i)
		if(!used[str[i]])
			{
			used[str[i]]=true;
			++base;
			}
	if(base<2)
		base=2;
	memset(map,-1,sizeof(map));
	now=0;
	map[str[0]]=1;
	result=1ULL;
	for(i=1;i<len;++i)
		{
		if(map[str[i]]==-1)
			{
			if(now==1)
				map[str[i]]=2,now=3;
			else
				map[str[i]]=now++;			
			}
		result=result*base+map[str[i]];
		}
	printf("Case #%d: %llu\n",t,result);
	}
}