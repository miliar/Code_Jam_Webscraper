#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <sstream>

using namespace std;

#define iter(c) __typeof((c).begin())

#define rep(i,n) for(int i=0; i<(int)(n); i++)
#define repd(i,n) for(int i=(int)(n); i-->0;)
#define repi(i,a,b) for(int i=(int)(a); i<=(int)(b); i++)
#define times(n) for(int __times=(n); __times-->0;)
#define each(i, c) for (iter(c) i = (c).begin(); i != (c).end(); ++i)

#define all(a) (a).begin(),(a).end()
#define elem(e, c) (find(all(c), (e)) != (c).end())
#define pb push_back
#define mp make_pair
#define fst first
#define snd second

#define INF 501001001
#define INFTY (INF<<32LL|INF)
#define EPS 1e-9
#define PI 3.141592653589793

typedef long long ll;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<double> vd;
typedef vector<string> vs;

template <class T>
void debug(vector<T> v){ each(i,v.size()) cout<<*i<<" "; cout<<endl; }

int nextInt(){ int t; scanf("%d", &t); return t; }
string next(){ string t; cin>>t; return t; }

#define N 102
int bac[N][N];
int main(){
  int T=nextInt();
  repi(cases,1,T){
    rep(i,N) rep(j,N) bac[i][j]=0;
    int R = nextInt();
    rep(k,R){
      int x1=nextInt();
      int y1=nextInt();
      int x2=nextInt();
      int y2=nextInt();
      repi(x,x1,x2) repi(y,y1,y2) bac[x][y]=1;
    }
    int cnt;
    for(cnt=0;;cnt++){
      //rep(y,10){
	//rep(x,10) cout<<bac[x][y];
	//cout<<endl;
      //}cout<<endl;
      bool isEnd=true;
      rep(i,N) rep(j,N) if(bac[i][j]) isEnd=false;
      if(isEnd) break;
      for(int x=N-1;x>0;x--) for(int y=N-1;y>0;y--){
	bac[x][y]=(bac[x][y]+bac[x-1][y]+bac[x][y-1])/2;
      }
    }
    cout<<"Case #"<<cases<<": ";
    cout<<cnt;
    cout<<endl;
  }
  return 0;
}
/* c.hs
import List
import Array

gcj solver = readLine >>=
  sequence_ . flip take [solver >>= output num | num <- [1..]] where
    output num ans = putStrLn $ "Case #"++show num++": "++ans
readLine = fmap read getLine

main = gcj $ do
  r <- fmap read getLine
  recs <- sequence $ replicate r (fmap (map read . words) getLine)
  return . show $ solve recs

w=102
solve recs =
  let bac0 = [((x,y),1)| [x1,y1,x2,y2]<-recs, x<-[x1..x2], y<-[y1..y2]]
      bac = accumArray (flip const) 0 ((0,0),(w,w)) bac0
  in length . takeWhile (not . annihilated) $ iterate step bac
  where
    step bac = accumArray (flip const) 0 ((0,0),(w,w)) $
      [((x,y),major (bac!(x,y)) (bac!(x-1,y)) (bac!(x,y-1)))|
        x<-[1..(w-1)], y<-[1..(w-1)]]
    major a b c = (a+b+c)`div`2
    annihilated bac = all (==0) (elems bac)
*/
