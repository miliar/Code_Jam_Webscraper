#include <iostream>
using namespace std;
int **classes;
int *flag;
int main()
{
	bool seek(int now);
	bool dec;
	int n,k=1;
	int num;
	int cs;
	int i,j;
	FILE *fp1;
	FILE *fp2;
	fp1=fopen("A-large.in","r");
	fp2=fopen("A-large.out","w");
	fscanf(fp1,"%d\n",&n);
	while(n--)
	{
		fscanf(fp1,"%d\n",&num);
		classes=new int*[num+1];
		flag=new int[num+1];
		j=1;
		for(j=1;j<=num;j++)
		{
			fscanf(fp1,"%d",&cs);
			classes[j]=new int[cs+1];
			classes[j][0]=cs;
			for(i=1;i<=cs;i++)
			{
				fscanf(fp1," %d",&classes[j][i]);
			}
			fgetc(fp1);
		}
		for(i=0;i<num;i++)
		{
			if(classes[i+1][0]==0)
			{
				dec=false;
			}
			else
			{
				for(j=1;j<=num;j++)
				{
					flag[j]=0;
				}
				if(seek(i+1))
				{
					dec=true;
					break;
				}
				else
				{
					dec=false;
				}
			}
		}
		if(dec)
		{
			fprintf(fp2,"Case #%d: Yes\n",k++);
		}
		else
			fprintf(fp2,"Case #%d: No\n",k++);
	}
	return 0;
}

bool seek(int now)
{
	int i;
	if(classes[now][0]==0)
		return false;
	for(i=0;i<classes[now][0];i++)
	{
		if(flag[classes[now][i+1]]==1)
		{
			return true;
		}
		else flag[classes[now][i+1]]=1;
		if(seek(classes[now][i+1]))
		{
			return true;
		}
	}
	return false;
}
