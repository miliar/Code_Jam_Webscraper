#include <iostream>
#define maxn 10010

int h , w , n , t;
int rank[maxn],pnt[maxn];
int dir[4][2] = {   {-1 , 0} , {0 , -1} ,  {0 ,1} , {1 , 0} }; // North, West, East, South
int a[101][101] , db[10010];

inline int getNo(int i , int j)
{
	return i * w + j;
}

void makeset ( int x )
{ 
	rank [pnt[x]=x] = 0; 
}

int findUnionSet(int x)
{ 
	int px = x, i;
	while(px != pnt[px]){
		px = pnt[px];
	}
	while(x != px){
		i = pnt[x];
		pnt[x] = px;
		x = i;
	}
	return px;
}

void mergeUnionSet(int x, int y) // or just pnt[find(x)]=find(y)
{ 
	if(rank[x=findUnionSet(x)] > rank[y=findUnionSet(y)]) 
		pnt[y] = x;
	else
	{
		pnt[x] = y;
		rank[y] += (rank[x]==rank[y]);
	}
}

int main()
{
	freopen("B-large.in" , "r" , stdin);
	freopen("B-large.out" , "w" , stdout);
	int i , j , k , ca , pi , pj;
	scanf("%d" , &t);
	for( ca = 1 ; ca <= t ; ca++)
	{
		scanf("%d%d" , &h , &w);
		for( i = 0 ; i < h ; i++)
			for( j = 0 ; j < w ; j++)
				scanf("%d" , &a[i][j]);
		n = h * w;
		for(i = 0 ; i < n ; i++)
			makeset(i);
		for( i = 0 ; i < h ; i++)
			for( j = 0 ; j < w ; j++)
			{
				int mh = a[i][j] , pn;
				for (k = 0 ; k < 4 ; k++)
				{
					pi = dir[k][0] + i;
					pj = dir[k][1] + j;
					if( pi >=0 && pi < h && pj >=0 && pj < w && a[pi][pj] < mh)
					{
						pn = getNo(pi , pj);
						mh = a[pi][pj];
					}
				}
				if( mh < a[i][j] )
					mergeUnionSet(getNo(i , j) , pn);
			}
		memset( db , 0 , sizeof(db));
		char no = 'a' - 1;
		printf("Case #%d:\n" , ca);
		for( i = 0 ; i < h ; i++)
			for( j = 0 ; j < w ; j++)
			{
				int pn = findUnionSet(getNo(i , j));
				if(!db[pn])
				{
					no++;
					db[pn] = no;
				}
				printf("%c" , db[pn]);
				if(j == w-1 )printf("\n");
				else printf(" ");
			}
	}
	return 0;
}

/*

5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8

5
2 3
7 6 7
7 6 7
*/