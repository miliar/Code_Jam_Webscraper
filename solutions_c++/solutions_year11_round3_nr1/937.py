#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

#define CLR(a) memset(a,0,sizeof(a))
#define F(i,a,b) for(i=a;i<=b;++i)

int t,cs=0,r,c;
char a[100][100];

void tile()
{
	int i,j;

	F(i,1,r-1)
		F(j,1,c-1)
			if(a[i][j]=='#'){
				if(a[i+1][j]!='#'||a[i][j+1]!='#'||a[i+1][j+1]!='#')
					return;
				a[i][j] = '/';
				a[i][j+1] = '\\';
				a[i+1][j] = '\\';
				a[i+1][j+1] = '/';
			}
}

bool imp()
{
	int i,j;

	F(i,1,r)
		F(j,1,c)
			if(a[i][j]=='#')
				return true;
	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int i;

	cin >> t;

	while(t--){
		cin >> r >> c;
		F(i,1,r)
			scanf("%s",&a[i][1]);

		tile();
		
		printf("Case #%d:\n",++cs);
		
		if(imp())
			printf("Impossible\n");
		else	
			F(i,1,r)
				printf("%s\n",&a[i][1]);
		
	}

	return 0;
}