#include <iostream>
#include <vector>
#include <queue>
#include <string.h>
using namespace std;
int graph[200][200];
char res[101][101];
int used[101][101];
int H,W;

/*bool sink(int i , int j)
{
	int v = graph[i+3][j+3];
	if(graph[i-1+3][j+3] >= v && 
	   graph[i+1+3][j+3] >= v &&
	   graph[i+3][j-1+3] >= v &&
	   graph[i+3][j+1+3] >= v)
	return 1;

	return 0;
}*/

bool sink(int i , int j)
{
	int v = graph[i][j];
	if((i-1 >=0) && (graph[i-1][j] < v ))
		return 0;
	if((i+1 < H) && (graph[i+1][j] < v ))
		return 0;
	if((j-1 >= 0) && (graph[i][j-1] < v)) 
		return 0;
	if((j+1 < W) && (graph[i][j+1] < v))
		return 0;
	return 1;

}
void floodfill(int i, int j, int c)
{
	queue < pair<int, int> > q;
	q.push(pair<int,int>(i,j));
	while(!q.empty())
	{
		pair <int,int> p = q.front();
		q.pop();

	//	cout<<p.first<< " " <<p.second << " " << c << endl;
		
		used[p.first][p.second] = c;

		int dy[] = {-1 ,  0 ,  0 , +1};
		int dx[] = { 0 , -1 , +1 ,  0};

		for(int k=0 ; k<4 ; k++)
		{
			int min = 100000 , r=-1, c=-1;
			int ti = p.first + dy[k] , tj = p.second + dx[k];

			if(ti>=0 && tj>=0 && ti<H && tj<W)
			{
				for(int l=0 ; l<4 ; l++)
				{
					int ni = ti + dy[l] , nj = tj + dx[l];
					if(!(ni>=0 && nj>=0 && ni<H && nj<W))	
						continue;

					int v = graph[ni] [nj];
					if(min > v)
					{
						min = v;
						r = ti + dy[l];
						c = tj + dx[l];
					}
				}

				if(r == p.first && c == p.second && !used[ti][tj] && (graph[ti][tj] > graph[p.first][p.second]))
					q.push(pair<int,int>(ti,tj)); //, cout << ti << " " << tj <<endl;
			}
			
		}
	}
}

void traverse_mark(int i, int j, char c , int n)
{	
	queue < pair<int, int> > q;
	q.push(pair<int,int>(i,j));
	//cout << c << endl;
	while(!q.empty())
	{
		pair <int,int> p = q.front();
		q.pop();
		
		res[p.first][p.second] = c;

		int dy[] = {-1 ,  0 ,  0 , +1};
		int dx[] = { 0 , -1 , +1 ,  0};

		for(int k=0 ; k<4 ; k++)
		{
			int ti = p.first + dy[k] , tj = p.second + dx[k];

			if(ti>=0 && tj>=0 && ti<H && tj<W && used[ti][tj] == n 
					&& res[ti][tj] == 0)
				q.push(pair<int,int>(ti,tj));
		}
	}
}

void disp(int a[][101])
{
	for(int i=0 ; i<H ; i++,cout<<endl)
		for(int j=0 ; j<W ; j++)
			cout << a[i][j] <<" ";
	cout<<"------------------"<<endl;
}

void disp(char a[][101])
{
	for(int i=0 ; i<H ; i++,cout<<endl)
		for(int j=0 ; j<W ; j++)
			cout << a[i][j] <<" ";
	cout<<"------------------"<<endl;
}
void solve()
{
	memset(used , 0 , sizeof(used));

	int c=1;
	for(int i=0 ; i<H ; i++)
		for(int j=0  ; j<W  ; j++)
			if(!used[i][j] && sink(i,j))
				floodfill(i , j , c++);

//	disp(used);
	memset(res , 0 , sizeof(res));

	char cur = 'a';
	for(int i=0 ; i<H ; i++)
		for(int j=0 ; j<W ; j++)
			if(res[i][j] == 0)
				traverse_mark(i, j, cur++, used[i][j]);

//	disp(res);

}

int main()
{
	int T;
	cin>>T;

	for(int i=0  ; i<200 ; i++)
		for(int j=0 ; j<200 ; j++)
			graph[i][j] = 100000;

	for(int t=1;  t<=T ; t++)
	{
	
		/*for(int i=0  ; i<200 ; i++)
		for(int j=0 ; j<200 ; j++)
			graph[i][j] = 100000;*/
			
		cin >> H >> W;
		for(int i=0 ; i<H ; i++)
			for(int j=0 ; j<W ; j++)
				cin >> graph[i][j];
		
		/*for(int i=0 ; i<W ; i++)
			graph[H][i] = graph[H+1][i] = graph[H+2][i] = graph[H+3][i] = 100000;
		for(int i=0 ; i<H ; i++)
			graph[i][W] = graph[i][W+1] = graph[i][W+2] = graph[i][W+3] = 100000;*/
			
		solve();
	

		/*cout << H << W <<endl;
		for(int i=0 ; i<H ; i++,cout<<endl)
			for(int j=0 ; j<W ; j++)
				cout<<graph[i+3][j+3]<<" ";*/

		cout << "Case #" << t <<":";
		for(int i=0 ; i<H ; i++)
		{
			cout<<endl;
			for(int j=0 ; j<W ; j++)
				cout << res[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}
