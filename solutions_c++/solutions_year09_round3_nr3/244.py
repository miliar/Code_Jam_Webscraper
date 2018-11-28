#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<set>
#include<algorithm>
#include<sstream>
#include<queue>
#include<stack>
#include<string>
#include<cmath>
#include<map>
#include<fstream>

#define all(c) c.begin(), c.end()
#define allr(c) c.rbegin(), c.rend()
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define INF (int)1e9

using namespace std ;

int P , Q ;
int pris[200] ;
vector<bool> vis ;

int f1()
{
   return P - 1 ;
}

int f2()
{
   int out = INF ;
   for(int i=0;i<Q;++i) for(int j=0;j<Q;++j) if( i != j )
   {
      int cur = P - 1 ;
      vis[pris[i]] = false ;
      for(int k=pris[j]-1;k>=0 && vis[k];--k,++cur) ;
      for(int k=pris[j]+1;k<P && vis[k];++k,++cur) ;
      out = min(out,cur) ;
      vis.clear() ;
      vis.resize(P,true) ;
   }
   return out ;
}

int f3()
{
   int out = INF ;
   for(int i=0;i<Q;++i) for(int j=0;j<Q;++j) if( i != j )
      for(int l=0;l<Q;++l) if( i!=l && j!=l )
      {
         //cout << pris[i] << " " << pris[j] << " " << pris[l] << " " << endl ;
         int cur = P - 1 ;
         //cout << "\t" << cur << endl ;
         vis[pris[i]] = false ;
         for(int k=pris[j]-1;k>=0 && vis[k];--k,++cur) ;
         for(int k=pris[j]+1;k<P && vis[k];++k,++cur) ;
         //cout << "\t" << cur << endl ;
         vis[pris[j]] = false ;
         for(int k=pris[l]-1;k>=0 && vis[k];--k,++cur) ;
         for(int k=pris[l]+1;k<P && vis[k];++k,++cur) ;
         //cout << "\t" << cur << endl ;
         out = min(out,cur) ;
         vis.clear() ;
         vis.resize(P,true) ;
      }
   return out ;
}

int f4()
{
   int out = INF ;
   for(int i=0;i<Q;++i) for(int j=0;j<Q;++j) if( i != j )
      for(int l=0;l<Q;++l) if( i!=l && j!=l ) for(int m=0;m<Q;++m) if( i!=m && j!=m && l!=m)
      {
         int cur = P - 1 ;
         vis[pris[i]] = false ;
         for(int k=pris[j]-1;k>=0 && vis[k];--k,++cur) ;
         for(int k=pris[j]+1;k<P && vis[k];++k,++cur) ;
         vis[pris[j]] = false ;
         for(int k=pris[l]-1;k>=0 && vis[k];--k,++cur) ;
         for(int k=pris[l]+1;k<P && vis[k];++k,++cur) ;
         vis[pris[l]] = false ;
         for(int k=pris[m]-1;k>=0 && vis[k];--k,++cur) ;
         for(int k=pris[m]+1;k<P && vis[k];++k,++cur) ;
         out = min(out,cur) ;
         vis.clear() ;
         vis.resize(P,true) ;
      }
   return out ;
}

int f5()
{
   int out = INF ;
   for(int i=0;i<Q;++i) for(int j=0;j<Q;++j) if( i != j )
      for(int l=0;l<Q;++l) if( i!=l && j!=l ) for(int m=0;m<Q;++m) if( i!=m && j!=m && l!=m)
         for(int n=0;n<Q;++n) if( i!=n && j!=n && l!=n && m!=n)
      {
         int cur = P - 1 ;
         vis[pris[i]] = false ;
         for(int k=pris[j]-1;k>=0 && vis[k];--k,++cur) ;
         for(int k=pris[j]+1;k<P && vis[k];++k,++cur) ;
         vis[pris[j]] = false ;
         for(int k=pris[l]-1;k>=0 && vis[k];--k,++cur) ;
         for(int k=pris[l]+1;k<P && vis[k];++k,++cur) ;
         vis[pris[l]] = false ;
         for(int k=pris[m]-1;k>=0 && vis[k];--k,++cur) ;
         for(int k=pris[m]+1;k<P && vis[k];++k,++cur) ;
         vis[pris[m]] = false ;
         for(int k=pris[n]-1;k>=0 && vis[k];--k,++cur) ;
         for(int k=pris[n]+1;k<P && vis[k];++k,++cur) ;
         out = min(out,cur) ;
         vis.clear() ;
         vis.resize(P,true) ;
      }
   return out ;
}

int main()
{
   freopen("C-small-attempt0.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   int N ;
   cin >> N ;
   for(int run=1;run<=N;++run)
   {
      cin >> P >> Q ;
      //cout << "\t" << P << " " << Q << endl ;
      for(int i=0;i<Q;++i) { cin >> pris[i] ; --pris[i] ; }
      vis.clear() ;
      vis.resize(P,true) ;
      int out = 0 ;
      if(Q == 1) out = f1() ;
      else if(Q == 2) out = f2() ;
      else if(Q == 3) out = f3() ;
      else if(Q == 4) out = f4() ;
      else if(Q == 5) out = f5() ;
      cout << "Case #" << run << ": " << out << endl ;
   }  
   //while(1) ;
   return 0 ;
}
