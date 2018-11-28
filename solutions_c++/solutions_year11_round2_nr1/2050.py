#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <algorithm>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <cmath>

using namespace std;
char fileIn[100]="";
char fileOut[100]="";

#define Cases(N) for (i=0;i<N;i++)
#define CaseOut(n,v) cout<<"Case #"<<(n+1)<<": "<<(v)<<endl
#define CaseOutStd(fp,n,v) fprintf((fp),"Case #%d: %d\n",(n+1),(v))

#define  MAX 105
float OWPS[MAX];
float OOWPS[MAX];
char tables[MAX][MAX];
float values[MAX][MAX];
int main()
{
	cin>>fileIn>>fileOut;
	ifstream cin(fileIn);
	ofstream cout(fileOut);
	int T;
	int i,j,k;
	cin>>T;
	Cases(T)
	{
		int N;
		cin>>N;
		
		memset(tables,0,sizeof(tables));
		memset(values,0,sizeof(values));
		for (j=0;j<N;j++)
		{
			cin>>tables[j];
			int numAll=0,num1=0;
			for (k=0;k<N;k++)
			{
				if(tables[j][k]=='.')
					continue;
				numAll++;//total
				if(tables[j][k]=='1')
					num1++;
			}
			for (k=0;k<N;k++)
			{
				if(k==j)
				{
					values[j][k]=(float)num1/(float)numAll;
					continue;
				}
				switch (tables[j][k])
				{
				case '.':
					values[j][k]=0;
					break;
				case '0':
					values[j][k]=(float)num1/(float)(numAll-1);
					break;
				case '1':			
					values[j][k]=(float)(num1-1)/(float)(numAll-1);
					break;
				}
			}
		}
		
		memset(OWPS,0,sizeof(OWPS));
		memset(OOWPS,0,sizeof(OOWPS));
		
		for (j=0;j<N;j++)
		{int num=0;
			//float RPI=values[j][j]*0.25;	
			for (k=0;k<N;k++)
			{	
				switch (tables[j][k])
				{
				case '.':
					
					break;
				case '0':
					OWPS[j]+=values[k][j];
					num++;
					break;
				case '1':		
					num++;
					OWPS[j]+=values[k][j];
					break;
				}
			}
			OWPS[j]*=0.5;
			OWPS[j]=OWPS[j]/num;
		}
		for (j=0;j<N;j++)
		{
			int num=0;
			for (k=0;k<N;k++)
			{	
				switch (tables[j][k])
				{
				case '.':
					
					break;
				case '0':
					num++;
					OOWPS[j]+=OWPS[k];
					break;
				case '1':
					num++;
					OOWPS[j]+=OWPS[k];
					break;
				}
			}
			OOWPS[j]*=0.5;
			OOWPS[j]=OOWPS[j]/num;
		}
		cout<<"Case #"<<(i+1)<<": "<<endl;
		for(j=0;j<N;j++)
		{

			float RPI=values[j][j]*0.25;	
			RPI+=OWPS[j];
			RPI+=OOWPS[j];
			cout<<RPI<<endl;
		}
		
	}
	return 0;
}
