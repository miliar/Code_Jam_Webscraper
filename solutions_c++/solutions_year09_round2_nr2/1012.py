#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

typedef long long ll;
int cnt[10];
char a[100];
bool f;
int l;
vector<int> ans;
bool che(int k)
{
	if(k==0) return true;
	int t[20],i;
	for(i=0;i<10;i++) t[i]=cnt[i];
	for(i=0;i<k;i++)
	{
   if(t[a[i]-'0']<=0) return false;
   t[a[i]-'0']--;
	}
	return true;
}


void com()
{
	if(f) return ;
	int t[20];
	int i,j,k,p;
	for(p=0;p<10;p++) t[p]=cnt[p];
	for(i=l-1;i>=0;i--)
	{
		if(f) return ;
		for(j=0;j<10;j++) if(cnt[j]>0&&j>a[i]-'0')
		{
			cnt[j]--;
			if(che(i)) 
			{
				f=true;
				for(k=0;k<i;k++) 
				{
					ans.push_back(a[k]-'0');
					t[a[k]-'0']--;
				}
			    ans.push_back(j);
			    t[j]--;
				for(k=i+1;k<l;k++) 
				{
					for(p=0;p<10;p++)
						if(t[p]>0)
						{
							ans.push_back(p);
							t[p]--;
							break;
						}
				}
			}
			else cnt[j]++;
			if(f) return ;
		}
	}
}
					
 

int main()
{

	int t,i,j,p;
		int pv[20];
	freopen("B-large.in","r",stdin);
	freopen("bb.out","w",stdout);
	scanf("%d",&t);
	for(p=1;p<=t;p++)
	{
		scanf("%s",a);
		l=strlen(a);
		memset(cnt,0,sizeof(cnt));
        
		for(i=0;i<l;i++) 
		{
			cnt[a[i]-'0']++;
		}
		for(i=0;i<10;i++) pv[i]=cnt[i];
        f=false;
		com();
		printf("Case #%d: ",p);
			if(f) 
		for(i=0;i<ans.size();i++) printf("%d",ans[i]);
			else
			{
				for(i=1;i<10;i++)
					if(pv[i]>0) 
					{
						printf("%d0",i);
                        pv[i]--;
						break;
					}
					for(j=1;j<l;j++)
						for(i=0;i<10;i++)
							if(pv[i]>0)
							{
								printf("%d",i);
								pv[i]--;
								break;
							}
			}
		printf("\n");
		ans.resize(0);
	}
	return 0;
}

		

