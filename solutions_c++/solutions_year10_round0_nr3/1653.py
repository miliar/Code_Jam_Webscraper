#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

typedef long long llint;

const int mxn = 1100;

int k, n;
int niz[mxn];

int bio[mxn], R;

pair <llint,int> Poc, Cik;
llint suma[mxn];
llint pom;

void ciklus(){
  Poc = Cik = make_pair(0,0);
  memset( bio, 0, sizeof(bio) );
  memset( suma, 0, sizeof(suma) );
  pom = 0;
  queue <int> now;
  for( int i = 0; i < n; i++ )
    now.push(i);

  int when;
  llint S = 0;
  for( when = 1; !bio[now.front()]; when++ ){
    bio[now.front()] = when;
    vector <int> usao;
    for( int left = k; !now.empty() ; now.pop() ){
      if( niz[now.front()] <= left ){
	usao.push_back(now.front());
	left -= niz[now.front()];
	S += niz[now.front()];
      } else break;
    }
    suma[when] = S;
    for( int i = 0; i < (int)usao.size(); i++) 
      now.push(usao[i]);
    if( when <= R ) pom = S;
  }

  if( bio[now.front()] ) Cik.first = S - suma[bio[now.front()]-1];
  else Cik.first = S;
  Cik.second = when - bio[now.front()];

  Poc.first = S - Cik.first;
  Poc.second = when - Cik.second - 1;

}

llint solve(){
  scanf( "%d %d %d", &R, &k, &n );
  for( int i = 0; i < n; i++ )
    scanf( "%d", &niz[i] );

  ciklus();

  if( R <= Poc.second ) return pom;
  llint ret = Poc.first;
  R-= Poc.second;

  ret += (llint)(R/Cik.second) * Cik.first;
  int kol = R % Cik.second;
  ret += suma[Poc.second+kol] - suma[Poc.second];

  return ret;
}

int main(){
  int t;
  scanf( "%d", &t );
  for( int id = 1; id <= t; id++ )
    printf( "Case #%d: %lld\n", id, solve() );

  return 0;
}
