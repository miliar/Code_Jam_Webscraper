#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int test;
	char mat[4][4];
	scanf("%d",&test);
	int count=0;
	while(test--)
	{
		count++;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				cin>>mat[i][j];
		}
		/*for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				cout<<mat[i][j]<<" ";
			cout<<endl;
		}*/

		int cx,co,ct,ccx,cco,cct;
		int spaces=0;
		int flag=0;
		char winner;
		int dcx,dco,dct,d2cx,d2co,d2ct;
		dcx=dco=dct=d2cx=d2co=d2ct=0;
		for(int i=0;i<4;i++)
		{
			cx=co=ct=0;
			ccx=cco=cct=0;
			for(int j=0;j<4;j++)
			{
				if(mat[i][j]=='.')
					spaces++;
				if(mat[i][j]=='X')
					cx++;
				if(mat[i][j]=='O')
					co++;
				if(mat[i][j]=='T')
					ct++;
				if(cx==4 || (cx==3 && ct==1))
				{
					flag=1;
					winner='X';
					break;
				}
				if(co==4|| (co==3 && ct==1))
				{
					flag=1;
					winner='O';
					break;
				}
				//cx=co=ct=0;
				if(mat[j][i]=='X')
					ccx++;
				if(mat[j][i]=='O')
					cco++;
				if(mat[j][i]=='T')
					cct++;
				if(ccx==4 || (ccx==3 && cct==1))
				{
					flag=2;
					winner='X';
					break;
				}
				if(cco==4|| (cco==3 && cct==1))
				{
					flag=2;
					winner='O';
					break;
				}
				//int cdx,cdo,cdt=0;
				if(i==j)
				{
					if(mat[j][i]=='X')
						dcx++;
					if(mat[j][i]=='O')
						dco++;
					if(mat[j][i]=='T')
						dct++;
					if(dcx==4 || (dcx==3 && dct==1))
					{
						flag=3;
						winner='X';
						break;
					}
					if(dco==4|| (dco==3 && dct==1))
					{
						flag=3;
						winner='O';
						break;
					}
				}
					if((i+j)==3)
					{
					if(mat[i][j]=='X')
						d2cx++;
					if(mat[i][j]=='O')
						d2co++;
					if(mat[i][j]=='T')
						d2ct++;
					if(d2cx==4 || (d2cx==3 && d2ct==1))
					{
						flag=4;
						winner='X';
						break;
					}
					if(d2co==4|| (d2co==3 && d2ct==1))
					{
						flag=4;
						winner='O';
						break;
					}

					}
				
			}
		}

		if(flag!=0)
		{
			printf("Case #%d: %c won\n",count,winner,flag);
		}
		else if(flag==0)
		{
			
			if(spaces==0)
			{
				printf("Case #%d: Draw\n",count);
			}
			else
			{
				printf("Case #%d: Game has not completed\n",count);
			}

		}
	}

	return 0;
}



