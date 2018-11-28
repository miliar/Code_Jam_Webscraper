#include <stdio.h>
#include <map>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	//ofstream debug("check");
	freopen("input","r",stdin);
	freopen("output.txt","w",stdout);
	
	int t,j,i,T;
	scanf("%d%*c",&t);
	//debug << t << endl;
	T=t;
	map<char,int> mymap;
	mymap['X']=24;
	mymap['O']=15;
	mymap['T']=1;
	mymap['.']=0;
	
	while(t--)
	{
		int mat[4][4],tot=0,win=0,empty=0;
		char c[6];
		for(i=0;i<4;i++)
		{
			
			scanf("%s",c);
			for(j=0;j<4;j++)
			{
				mat[i][j]=mymap[c[j]];
				if(mat[i][j]==0)
				empty=1;
			}
			//debug << "Input : " << c << endl;
		//	scanf("%*c");
		}
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				tot+=mat[i][j];
			}
			
			if(tot==60||tot==46)
			{
				printf("Case #%d: O won\n",T-t);
				win=1;
				tot=0;
				break;
			}
			else if(tot==96||tot==73)
			{
				printf("Case #%d: X won\n",T-t);
				win=1;
				tot=0;
				break;
			}
			tot=0;
		}
		
		if(win==0)
		{
			for(j=0;j<4;j++)
			{
				for(i=0;i<4;i++)
				{
					tot+=mat[i][j];
				}
				
				if(tot==60||tot==46)
				{
					printf("Case #%d: O won\n",T-t);
					win=1;
					tot=0;
					break;
				}
				else if(tot==96||tot==73)
				{
					printf("Case #%d: X won\n",T-t);
					win=1;
					tot=0;
					break;
				}
				tot=0;
			}
		}
		
		if(win==0)
		{
			tot=mat[0][0]+mat[1][1]+mat[2][2]+mat[3][3];
			
				if(tot==60||tot==46)
				{
					printf("Case #%d: O won\n",T-t);
					win=1;
					tot=0;
				}
				else if(tot==96||tot==73)
				{
					printf("Case #%d: X won\n",T-t);
					win=1;
					tot=0;
				}
		}
		
		if(win==0)
		{
			tot=mat[0][3]+mat[1][2]+mat[2][1]+mat[3][0];
			
				if(tot==60||tot==46)
				{
					printf("Case #%d: O won\n",T-t);
					win=1;
					tot=0;
				}
				else if(tot==96||tot==73)
				{
					printf("Case #%d: X won\n",T-t);
					win=1;
					tot=0;
				}
		}
		
		if(win==0&&empty==1)
		printf("Case #%d: Game has not completed\n",T-t);
		else if(win==0&&empty==0)
		printf("Case #%d: Draw\n",T-t);
		
		getchar();
	}
}
