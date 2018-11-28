#include<iostream>
using namespace std;
int mat[501][501];
int main()
{
	freopen("bin.txt","r",stdin);
	freopen("bout.txt","w",stdout);
	int cas_num;
	scanf("%d",&cas_num);
	for(int case_num=1;case_num<=cas_num;case_num++)
	{
		printf("Case #%d: ",case_num);
		int m,n,d;
		scanf("%d%d%d",&m,&n,&d);
		char c[1000];
		for(int i=0;i<m;i++)
		{
			scanf("%s",c);
			for(int j=0;j<n;j++)
			{
				mat[i][j]=c[j]-'0';
			}
		}
		int z = min(m,n);
		int res=-1;
		for(int ii=z;ii>=3;ii--)
		{
		//	if(ii==3)	cout<<"";
			for(int i=0,p=i+ii-1;p<m;i++,p++)
				for(int j=0,q=j+ii-1;q<n;j++,q++)
			{
				int x1=0,x2=0;
				for(int x=i;x<=p;x++)for(int y = j;y<=q;y++)
				{
					//if((x==i||x==p)&&(y==j||y==q))
					if((x==i&&y==j)||(x==i&&y==q)||(x==p&&y==j)||(x==p&&y==q))
					{
						continue;
					}
					{
					x1+=mat[x][y]*(x*2-i-p);
					x2+=mat[x][y]*(y*2-j-q);
					}
				}
				if(x1==0&&x2==0)
				{
				//	cout<<i<<" "<<j<<" "<<ii<<endl;
					res=ii;
					goto end;
				}
			}
		}
end:;;
		if(res==-1)puts("IMPOSSIBLE");
		else
			printf("%d\n",res);
	}
}