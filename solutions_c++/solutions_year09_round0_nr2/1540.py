#include<stdio.h>

struct aNode{
	int x,y;
};

int m,n;   //m行n列
aNode parent[100][100];
int h[100][100];
int map[100][100];


void init()
{
	int i,j;
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
		{
			parent[i][j].x = i;
			parent[i][j].y = j;
			h[i][j] = 0;
		}
}

bool isRoot(aNode a)
{
	aNode p;
	p = parent[a.x][a.y];
	if(p.x == a.x && p.y == a.y)
		return true;
	return false;
}

aNode findRoot(aNode a)
{
	aNode r,temp;
	r = a;
	while(!isRoot(r))
		r=parent[r.x][r.y];
	while(!isRoot(a))
	{
		temp = parent[a.x][a.y];
		parent[a.x][a.y] = r;
		a = temp;
	}
	return r;
}

void Union(aNode a,aNode b)
{
	a = findRoot(a);
	b = findRoot(b);
	if(a.x == b.x && a.y == b.y)
		return;
	if(h[a.x][a.y]>h[b.x][b.y])
	{
		parent[b.x][b.y] = a;
	}
	else if(h[a.x][a.y]<h[b.x][b.y])
	{
		parent[a.x][a.y] = b;
	}
	else 
	{
		parent[a.x][a.y] = b;
		h[b.x][b.y]++;
	}

}

bool check(aNode a)
{
	if(a.x < 0 || a.x >= m || a.y < 0 || a.y >= n)
		return false;
	return true;
}

bool isLower(aNode a,aNode b)   //a是否比b低
{
	if(map[a.x][a.y] < map[b.x][b.y])
		return true;
	return false;
}

void XYZ(){
    #ifndef  ONLINE_JUDGE
    freopen("B-large.in","r",stdin);
    #endif
}

int main()
{
	XYZ();
	FILE * cfPtr;
	cfPtr = fopen("out.txt","w");
	int testNo;
	int i,j,k,p;
	int min;	
	scanf("%d",&testNo);
	int dx[4] = {-1,0,0,1};
	int dy[4] = {0,-1,1,0};
	aNode a;
	aNode r;
	aNode newNode[4];
	int no;
	int num[100][100];
	for(k=1;k<=testNo;k++)
	{
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++)
			for(j=0;j<n;j++)
				scanf("%d",&map[i][j]);
		init();
		for(i=0;i<m;i++)
			for(j=0;j<n;j++)
			{
				a.x = i;
				a.y = j;
				min = -1;
				for(p=0;p<4;p++)
				{
					newNode[p].x = i + dx[p];
					newNode[p].y = j + dy[p];
					if(check(newNode[p]) &&  isLower(newNode[p],a))
						if(min == -1 || isLower(newNode[p],newNode[min]))
							min = p;
				}
				if(min!=-1)
					Union(a,newNode[min]);
			}
		for(i=0;i<m;i++)
			for(j=0;j<n;j++)
				num[i][j] = -1;
		fprintf(cfPtr,"Case #%d:\n",k);
		no = 0;
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)
			{
				a.x = i;
				a.y = j;
				r = findRoot(a);
				if(num[r.x][r.y] == -1)
				{
					num[r.x][r.y] = no;
					no++;
				}
				fprintf(cfPtr,"%c ",'a'+num[r.x][r.y]);
			}
			fprintf(cfPtr,"\n");
		}

	}
	return 0;
}