#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
struct node
{
	int flag;
	char a[105];
};
node map[205];
int cmp (node a,node b)
{
	return strcmp(a.a,b.a)<0;
}
int main ()
{
	freopen("a3l.txt","r",stdin);
	freopen("ans3l.txt","w",stdout);
	int T;
	int i,aaa,n,m,t,j,k1,ans,ans1,ans2,k,mm,mmm;
	int sum;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		aaa=0;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			scanf("%s",map[i].a);
			map[i].flag=1;
			//	cout<<map[i].flag<<endl;
		}
			for(i=0;i<m;i++)
			{
				scanf("%s",map[n+i].a);
				map[n+i].flag=0;
			//	cout<<i+n<<endl;
			}
		sort(map,map+n+m,cmp);
		for(i=0;i<n+m;i++)
		{
			if(map[i].flag==1)continue;
			mm=strlen(map[i].a);
			sum=0;
			for(k=0;k<mm;k++)
			{
				if(map[i].a[k]=='/')sum++;
			}
			j=i-1;
			while(j>=0&&map[j].flag==0)j--;
			ans1=0;
			if(j>=0)
			{
				mmm=strlen(map[j].a);
				for(k1=0;k1<mm;k1++)
				{
					if(map[j].a[k1]!=map[i].a[k1])break;
					if(map[j].a[k1]=='/')ans1++;
				}
				if((map[i].a[k1]=='\0'&&(map[j].a[k1]=='/'||map[j].a[k1]=='\0'))||(map[j].a[k1]=='\0'&&(map[i].a[k1]=='/'||map[i].a[k1]=='\0')));
				else ans1--;
			}
			j=i+1;
			while(j<n+m&&map[j].flag==0)j++;
			ans2=0;
			if(j<n+m)
			{
				mmm=strlen(map[j].a);
				for(k1=0;k1<mm;k1++)
				{
					if(map[j].a[k1]!=map[i].a[k1])break;
					if(map[j].a[k1]=='/')ans2++;
				}
				if((map[i].a[k1]=='\0'&&(map[j].a[k1]=='/'||map[j].a[k1]=='\0'))||(map[j].a[k1]=='\0'&&(map[i].a[k1]=='/'||map[i].a[k1]=='\0')));
				else ans2--;
			}
			ans=ans1>ans2?ans1:ans2;
			aaa+=sum-ans;
			map[i].flag=1;
		}
		printf("Case #%d: %d\n",t,aaa);
	}
}