/*Written by Vladimir Ignatiev aka Neacher (neacher@gmail.com)*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

int R, C;
char a[100][100];

void test(int i, int j)
{
	if(i==R-1) return;
	if(j==C-1) return;

	if((a[i][j]==1)&&
	  (a[i+1][j]==1)&&
	  (a[i][j+1]==1)&&
	  (a[i+1][j+1]==1))
	{
		  a[i][j]=2;
		  a[i][j+1]=3;
		  a[i+1][j]=3;
		  a[i+1][j+1]=2;
    }
	return;
}

void f()
{	
	for(int i=0;i<R-1;i++)	
		for(int j=0;j<C-1;j++)	
		{
			test(i,j);
		}
}

int main()
{
	FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	int nCount,i;
	char c;
	fscanf(In,"%d",&nCount);
	for(int n=0;n<nCount;n++)
	{
		fprintf(Out,"Case #%d:\n",n+1);
		printf("%d\n",i);
		fscanf(In,"%d%d%*[ \n\r\t]",&R,&C);
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
			{
				fscanf(In,"%c%*[ \n\r\t]",&c);
				if(c=='.') a[i][j]=0;
				else
					if(c=='#') a[i][j]=1;
			}

		f();
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
				if(a[i][j]==1)	{fprintf(Out,"%s\n","Impossible");goto Next;}

		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				switch(a[i][j])
				{
					case 0:  fprintf(Out,".");break;
					case 2:  fprintf(Out,"/");break;
					case 3:  fprintf(Out,"\\");break;
				};
			}
			fprintf(Out,"\n");
		}
Next:;
	};
	fclose(In);
	fclose(Out);
	return 0;
}