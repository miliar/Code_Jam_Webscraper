#include<iostream>
using namespace std;
char dic[11000][20]={};
char maybe[20][30];
int cnt[20];
int main()
{
	freopen("out.txt","w",stdout);
	int l,d,n;
	char act[1000];
	cin>>l>>d>>n;
	for (int i=0;i<d;i++)
		cin>>dic[i];
	cin.getline(act,1000);
	for(int i=1;i<=n;i++)
	{
		cin.getline(act,1000);
		int len=strlen(act);
		memset(maybe,0,sizeof(maybe));
		memset(cnt,0,sizeof(cnt));
		int ind=0;
		int flag=0;
		for (int j=0;j<len;j++)
		{
			if (act[j]=='(')
			{
				flag=1;
				continue;
			}
			if (act[j]==')')
			{
				flag=0;
				ind++;
				continue;
			}
			maybe[ind][cnt[ind]++]=act[j];
			if (flag==0)
				ind++;
		}
		int ans=0;
		for (int k=0;k<d;k++)
		{
			int flag=1;
			for (int j=0;j<l;j++)
			{
				int ok=0;
				for (int a=0;a<cnt[j];a++)
					if (dic[k][j]==maybe[j][a])
					{
						ok=1;
						break;
					}
				if (ok==0)
				{
					flag=0;
					break;
				}
			}
			if (flag)
				ans++;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}

}