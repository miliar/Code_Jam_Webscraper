#include <stdio.h>
#include <string.h>

int dx[]={1,0,1,-1};
int dy[]={0,1,1,1};

char a[100][100],b[100][100],top[100];
int n,i,j,k,l,o,T,t,red,blue;

int good(int x,int y)
{
	return x>=0 && x<n && y>=0 && y<n;
}

void push(char c,int j)
{
	b[top[j]][j]=c;
	top[j]--;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&l);
		for(i=0;i<n;i++)
			scanf("%s",&a[i]);
		memset(b,'.',sizeof(b));
		for(i=0;i<n;i++)
			top[i]=n-1;
		for(i=0;i<n;i++)
			for(j=n-1;j>=0;j--)
				if(a[i][j]!='.')
					push(a[i][j],n-1-i);
		red=blue=0;
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				for(o=0;o<4;o++)
				{
					for(k=0;k<l;k++)
						if(!good(i+k*dx[o],j+k*dy[o]) || b[i+k*dx[o]][j+k*dy[o]]!='R')
							break;
					if(k==l)
						red=1;
					for(k=0;k<l;k++)
						if(!good(i+k*dx[o],j+k*dy[o]) || b[i+k*dx[o]][j+k*dy[o]]!='B')
							break;
					if(k==l)
						blue=1;
				}
		printf("Case #%d: ",++t);
		if(red && blue)
			printf("Both\n");
		else if(red)
			printf("Red\n");
		else if(blue)
			printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}