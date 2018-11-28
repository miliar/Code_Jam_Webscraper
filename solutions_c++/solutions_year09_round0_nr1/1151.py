#include<iostream>
#include<string>
using namespace std;
string str[5010];
struct node 
{
	string sam[30];
	int cntt;
}stu[510];
int main()
{
	freopen("G:\\A-large.in","r",stdin);
	freopen("G:\\A-large.out","w",stdout);
	int Lx,D,N;	
	string temp;
	int cnt;
	int sta;
	int cas=1;
	while(scanf("%d%d%d",&Lx,&D,&N)!=EOF)
	{
		cas=1;
		for(int i=0;i<D;++i)
			cin>>str[i];
		for(int i=0;i<N;++i)
			for(int j=0;j<Lx;++j)
				stu[i].sam[j]="",stu[i].cntt=0;
		for(int i=0;i<N;++i)
		{
			cin>>temp;
			cnt=0;
			sta=0;
			for(int j=0;j<temp.size();++j)
			{
				if(sta==0&&temp[j]!='(')
				{
					stu[i].sam[cnt]+=temp[j];
					cnt++;
				}
				else if(sta==0&&temp[j]=='(')
					sta=1;
				else if(sta==1)
				{
					if(temp[j]==')')
					{
						sta=0;
						cnt++;
					}
					else
						stu[i].sam[cnt]+=temp[j];
				}
			}
			stu[i].cntt=cnt;
		}
		int ans=0,i,j,k,ii;
		for(k=0;k<N;++k)
		{
			ans=0;
			for(i=0;i<D;++i)
			{
				for(j=0;j<Lx;++j)
				{
					bool findf=0;
					for(ii=0;ii<stu[k].sam[j].size();++ii)
					{
						if(str[i][j]==stu[k].sam[j][ii])
						{
							findf=1;
							break;
						}
					}
					if(findf==0)
						break;
				}
				if(j>=Lx)
					ans++;
			}
		   printf("Case #%d: %d\n",cas++,ans);
		}
	}
	return 0;
}