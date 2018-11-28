#include<cstdio>
#include<cstring>
char s[5011][17],t[1000];
bool mk[16][27];
int main()
{
	freopen("A-Large.in","r",stdin);
	freopen("A-Large.out","w",stdout);
	int ans,tt,ttt,ii,i,ct,d,n,j,k,l,temp,sz=sizeof(mk),num;
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)
		scanf("%s",s[i]);
	for(tt=1;tt<=n;tt++)
	{
		memset(mk,0,sz);
		scanf("%s",t);
		for(num=i=0;t[i];i++)
			if(t[i]=='(')
			{
				i++;
				while(t[i]!=')')
				{
					mk[num][t[i]-'a']=true;
					i++;
				}
				num++;
			}
			else
			{
				mk[num][t[i]-'a']=true;
				num++;
			}
		for(ct=i=0;i<d;i++)
		{
			for(j=0;j<l;j++)
				if(mk[j][s[i][j]-'a']==false)break;
			if(j==l)ct++;
		}
		printf("Case #%d: %d\n",tt,ct);
	}
	return 0;
}
