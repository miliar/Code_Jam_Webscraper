#include<cstdio>
#include<cstring>
#include<algorithm>
#define N 5002
#define M 52
#define K 502
using namespace std;
char a[N][M],c[K],s[K][M];
short int n,L,d,poz;
int num, rez;
bool compar1(const char&a,const char&b)
{
	return a<b;
}
void sir()
{
	num=1;
	int i;
	bool paranteza=false;
	for (i=0; c[i]&&c[i]!='\n'; ++i)
	{
		if (c[i]=='(')
		{
			paranteza=true;
			/*if (i&&c[i-1]!=')')
			{
				s[num][0]=poz;
				sort (s[num]+1,s[num]+1+poz,compar1);
				++num;
				poz=0;
			}*/
			continue;
		}
		if (!paranteza)
		{
			s[num][0]=1;
			s[num][1]=c[i];
			++num;
			continue;
		}
		if (c[i]==')')
		{
			paranteza=false;
			s[num][0]=poz;
			sort (s[num]+1,s[num]+1+poz,compar1);
			++num;
			poz=0;
			continue;
		}
		s[num][++poz]=c[i];
	}
	if (c[i-1]==')'||!paranteza) --num;
}
bool compar(const char*&a,const char*&b)
{
	int x=strcmp(a,b);
	if (x<=0)
		return true;
	return false;
}
bool caut(char c,int x)
{
	int p=1,u=s[x][0],m;
	while (p!=u)
	{
		m=(u+p)/2;
		if (s[x][m]>=c)
			u=m;
		else
			p=m+1;
	}
	if (s[x][p]==c)
		return true;
	return false;
}
void matrice()
{
	bool ok;
	for (int i=1; i<=d; ++i)
	{
		ok=true;
		for (int j=0; j<L; ++j)
			if (!caut(a[i][j],j+1))
			{
				ok=false;
				break;
			}
		if (ok)
			++rez;
	}
}
void citire()
{
	freopen("aliens.in","r",stdin);
	freopen("aliens.out","w",stdout);
	scanf("%hd%hd%hd\n",&L,&d,&n);
	for (short int i=1; i<=d; ++i)
		fgets(a[i],M-1,stdin);
	for (int i=1; i<=n; ++i)
	{
		fgets(c,K-1,stdin);
		sir();
		rez=0;
		if (num==L)
			matrice();
		printf("Case #%d: %d\n",i,rez);
		
	}
}
int main()
{
	citire();
	return 0;
}
