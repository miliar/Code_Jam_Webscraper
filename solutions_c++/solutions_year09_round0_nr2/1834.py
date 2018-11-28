#include <cstdio>
#include <map>

#define DISJOINT_SET_SIZE 10000

struct DisjointSet
{
  int parent[DISJOINT_SET_SIZE];
  int rank  [DISJOINT_SET_SIZE];
  
  DisjointSet()
  {
    int i;
    for ( i=0; i<DISJOINT_SET_SIZE; ++i ) {
      parent[i] = i;
      rank  [i] = 0;
    }
  }
  
  int Find( const int x )
  {
    int i = x;
    while ( parent[i]!=i ) i = parent[i];
    return i;
  }
  
  void Union( const int x, const int y )
  {
    const int x_root = Find(x);
    const int y_root = Find(y);
    if ( x_root==y_root ) return;
    if      ( rank[x_root] > rank[y_root] ) parent[y_root] = x_root;
    else if ( rank[x_root] < rank[y_root] ) parent[x_root] = y_root;
    else {
      parent[y_root] = x_root;
      ++rank[x_root];
    }
  }
  
};

struct Map
{
  int rows,cols;
  int matrix[100][100];
  
  void Read()
  {
    scanf("%d%d",&rows,&cols);
    int i,j;
    for ( i=0; i<rows; ++i )
      for ( j=0; j<cols; ++j )
        scanf("%d",&matrix[i][j]);
  }
  
  void Solve()
  {
    const int di[4]={-1, 0, 0,+1};
    const int dj[4]={ 0,-1,+1, 0};
    const int INF = 2147483647;
    
    DisjointSet sets;
    int i,j,k,ni,nj,ti,tj,min;
    
    for ( i=0; i<rows; ++i )
      for ( j=0; j<cols; ++j ) {
        min = INF;
        for ( k=0; k<4; ++k ) {
          ni = i+di[k];
          nj = j+dj[k];
          if ( ni>=0 && ni<rows &&
               nj>=0 && nj<cols && 
               matrix[ni][nj] < matrix[i][j] &&
               matrix[ni][nj] < min ) {
            min = matrix[ni][nj];
            ti = ni;
            tj = nj;
          }
        }
        if ( min != INF ) {
          sets.Union(  i*cols +  j,
                      ti*cols + tj );
        }
      }
    
    // output
    std::map<int,char> label;
    int  set_index;
    char set_label,max_label('a');
    
    for ( i=0; i<rows; putchar('\n'),++i )
      for ( j=0; j<cols; ++j ) {
        set_index = sets.Find( i*cols+j );
        if ( label.count(set_index) ) set_label = label[set_index];
        else                          set_label = label[set_index] = max_label++;
        if ( j>0 ) putchar(' ');
        putchar(set_label);
      }
  }
};

int main()
{
  int num_tests,i;
  scanf("%d",&num_tests);
  for ( i=1; i<=num_tests; ++i ) {
    printf("Case #%d:\n",i);
    Map map;
    map.Read();
    map.Solve();
  }
}