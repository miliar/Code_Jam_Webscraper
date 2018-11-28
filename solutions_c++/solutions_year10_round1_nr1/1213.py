#include <stdio.h>
#include <vector>
#include <string.h>
using namespace std;
char mat[100][100];
char mat2[100][100];
char mat3[100][100];
void my_swap(char &a,char &b)
{
	char t=a;a=b;b=t;
}
void g(int n, char mat[100][100])
{
	int i,j,k;
	for(j=0;j<n;j++)
	{
		for(i=n-1;i>=0;i--)
		{
			if(mat[i][j]!='.') continue;
			for(k=i-1;k>=0;k--)
			{
				if(mat[k][j]=='.') continue;
				my_swap(mat[i][j],mat[k][j]);
				break;
			}
		}
	}
}

void prt(int n,char mat[100][100])
{
	int i,j,k;
	for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				putchar(mat[i][j]);
				//mat2[r-1-i][i]=mat[i][j];
			}
			putchar('\n');
		}
	putchar('\n');
}
int _k;
int getmax(int a,int b)
{
	return a>b?a:b;
}
int count(vector<char> &a,char c)
{
	int max=0;
	int counter=0;
	if(a.size()==0) return 0;
	if(a[0]==c) counter=1;
	max=getmax(max,counter);
	int i,j,k;
	for(i=1;i<a.size();i++)
	{
		if(a[i-1]==c)
		{
			if(a[i]==c) counter++;
		}
		else
		{
			counter=0;
			if(a[i]==c) counter++;
 		}
		max=getmax(max,counter);
	}
	return max;
}
int _n;
int okay(int i,int j)
{
	if(i<0) return 0;
	if(j<0) return 0;
	if(i>=_n) return 0;
	if(j>=_n) return 0;
	return 1;
}
int _rwin,_bwin;
int cal(int n,char mat[100][100])
{
	int i,j,k;
	int redwin=0;
	int bluewin=0;
	for(i=0;i<n;i++)
	{
		vector <char> a;
		for(j=0;j<n;j++)
		{
			a.push_back(mat[i][j]);
		}
		if(count(a,'R')>=_k) redwin=1;
		if(count(a,'B')>=_k) bluewin=1;
	}
	for(j=0;j<n;j++)
	{
		vector <char> a;
		for(i=0;i<n;i++)
		{
			a.push_back(mat[i][j]);
		}
		if(count(a,'R')>=_k) redwin=1;
		if(count(a,'B')>=_k) bluewin=1;
	}
	for(i=0;i<n;i++)
	{
		vector<char> a;
		for(k=0;;k++)
		{
			int x,y;
			x=i+k;
			y=0+k;
			if(okay(x,y)==0) break;
			a.push_back(mat[x][y]);
		}
		if(count(a,'R')>=_k) redwin=1;
		if(count(a,'B')>=_k) bluewin=1;
	}
	for(j=0;j<n;j++)
	{
		vector<char> a;
		for(k=0;;k++)
		{
			int x,y;
			x=0+k;
			y=j+k;
			if(okay(x,y)==0) break;
			a.push_back(mat[x][y]);
		}
		if(count(a,'R')>=_k) redwin=1;
		if(count(a,'B')>=_k) bluewin=1;
	}
	for(i=0;i<n;i++)
	{
		vector<char> a;
		for(k=0;;k++)
		{
			int x,y;
			x=i+k;
			y=n-1-k;
			if(okay(x,y)==0) break;
			a.push_back(mat[x][y]);
		}
		if(count(a,'R')>=_k) redwin=1;
		if(count(a,'B')>=_k) bluewin=1;
	}
	for(j=0;j<n;j++)
	{
		vector<char> a;
		for(k=0;;k++)
		{
			int x,y;
			x=n-1-k;
			y=j+k;
			if(okay(x,y)==0) break;
			a.push_back(mat[x][y]);
		}
		if(count(a,'R')>=_k) redwin=1;
		if(count(a,'B')>=_k) bluewin=1;
	}
	if(redwin) _rwin=1;
	if(bluewin) _bwin=1;
	//for()
	//printf("<%d,%d>\n",redwin,bluewin);
	return 0;
}
string res()
{
	int a=_rwin;
	int b=_bwin;
	if(a==1&&b==1) return "Both";
	if(a==0&&b==0) return "Neither";
	
	if(a==1&&b==0) return "Red";
	if(a==0&&b==1) return "Blue";
}
int main()
{
	int cas;
	int i,j;
	//freopen("c:\\1.txt","r",stdin);
	//freopen("c:\\2.txt","w",stdout);

	vector<char> test;
	/*test.push_back('.');
	test.push_back('R');
	test.push_back('R');
	test.push_back('R');
	test.push_back('R');
	test.push_back('R');

	printf("%d",count(test,'R'));*/
	scanf("%d",&cas);
	for(int x=1;x<=cas;x++)
	//while(cas--)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		_k=k;
		_n=n;
		_rwin=0;
		_bwin=0;
		for(i=0;i<n;i++)
				scanf("%s",mat[i]);
		//printf("\n");
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				mat2[n-1-j][i]=mat[i][j];
			}
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				mat3[j][n-1-i]=mat[i][j];
			}

		//cal(n,mat);

		//prt(n,mat2);
		//g(n,mat2);
		//prt(n,mat2);
		//cal(n,mat2);

		//prt(n,mat3);
		g(n,mat3);
		//prt(n,mat3);
		cal(n,mat3);

		//printf("<%d,%d>\n",_rwin,_bwin);
		printf("Case #%d: %s\n",x,res().c_str());
	}
	return 0;
}