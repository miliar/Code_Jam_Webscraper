/*
author:cydorniaknight@gmail.com
blog:http://hi.baidu.com/cydorniaknight
*/

#include<iostream>
using namespace std;

int t,n;
int l,h,op[10010];
int ans;

bool is_appropriate()
{
	int i;
	for(i=0;i<n;++i)
	{
		if((op[i]%ans)&&(ans%op[i])) return false;
	}
	return true;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("r1c_c.out","w",stdout);
	int ti,i,flag;
	scanf("%d",&t);
	for(ti=1;ti<=t;++ti)
	{
		scanf("%d%d%d",&n,&l,&h);
		for(i=0;i<n;++i)
			scanf("%d",&op[i]);
		flag=false;
		for(ans=l;ans<=h;++ans)
		{
			if(is_appropriate()){
				flag=true;
				break;
			}
		}
		if(flag) printf("Case #%d: %d\n",ti,ans);
		else printf("Case #%d: NO\n",ti);
	}
	//system("pause");
	return 0;
}