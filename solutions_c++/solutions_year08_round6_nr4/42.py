#include<iostream>
#include<sstream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>

using namespace std;

#define BET(a,i,b) (((a)<=(i))&&((i)<=(b)))
#define FOR(i,n)  for(int i=0;i<(int)(n);i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> edge_t;
int N,M;

bool dfs(vector<edge_t> A , vector<edge_t>& B , int pos = 0)
{
  if(A.size()==B.size()){
    sort(ALL(A));
    return A==B;
  }
  for(int i = pos ; i< SZ(A) ; i++){
    vector<edge_t> nA(A);
    nA.erase(nA.begin() + i);
    if(dfs(nA , B , i)) return true;
  }
  return false;
}

bool solve_sub(vector<edge_t>& A , vector<edge_t>& B)
{
  sort(ALL(A));
  sort(ALL(B));
  vector<int> perm(N);
  FOR(i,N) perm[i] = i ;
  do{
    vector<edge_t> nA(A);
    FOR(i,SZ(nA)){
      nA[i].first = perm[nA[i].first];
      nA[i].second = perm[nA[i].second];
      if(nA[i].first > nA[i].second)    
        swap(nA[i].first , nA[i].second);
    }
    sort(ALL(nA));
    if(dfs(nA , B))
      return true;
  }while(next_permutation(ALL(perm)));

  return false;
}

void solve()
{
  cin>>N;
  vector<edge_t> A,B;
  FOR(i,N-1){
    int a,b;
    cin>>a>>b; a--; b--;
    if(a>b) swap(a,b);
    A.push_back(MP(a,b));
  }
  cin>>M;
  FOR(i,M-1){
    int a,b;
    cin>>a>>b; a-- ; b--;
    if(a>b) swap(a,b);
    B.push_back(MP(a,b));
  }
  puts(solve_sub(A,B)?"YES":"NO");
}

int main()
{
  int t; 
  cin>>t;
  FOR(case_no,t)
    {
      printf("Case #%d: " , case_no + 1 );
      solve();
    }
  return 0 ;
}
