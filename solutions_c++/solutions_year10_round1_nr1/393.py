#include<stdio.h>
char temp[55][55],_node[55][55];
int n,k;
bool check(int i,int j,char ch)
{
	int ii=i,jj=j,cnt;
	cnt=0;
	while(cnt<k)
	{
		if(ii>=0&&ii<n&&jj>=0&&jj<n&&_node[ii][jj]==ch)
			cnt++;
		else
			break;
		jj++;
	}
	if(cnt==k)
		return true;
	ii=i;jj=j;cnt=0;
	while(cnt<k)
	{
		if(ii>=0&&ii<n&&jj>=0&&jj<n&&_node[ii][jj]==ch)
			cnt++;
		else
			break;
		ii++;
	}
	if(cnt==k)
		return true;
	ii=i;jj=j;cnt=0;
	while(cnt<k)
	{
		if(ii>=0&&ii<n&&jj>=0&&jj<n&&_node[ii][jj]==ch)
			cnt++;
		else
			break;
		ii++;jj++;
	}
	if(cnt==k)
		return true;
	ii=i;jj=j;cnt=0;
	while(cnt<k)
	{
		if(ii>=0&&ii<n&&jj>=0&&jj<n&&_node[ii][jj]==ch)
			cnt++;
		else
			break;
		ii++;jj--;
	}
	if(cnt==k)
		return true;
	return false;
}
int main()
{
	int cas,ii,i,j,iii;
	bool flag_r,flag_b;
	//freopen("A-large.in","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(ii=1;ii<=cas;ii++)
	{
		scanf("%d%d",&n,&k);
		flag_r=flag_b=false;
		for(i=0;i<n;i++)
			scanf("%s",temp[i]);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				_node[j][n-i-1]=temp[i][j];
		for(i=n-1;i>=0;i--)
			for(j=0;j<n;j++)
				if(_node[i][j]=='.')
					for(iii=i-1;iii>=0;iii--)
						if(_node[iii][j]!='.')
						{
							_node[i][j]=_node[iii][j];
							_node[iii][j]='.';
							break;
						}
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(_node[i][j]=='R'&&flag_r==false)
				{
					if(check(i,j,'R'))
						flag_r=true;
				}
				else if(_node[i][j]=='B'&&flag_b==false)
				{
					if(check(i,j,'B'))
						flag_b=true;
				}
		if(flag_r&&flag_b)
			printf("Case #%d: Both\n",ii);
		else if(flag_r)
			printf("Case #%d: Red\n",ii);
		else if(flag_b)
			printf("Case #%d: Blue\n",ii);
		else
			printf("Case #%d: Neither\n",ii);
	}
	return 0;
}
