#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
// #include<fstream>

#define iter(n) for( int i = 0 ; i < n ; i++ )
#define MAX 100

using namespace std;

//typedef vector<int> vint;
//typedef vector<float> vfloat;
//typedef vector<double> vdouble;
//typedef vector<char> vchar;
//typedef vector< pair<int , int> > vpair;

struct cell
{
     char val;
     int from_x;
     int from_y;
};

int main()
{
// ifstream cin("B-large.in");
// ofstream cout("B-large.out");

int tests;
int dir[4][2] = { {0,-1}, {-1,0}, {1,0}, {0,1} };

cin >> tests;

// system("pause");
int H,W;
for(int t = 0 ; t < tests ; t++)
{
        cin >> H >> W;
        vector<vector<int> > v(H);
        cell res[MAX][MAX];
        
        for(int i = 0; i < H; i++)
                v[i] = vector<int>(W);
         
        for(int i = 0 ; i < H ; i++)
            for(int j = 0 ; j < W ; j++)           
                    {
                     cin >> v[i][j];
                     res[i][j].val = '#';
                    }
        char next = 'a';
        
        cout << "Case #" << t + 1 << ":" << endl;
        
        for(int i = 0 ; i < H ; i++) {
            for(int j = 0 ; j < W ; j++) {
                    
              /*      for(int i1 = 0 ; i1 < H ; i1++) {
            for(int j1 = 0 ; j1 < W ; j1++)
                    cout << res[i1][j1].val;
                    cout << endl;    
                    } */
                    
                if(res[i][j].val == '#')
                    {
                     res[i][j].val = next;
                     int st_y = i,
                         st_x = j;
                         
                     while(true)       
                        {
                         int n_x = -1;
                         int n_y = -1;
                         int min = v[st_y][st_x];
                         
                         for(int p = 0 ; p < 4 ; p++)
                             {
                                 int v_x = st_x + dir[p][0],
                                     v_y = st_y + dir[p][1];
                              
                                 if(v_x >=0 && v_x < W &&
                                    v_y >=0 && v_y < H && min > v[v_y][v_x])
                                  {
                                   
                                   min = v[v_y][v_x];
                                   n_x = v_x;
                                   n_y = v_y;
                                  }
                             }

                         if(n_x != -1 && res[n_y][n_x].val != '#')
                             {
                              char col = res[n_y][n_x].val;
                              while(st_y != i || st_x != j)
                                  {
                                   res[st_y][st_x].val = col;
                                   int p_x = res[st_y][st_x].from_x,
                                       p_y = res[st_y][st_x].from_y;
                                   st_x = p_x;
                                   st_y = p_y;
                                  }
                              res[i][j].val = col;              
                              break;
                             }
                         else if( n_x == -1 )
                             {
                              next++;
                              break;
                             }
                         else
                             {
                              res[n_y][n_x].from_x = st_x;
                              res[n_y][n_x].from_y = st_y;
                              res[n_y][n_x].val = next;
                              st_x = n_x;
                              st_y = n_y;
                             }
                        } // for while(true)
                    }//  if(res[i][j].val == '#')
                   cout << res[i][j].val;
                   if( j!= W-1) cout << ' ';
               } // for - j
               cout << endl;
        } // for - i

} // for - tests

// in.close();
//  system("pause");
return 0;
}
