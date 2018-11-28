#include<stdio.h>


main()
{
	int l,d,n;
	int i,j,k;

	FILE *fp;
	fp=fopen("input.in","r");

	FILE *fw;
	fw=fopen("out.txt","w");

	fscanf(fp,"%d %d %d",&l,&d,&n);

	char p[5000][15];

	for(i=0;i<d;i++)
		fscanf(fp,"%s",p[i]);

	char dict[500][15][50];  //char[n][l][26]
	char ch;
	fscanf(fp,"%c",&ch);
	for(i=0;i<n;i++)
	{
		char ch;
		for(j=0;j<l;j++)
		{
			fscanf(fp,"%c",&ch);
			if(ch=='(')
			{
				fscanf(fp,"%[^)]",dict[i][j]);
				fscanf(fp,"%c",&ch);
			}
			else
			{
				dict[i][j][0]=ch;
				dict[i][j][1]='\0';
			}
		}
		fscanf(fp,"%c",&ch);
	}
	for(i=0;i<n;i++)  //line sample number second
	{
		int ctr=0;
		int x=0;
		for(x=0;x<d;x++) //line language number first
		{
			for(j=0;j<l;j++)  //token number
			{
				int flag=0;
				int k=0;	
				while(1)
				{
					if(dict[i][j][k]=='\0')
					{
						flag=1;
						break;
					}
					if(dict[i][j][k]==p[x][j])
						break;
					k++;
				}
				if(flag==1)
					break;
			}
			if(j==l)
				ctr++;
		}
		fprintf(fw,"Case #%d: %d\n",i+1,ctr);
	}
}
