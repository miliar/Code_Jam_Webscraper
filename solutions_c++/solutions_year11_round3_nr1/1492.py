#include<iostream>
using namespace std;




int main()
{
	int t,total;
	FILE * fp,*fp1;
	fp=fopen("A-large(2).in","r");
	fp1=fopen("OUTPUT A-large.txt","w");
	
	fscanf(fp,"%d",&t);
	
	total=t;
	while(t--)
	{
		int n,i,k=0,j,flag=0;
		
	
		char (*a)[50]=new char[50][50];
	
		char ch;
			int r,c,ct=0;
		fscanf(fp,"%d",&r);
		fscanf(fp,"%d",&c);
		fscanf(fp,"%c",&ch);
	
			for(i=0;i<r;i++)
			{
				for(j=0;j<c;j++)
				{
					fscanf(fp,"%c",&a[i][j]);
					if(a[i][j]=='#')
						ct++;
				}

				fscanf(fp,"%c",&ch);
			}

			fprintf(fp1,"Case #%d:\n",total -t);

			if(ct%4!=0)
			{
				fprintf(fp1,"Impossible\n");

			}
			else
			{

				for(i=0;i<r;i++)
				{
					for(j=0;j<c;j++)
					{
						if(a[i][j]=='#'&&a[i][j+1]=='#'&&a[i+1][j]=='#'&&a[i+1][j+1]=='#')
						{
							
							a[i][j]='/';
							a[i][j+1]='\\';

							a[i+1][j]='\\';
							a[i+1][j+1]='/';

						}

					}
				}

				for(i=0;i<r;i++)
				{
					for(j=0;j<c;j++)
					{
						if(a[i][j]=='#')
						{flag=1;
						break;}

					}
					if(flag==1)
						break;
				}

				if(flag!=1)
				{
				for(i=0;i<r;i++)
				{
					for(j=0;j<c;j++)
					{
					fprintf(fp1,"%c",a[i][j]);

					}
							fprintf(fp1,"\n");
				
				}
				}
				else
				{
						fprintf(fp1,"Impossible\n");
				}
			}

	}



	return 0;
}
	