#include<cstdio>
#include<cstring>
#include<queue>



int row, col;
int movrow[4] = { -1,0,0,1};
int movcol[4] = { 0,-1,1,0};
int map[128][128];
int set[128][128] , maxSet = 0;

char check(int i, int j , int val )
{
	if(i < 0 || j < 0 || i>=row || j >=col)
		return 0;

	return  map[i][j] < val;
}

int moveTo(int i , int j)
{
	int min = 1000000;
	int idx = -1;

	for(int n=0;n<4;n++)
	{
		if( check( i+movrow[n] , j+movcol[n] , map[i][j]) )
		{
			if( map[ i+movrow[n] ] [ j+movcol[n] ] < min )
			{
				min = map[ i+movrow[n] ] [ j+movcol[n] ] ;
				idx = n;
			}
		}
	}

	return idx;
}


void doit()
{
	int i ,j;
	maxSet = 1;

	for(i=0;i<row;i++)
		for(j=0;j<col;j++)
		{
			if( !set[i][j] )
			{
				std::queue< std::pair<int ,int> > q;
				char canMove = 0;
				int nextIdx = moveTo( i,j);
				int thisSet = maxSet;
				int nextI =i, nextJ =j;

				q.push( std::make_pair( i,j)) ;
				while( nextIdx!= -1 )
				{
					nextI += movrow[nextIdx];
					nextJ += movcol[nextIdx];

					q.push( std::make_pair(  nextI,  nextJ  ) );
					

					nextIdx = moveTo( nextI ,  nextJ );
				}

				if( set[nextI][nextJ ] )
					thisSet = set[nextI][ nextJ];

				std::pair<int ,int> aaaa;
				while( !q.empty() )
				{
					aaaa = q.front(); q.pop();
					set[ aaaa.first] [ aaaa.second ] = thisSet;

				}

				if( thisSet == maxSet )
					maxSet ++;

			}
		}


}



int main()
{
	int cases = 0 , Case = 0;
	int i ,j;

	scanf("%d" , &cases);
	while(cases-- )
	{
		scanf("%d%d" , &row , &col);

		for(i=0;i<row;i++)
		{
			for(j=0;j<col;j++)
			{
				scanf("%d" , &map[i][j]);
				set[i][j] = 0;
			}
		}

		doit();


		printf("Case #%d:\n" , ++Case);

		for(i=0;i<row;i++)
		{
			if( i == 0 )
			{
				if( set[i][0] != 1 )
					puts("AAAAAAAAAAAAA");
			}

			printf("%c" , set[i][0]+'a'-1);
			for(j=1;j<col;j++)
				printf(" %c" , set[i][j]+'a'-1);
			puts("");

		}





		//puts("");
	}



	return 0;
}