#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool conflict(vector<vector<int> > &mat)
{
  vector<pair<int,int> > pos;
  for(int i = 0; i < mat.size(); i++)
    {
      for(int j = 0; j < mat[i].size(); j++)
	{
	  if (mat[i][j] == 1 && j > 0 && mat[i][j-1] == 1) return true;
	  if (mat[i][j] == 1 && j < mat[i].size()-1 && mat[i][j+1] == 1) return true;
	  if (mat[i][j] == 1 && i > 0 && j > 0 && mat[i-1][j-1] == 1) return true;
	  if (mat[i][j] == 1 && i > 0 && j < mat[i].size()-1 && mat[i-1][j+1] == 1) return true;
	}
    }
  return false;
}

int BFS(vector<vector<int> > &mat, int r, int c)
{
  vector<pair<int,int> > lst;
  int maxsofar = 0;

  for(int i = 0; i < mat.size(); i++)
    {
      for(int j = 0; j < mat[i].size(); j++)
	{
	  if (mat[i][j] == 0)
	    lst.push_back(pair<int,int> (i,j));
	    
	}
    }


  for(int i = 0; i < r*c*10; i++)
    {
      vector<pair<int,int> > lstnew;
      vector<vector<int> > grid;
      grid = mat;
      lstnew = lst;
      int used = 0;
      int lastmatch  = 0;
      while (lstnew.size() > 0)
	{
	  int rnd = rand() % lstnew.size();
	  int randx, randy;
	  randx = lstnew[rnd].first;
	  randy = lstnew[rnd].second;
	  grid[randx][randy] = 1;
          if (conflict(grid))
	    {
	      grid[randx][randy] = 0;

	    }
	  else
	    {
	    used++;


	    /*	      if (used == 47)
		{
	      	      	      for(int k = 0; k < grid.size(); k++)
	      {
		  for(int j = 0; j < grid[k].size(); j++)
		    {
		      cout << grid[k][j] << " ";
		    }
		  cout << endl;
		}
		cout << endl;
		}*/
	}
	      lstnew.erase(lstnew.begin()+rnd);
	}
      maxsofar = max(used,maxsofar);
    }

   
  return maxsofar;
}


int main()
{
  int cases;
  int c = 1;
  cin >> cases;
  while (cases-- > 0)
    {
      int row, col;
      cin >> row >> col;
      vector<vector<int> > mat;
      mat.resize(row);
      for(int i = 0; i < row; i++)
	{
	  mat[i].resize(col,0);
	}

      for(int i = 0; i < row; i++)
	{
	  for(int j = 0; j < col; j++)
	    {
	      char tmp;
	      cin >> tmp;
	      if (tmp == 'x')
		{
		  mat[i][j] = -1;
		}
	    }
	}
      int val = BFS(mat, row,col);
      
      if (val == -1)
	{
	  cout << "Case #" << c << ": THE CAKE IS A LIE" << endl;
	}
      else
	{
	  cout << "Case #" << c << ": " << val << endl;
	}
      c++;
      //      break;
    }

}
