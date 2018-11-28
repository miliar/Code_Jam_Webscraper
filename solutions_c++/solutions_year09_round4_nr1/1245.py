#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
#include <string>

int N;

struct Matrix
{
  char m[40][41];
  int  depth;

  Matrix& operator= ( const Matrix &mat )
  {
    memcpy(m,mat.m,sizeof(m));
    depth = mat.depth;
    return *this;
  }

  void Read()
  {
    int i;
    depth = 0;
    for ( i=0; i<N; ++i ) scanf("%s",m[i]);
  }

  bool Finish() const
  {
    int x,y;
    for ( x=0; x<N; ++x )
      for ( y=x+1; y<N; ++y )
	if ( m[x][y]=='1' )
	  return false;
    return true;
  }

  void Swap( const int i, const int j )
  {
    char tmp[41];
    strcpy(tmp,m[i]);
    strcpy(m[i],m[j]);
    strcpy(m[j],tmp);
  }

  std::string Hash() const
  {
    int i,j;
    std::string value;
    for ( i=0; i<N; ++i )
      for ( j=0; j<N; ++j )
	value += m[i][j];
    return value;
  }

  void Print() const
  {
    int i,j;
    for ( i=0; i<N; ++i ) puts(m[i]);
    putchar('\n');
  }

} init;

int Solve()
{
  Matrix curr,next;
  std::queue<Matrix> queue;
  std::set<std::string> visited;
  std::string next_hash;
  int i,j;

  if ( init.Finish() ) return 0;
  queue.push(init);
  visited.insert(init.Hash());

  while ( !queue.empty() ) {
    curr = queue.front(); queue.pop();
    for ( i=0; i<N-1; ++i ) {
      next = curr;
      next.Swap(i,i+1); ++next.depth;
      if ( next.Finish() ) return next.depth;
      next_hash = next.Hash();
      if ( visited.count(next_hash)==0 ) {
	visited.insert(next_hash);
	queue.push(next);
      }
    }
  }
}

int main()
{
  int num_cases,i;
  scanf("%d",&num_cases);
  for ( i=1; i<=num_cases; ++i ) {
    scanf("%d",&N);
    init.Read();
    printf("Case #%d: %d\n",i,Solve());
  }
}
