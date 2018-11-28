#include <stdio.h>
#include <string.h>

char sum[38][5],del[29][5],str[102];
char temp[102];
int n,m,k;

int checkit()
{
	int chk,z,p,i,j;

	for(i=0;i<102;i++)
		temp[i]=0;

	for(i=0;i<k;i++)
	{
		for(j=0;j<i;j++)
		{
			for(z=0;z<m;z++)
			{
				if((del[z][0]==str[j] && del[z][1]==str[i]) || (del[z][1]==str[j] && del[z][0]==str[i]))
				{
					chk=0;
					for(p=i+1;p<k;p++)
						temp[chk++]=str[p];
					k=strlen(temp);
					strcpy(str,temp);
					return 1;
				}
			}
		}

		if(i+1<k)
		{
			for(j=0;j<n;j++)
			{
				if((sum[j][0]==str[i] && sum[j][1]==str[i+1]) || (sum[j][1]==str[i] && sum[j][0]==str[i+1]))
				{
					chk=0;
					for(p=0;p<i;p++)
						temp[chk++]=str[p];
					temp[chk++]=sum[j][2];
					for(p=i+2;p<k;p++)
						temp[chk++]=str[p];
					k=strlen(temp);
					strcpy(str,temp);
					return 1;
				}
			}
		}
	}
	return 0;
}

int main()
{
	int t,tcase;
	int i;
	

	FILE *out;
	out=stdout;//fopen("B.out","w");

	scanf("%d",&tcase);
	for(t=0;t<tcase;t++)
	{
		for(i=0;i<102;i++)
			str[i]=0;

		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",sum[i]);
		scanf("%d",&m);
		for(i=0;i<m;i++)
			scanf("%s",del[i]);
		scanf("%d",&k);
		scanf("%s",str);

		while(1)
		{
			if(checkit()==0)
				break;
		}	

		fprintf(out,"Case #%d: [",t+1);
		for(i=0;i<strlen(str);i++)
		{
			if(i!=0)
				fprintf(out,", ");
			fprintf(out,"%c",str[i]);
		}
		fprintf(out,"]\n");
	}
	return 0;
}