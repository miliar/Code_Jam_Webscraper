#include<stdio.h>
#include<fstream>
using namespace std;
ifstream fin("a.in");
ofstream fout("a.out");
void main()
{
	int l,d,n;
	int i,j,k=0,m=0,max=0;
	int f=0,s=0,s1=0;
	char exist[25][10];
	char string[10][300];
	char c[10][10][25];
//	scanf("%d%d%d",&l,&d,&n);
	fin>>l>>d>>n;
	for (i=0;i<d;i++)
//		scanf("%s",exist[i]);
	fin>>exist[i];
	printf("input string");
	for (i=0;i<n;i++)
//		scanf("%s",string[i]);
	fin>>string[i];
	for (i=0;i<n;i++)
	{
		m=0;f=0;
		for (j=0;(string[i][j])!='\0';j++)
		{
			if (string[i][j]=='(')
			{
				f=1;
			}
			else if (string[i][j]==')')
			{
				f=0;
				m++;
				k=0;
			}
			else if (f==0)
			{    
				
				c[i][m][0]=string[i][j];
				m++;
			}
			else if (f==1)
			{
				c[i][m][k]=string[i][j];
				k++;
				if (k>max) max=k;
			}
		}
	}
	m=0;
	for (i=0;i<n;i++)
	{
		for (j=0;j<d;j++)
		{
			m=0;
			for (k=0;k<l;k++)
			{
				for (m=0;m<max;m++)
				{
				//	fout << exist[j][k]<<"=="<<c[i][k][m]<<endl;
					if (exist[j][k]==c[i][k][m])
					{
						f=1;s++;
					}
				}
					
			}
			if (s==l) s1++;
			s=0;
			m=0;
			f=0;
		}

		fout << "Case #" << i+1 << ": " << s1 <<endl;
		s1=0;
	}

		



				
}

	