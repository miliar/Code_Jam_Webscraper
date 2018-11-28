#include<stdio.h>
int main()
{
	int l,d,n,i,j,k,l1,count[100],check;
	char word[5001][16],word2[500][500];
	FILE *in=fopen("A-small.in","r");
	FILE *out=fopen("A-small.out","w");
	fscanf(in,"%d %d %d",&l,&d,&n);
	for(i=0;i<d;i++)
	{
		fscanf(in,"%s",word[i]);
	
	}
	for(i=0;i<n;i++)
	{
		count[i]=0;
		fscanf(in,"%s",word2[i]);
	}
	for(i=0;i<d;i++)
	{
		for(j=0;j<n;j++)
		{
			l1=0;
			for(k=0;k<l;k++)
			{
				check=0;
				if(word2[j][l1]=='(')
				{
					l1++;
					while(word2[j][l1]!=')')
					{
						if(word2[j][l1]==word[i][k])
						{
							check=1;
						}
						l1++;
					}
					l1++;
				}
				else
				{
					if(word2[j][l1]==word[i][k])
						check=1;
					l1++;
				}
				if(check==0)
					break;
				if(k==(l-1))
					count[j]++;
			}
		}
	}
	for(j=0;j<n;j++)
		fprintf(out,"Case #%d: %d\n",j+1,count[j]);
}





