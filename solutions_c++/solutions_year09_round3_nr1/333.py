#include <iostream>


using namespace std;


char pro[100];
bool num[10],zimu[30],shu[100];
int num_j[10],zimu_j[30],ans[100];

int main()
{
	int t,i,j,ooo=1;
	freopen("h://A-large.in","r",stdin);
	freopen("h://ans.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		long long  sun=0;
		memset(num,false,sizeof(num));
		memset(zimu,false,sizeof(zimu));
		memset(num_j,-1,sizeof(num_j));
		memset(zimu_j,-1,sizeof(zimu_j));
		memset(shu,false,sizeof(shu));
		int sum=0;
		scanf("%s",&pro);
		for(i=0;i<strlen(pro);i++)
		{
			if(pro[i]<='9'&&pro[i]>='0')
			{
				int cnt=pro[i]-'0';
				if(!num[cnt])
				{
					sum++;
					num[cnt]=true;
				}
			}
			else
			{
				int cnt=pro[i]-'a';
				if(!zimu[cnt])
				{
					sum++;
					zimu[cnt]=true;
				}
			}
		}
		ans[0]=1;
		shu[1]=true;
		if(pro[0]<='9'&&pro[0]>='0')
		{
			num_j[pro[0]-'0']=1;
		}
		else
		{
			zimu_j[pro[0]-'a']=1;
		}
		int o=0;
		for(i=1;i<strlen(pro);i++)
		{
			if(pro[i]<='9'&&pro[i]>='0')
			{
				int cnt=pro[i]-'0';
				if(num_j[cnt]!=-1)
				{
					ans[i]=num_j[cnt];
				}
				else
				{
					while(shu[o])
						o++;
					num_j[cnt]=o;
					ans[i]=o;
					shu[o]=true;
				}
			}
			else
			{
				int cnt=pro[i]-'a';
				if(zimu_j[cnt]!=-1)
				{
					ans[i]=zimu_j[cnt];
				}
				else
				{
					while(shu[o])
						o++;
					zimu_j[cnt]=o;
					ans[i]=o;
					shu[o]=true;
				}
			}
		}
		if(sum==1)
			sum=2;
		long long it=1;
		printf("Case #%d: ",ooo++);
		for(i=strlen(pro)-1;i>=0;--i)
		{
			sun+=it*ans[i];
			it*=sum;
		}
		printf("%lld\n",sun);
	}
}
