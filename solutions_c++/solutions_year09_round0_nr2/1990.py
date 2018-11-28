#include <iostream>
#include <vector>

using namespace std;
enum dir{
	NONE=0,
	NORTH,
	WEST,
	EAST,
	SOUTH
};

int getVal(vector<vector<int> > mat, int i, int j, int row, int col)
{
	if (i >= 0 && j >= 0 && i < row && j < col) return mat[i][j];
	return 100000;
}

int inRange(int i, int j, int row, int col)
{
	if (i >= 0 && j >= 0 && i < row && j < col) return true;
	return false;
}

vector<pair<int, int> > getEdges(vector<vector<int> > &adj, int i, int j, int row, int col)
{
	vector<pair<int,int> > edges;
	if (inRange(i-1,j,row,col) && adj[i-1][j] == SOUTH)
		edges.push_back(pair<int,int>(i-1,j));
	if (inRange(i+1,j,row,col) && adj[i+1][j] == NORTH)
		edges.push_back(pair<int,int>(i+1,j));
	if (inRange(i,j-1,row,col) && adj[i][j-1] == EAST)
		edges.push_back(pair<int,int>(i,j-1));
	if (inRange(i,j+1,row,col) && adj[i][j+1] == WEST)
		edges.push_back(pair<int,int>(i,j+1));

	return edges;
}

vector<pair<int, int> > getEdgesToSink(vector<vector<int> > &adj, int i, int j, int row, int col)
{
	vector<pair<int,int> > edges;
	if (inRange(i-1,j,row,col) && adj[i][j] == NORTH)
		edges.push_back(pair<int,int>(i-1,j));
	if (inRange(i+1,j,row,col) && adj[i][j] == SOUTH)
		edges.push_back(pair<int,int>(i+1,j));
	if (inRange(i,j-1,row,col) && adj[i][j] == WEST)
		edges.push_back(pair<int,int>(i,j-1));
	if (inRange(i,j+1,row,col) && adj[i][j] == EAST)
		edges.push_back(pair<int,int>(i,j+1));

	return edges;
}


pair<int,int> getSink(int i,int j, vector<vector<int> > &adj, int row, int col)
{
	vector<pair<int, int> > edges = getEdgesToSink(adj, i, j, row, col);
	

	for(int k = 0; k < edges.size(); k++)
		return getSink(edges[k].first, edges[k].second, adj, row, col);


	return pair<int,int> (i,j);
}




void DFS(int i, int j, vector<vector<int> > &adj, vector<vector<char> > &labels, int sink, int row, int col)
{
	labels[i][j] = char('a'+sink);
	vector<pair<int, int> > edges = getEdges(adj, i, j, row, col);
	
	for(int k = 0; k < edges.size(); k++)
		DFS(edges[k].first, edges[k].second, adj, labels, sink, row, col);
	
	return;
}


int main()
{
	int cases;
	cin >> cases;
	int row, col;
	int ct = 1;
	while (cin >> row >> col)
	{
		vector<vector<int> > mat(row, vector<int>(col,0));
		vector<vector<int> > adj(row, vector<int>(col,0));
		vector<vector<int> > sink(row, vector<int>(col,0));
		vector<vector<char> > labels(row, vector<char>(col,'0'));

		for(int i = 0; i < row; i++)
			for(int j = 0; j < col; j++)
				cin >> mat[i][j];
		

		for(int i = 0; i < row; i++)
		{
			for(int j = 0; j < col; j++)
			{
				int mn = 100000;
				mn = min(mn, getVal(mat,i+1,j,row,col));
				mn = min(mn, getVal(mat,i-1,j,row,col));
				mn = min(mn, getVal(mat,i,j+1,row,col));
				mn = min(mn, getVal(mat,i,j-1,row,col));
				
				
				if (mn >= mat[i][j])
					sink[i][j] = 1;
				else if (mn == getVal(mat,i-1,j,row,col))
				{
					adj[i][j] = NORTH;
				}
				else if (mn == getVal(mat,i,j-1,row,col))
				{
					adj[i][j] = WEST;
				}
				else if (mn == getVal(mat,i,j+1,row,col))
				{
					adj[i][j] = EAST;
				}
				else if (mn == getVal(mat,i+1,j,row,col))
				{
					adj[i][j] = SOUTH;
				}
								
			}
		}
		
		int sinks = 0;
		
		for(int i = 0; i < row; i++)
		{
			for(int j = 0; j < col; j++)
				if (labels[i][j] == '0')
				{
					pair<int,int> sk = getSink(i,j, adj, row, col);
					DFS(sk.first,sk.second, adj, labels, sinks++, row, col);
				}
		}

		cout << "Case #" << ct++ << ":" << endl;
		for(int i = 0; i < row; i++)
		{
			for(int j = 0; j < col; j++)
			{
				cout << labels[i][j] << " ";
			}
			cout << endl;
		}


	}

}