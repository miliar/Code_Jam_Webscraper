#include <cstdio>
#include <iostream>
#include <iomanip>
#include <set>
#include <vector>
#include <cstring>
using namespace std;
int mat[101][101];
int rows, cols;
char res[101][101];
int dr[4] = {-1, 0, 0, 1};
int dc[4] = {0, -1, 1, 0};

vector<pair<int,int> > neigh[101][101];
bool in(int r, int c){ return r>= 0 && c >= 0 && r < rows && c < cols ;}
void calcNeigh(int r, int c)
{
       int res = -1, alt = 10000000;
       for( int k = 0 ; k < 4; k ++ )
       {
	      int rr = r + dr[k], cc = c + dc[k];
	      if( !in( rr, cc ) ) continue;
	      if( mat[rr][cc] < alt ) alt = mat[rr][cc], res = k;
       }
// //        cout << res << "... " << alt << endl;
       if( mat[r][c] > alt )
       {
	      int rr = r + dr[res], cc  = c + dc[res];
	      neigh[r][c].push_back(make_pair(rr,cc));
	      neigh[rr][cc].push_back(make_pair(r,c));
// 	      cout << r << " " << c << endl;
// 	      cout << ".... " << rr << " " << cc << endl;
       }
}

void dfs(int r, int c, char letter)
{
       if( res[r][c] != ' ' ) return;
       res[r][c] = letter;
       for( int i = 0 ; i < neigh[r][c].size(); i ++ )
	      dfs(neigh[r][c][i].first, neigh[r][c][i].second, letter); 
}





int main()
{
       int i,j ,k;
       int casos; cin >> casos;
       for( int h = 0 ; h < casos; h ++ )
       {
	       cin >> rows >> cols;
	       
	       for( i = 0 ; i < rows; i ++ ) for( j = 0 ; j < cols; j ++ ) cin >> mat[i][j];
	       for( i = 0 ; i < rows; i ++ ) for( j = 0 ; j < cols; j ++ ) neigh[i][j].clear();
	       for( i = 0 ; i < rows; i ++ ) memset(res[i], ' ' , sizeof(res[i]));
	       for( i = 0 ; i < rows; i ++ ) for( j = 0 ; j < cols; j ++ ) calcNeigh(i,j);
	       char c = 'a';
	       for( i = 0 ; i  < rows; i ++ ) for( j = 0 ; j < cols; j ++ ) if( res[i][j] == ' ' ) dfs(i,j,c), c++;
	       cout << "Case #" << h+1 << ":\n";
	       for( i = 0 ;i  < rows; i ++ )
	       {
		      for( j = 0 ; j < cols; j ++ )
		      {
			    if( j ) cout << " "; 
			    cout << res[i][j];
		      }
		      cout << endl;
	       }
       }return 0;
}

		      