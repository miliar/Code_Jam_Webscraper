#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<math.h>
#include<iostream.h>
#include<string.h>

void main()
{
	FILE *in,*out;
	//long long float n;
	//long long float m;
	int mat[50][50];
	char a;
	int r,c;
	int cases;
	int i,j,k;
	int count;
	int flag;
	clrscr();
	freopen("D:\\a0.in","r",stdin);
	freopen("D:\\def.txt","w",stdout);
	cin>>cases;
	for(i=0;i<cases;i++)
	{
		flag=0;
		count=0;
		cin>>r;
		cin>>c;
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				cin>>a;
				if(a=='.')
					mat[j][k]=0;
				else
				{
					mat[j][k]=1;
					count++;
				}
			}
		}
		if((count%4)!=0)
		{
			cout<<"Case #"<<(i+1)<<":\nImpossible\n";
			flag=1;
		}
		else
		{
			for(j=0;j<(r-1);j++)
			{
				for(k=0;k<(c-1);k++)
				{
					if((mat[j][k]==0)||(mat[j][k]==2)||(mat[j][k]==3))
					{
					}
					else
					{
					if((mat[j][k]==1)&&(mat[j][k+1]==1)&&(mat[j+1][k]==1)&&(mat[j+1][k+1]==1))
					{
						mat[j][k]=2;
						mat[j][k+1]=3;
						mat[j+1][k]=3;
						mat[j+1][k+1]=2;
					}
					else
					{
						//cout<<"Case #"<<(i+1)<<":\nImpossible\n";
						flag=1;
					}
					}
				}
			}
			if(flag==0)
			{
				cout<<"Case #"<<(i+1)<<":\n";
				for(j=0;j<r;j++)
				{
					for(k=0;k<c;k++)
					{
						if(mat[j][k]==0)
						{
							cout<<".";
						}
						if(mat[j][k]==2)
						{
							cout<<"/";
						}
						if(mat[j][k]==3)
						{
							cout<<"\\";
						}
					}
					cout<<"\n";
				}
				//cout<<"\n";
			}
			else
				cout<<"Case #"<<(i+1)<<":\nImpossible\n";

		}
	}
	fclose(stdin);
	fclose(stdout);
	getch();
}
