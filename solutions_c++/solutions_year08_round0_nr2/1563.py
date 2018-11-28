#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node{
	int start;
	int end;
	int type;
};

int N[2];
int n;
int wait;
Node g[205];

bool mark[2][100];
int b[2][101];
int bk[2];
int bc[2];

void qSort(int l,int r)
{
	if(l>=r) return;
	int i,j,m;
	Node t;
	i=l;  j=r;  m=g[l].start;
	do{
		while(g[i].start<m) i++;
		while(g[j].start>m) j--;
		if(i<=j) {
			t = g[i];   g[i] = g[j];   g[j] = t;
			i++;  j--;
		}
	}while(i<=j);
	qSort(l,j);
	qSort(i,r);
}


void Init()
{
	int i,j,tt,tj;
	char str[20];
	scanf("%d",&wait);
	scanf("%d",&N[0]);
	scanf("%d",&N[1]);
	n = N[0] + N[1];
	for(i=0;i<N[0];i++) {
		scanf("%s",str);
		g[i].start = ( (str[0]-48)*10 + str[1]-48 )*60 + (str[3]-48)*10 + str[4]-48;
		scanf("%s",str);
		g[i].end = ( (str[0]-48)*10 + str[1]-48 )*60 + (str[3]-48)*10 + str[4]-48;
		g[i].type = 0;
	}
	for(i=0;i<N[1];i++) {
		scanf("%s",str);
		g[N[0]+i].start = ( (str[0]-48)*10 + str[1]-48 )*60 + (str[3]-48)*10 + str[4]-48;
		scanf("%s",str);
		g[N[0]+i].end = ( (str[0]-48)*10 + str[1]-48 )*60 + (str[3]-48)*10 + str[4]-48;	
		g[N[0]+i].type = 1;
	}
	qSort(0,n-1);
	//for(i=0;i<n;i++)
	//	printf("%d\n",g[i].start);

	bc[0] = bc[1] = bk[0] = bk[1] = 0;
	for(i=0;i<n;i++) {
		tt = g[i].type;
		for(j=0;j<bc[tt];j++)
			if(g[i].start>=b[tt][j])
				break;
		if(j<bc[tt]) {	
			b[tt][j] = 10000000;
		}
		else bk[tt]++;
		tj = abs( tt - 1 );
		b[tj][bc[tj]] = g[i].end + wait;
		bc[tj]++;
	}
	printf("%d %d\n",bk[0],bk[1]);

}



int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int kase,i;
	scanf("%d",&kase);
	for(i=1;i<=kase;i++)
	{
		printf("Case #%d: ",i);
		Init();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}