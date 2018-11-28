#include<iostream>
#include<queue>
#include<string>
using namespace std;
int way[4][2] = {-1 ,0 , 0 , -1 ,0 , 1 , 1 , 0};
int L , r , c , LL;
int mat[105][105];
int biaoji[105][105];
struct QQ
{
	int x , y;
	QQ(){}
	QQ(int x, int y):x(x) , y(y){}
};
QQ now , next;
queue<QQ>kk , empty;
void bfs(int x , int y , int id)
{
	kk = empty;
	kk.push(QQ(x , y));
	biaoji[x][y] = id;
	int father =-1;
	bool f = false;
	int i , j;
	while(!kk.empty())
	{
		int ff = -1;
		now = kk.front();
		kk.pop();
		int Min = 10000000;
		for(i = 0 ; i < 4 ; i++)
		{
			next.x = now.x + way[i][0];
			next.y = now.y + way[i][1];
			if(next.x < 0 || next.x >= r || next.y < 0 || next.y >= c)
			{
				continue;
			}
			if(mat[next.x][next.y] >= mat[now.x][now.y])
				continue;
			if(mat[next.x][next.y]  < Min)
			{
				ff = i;
				Min = mat[next.x][next.y];
			}
		}
		if(ff == -1)
			continue;
		else
		{
			next.x = now.x + way[ff][0];
			next.y = now.y + way[ff][1];
			if(biaoji[next.x][next.y]!=-1)
			{
				father = biaoji[next.x][next.y];
				f = true;
			}
			else
			{
				biaoji[next.x][next.y] = L;
				kk.push(next);
			}
		}
	}
	if(f)
	{
		for(i = 0 ; i < r ; i++)
		{
			for(j = 0 ;j < c ; j++)
			{
				if(biaoji[i][j] == L)
				{
					biaoji[i][j] = father;
				}
			}
		}
	}
	else
	{
		for(i = 0 ; i < r ; i++)
		{
			for(j = 0 ;j < c ; j++)
			{
				if(biaoji[i][j] == L)
				{
					biaoji[i][j] = LL;
				}
			}
		}
		LL++;
	}
	/*for(i = 0 ; i < r ; i++)
	{
		for(j = 0 ;j < c ; j++)
		{
			cout<<biaoji[i][j]<<" ";
		}
		cout<<endl;
	}*/
}
int main()
{
	freopen("B-large.in" , "r" ,stdin);
	freopen("ans.out" , "w" , stdout);
	int T;
	scanf("%d" , &T);
	int C =0;
	while(T--)
	{
		C++;
		scanf("%d%d" ,&r , &c);
		int i , j;
		for(i = 0 ;i < r ; i++)
		{
			for(j = 0 ; j < c ; j++)
			{
				scanf("%d" , &mat[i][j]);
			}
		}
		memset(biaoji , -1 , sizeof(biaoji));
		bool f = false;
		L =0 , LL = 0;
		
		for(i = 0 ; i < r ; i++)
		{
			for(j= 0 ; j < c ;j++)
			{
				if(biaoji[i][j] == -1)
				{
					bfs(i , j , L);
					L++;
				}
			}
		}
		printf("Case #%d:\n" , C);
		for(i = 0 ; i < r ; i++)
		{
			for(j = 0 ; j < c ;j++)
			{
				if(j==0)
					printf("%c" , biaoji[i][j] + 'a');
				else
					printf(" %c" , biaoji[i][j] + 'a');
			}
			printf("\n");
		}
		
	}
	return 0;
}