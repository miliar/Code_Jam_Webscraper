#include<cstdio>
#include<cstring>
char f1[500][500],f2[500],s[200],l[200];
int t,mt,n1,n2,n3,len,i,j;
int main()
{
	freopen("B0.in","r",stdin);
	freopen("B0.out","w",stdout);
	scanf("%d",&t);
	for(mt=1;mt<=t;mt++)
	{
		memset(f1,-1,sizeof(f1));
		memset(f2,-1,sizeof(f2));
		scanf("%d",&n1);
		for(i=0;i<n1;i++)
		{
			scanf("%s",s);
			f1[s[0]][s[1]]=s[2];
			f1[s[1]][s[0]]=s[2];
		}
		scanf("%d",&n2);
		for(i=0;i<n2;i++)
		{
			scanf("%s",s);
			f2[s[0]]=s[1];
			f2[s[1]]=s[0];
		}
		scanf("%d",&n3);
		scanf("%s",s);
		len=0;
		for(i=0;i<n3;i++)
		{
			l[len++]=s[i];
			if (len>1)
			{
				if (f1[l[len-1]][l[len-2]]!=-1) 
				{
					l[len-2]=f1[l[len-1]][l[len-2]];
					len--;
				}
			}
			if (len>1)
			{
				for(j=0;j<len-1;j++)
				if (f2[l[j]]==l[len-1]) 
				{
					len=0;
					break;
				}
			}
		}
		printf("Case #%d: [",mt);
		for(i=0;i<len-1;i++)printf("%c, ",l[i]);
		if (len) printf("%c",l[len-1]);
		printf("]\n");
	}
}
