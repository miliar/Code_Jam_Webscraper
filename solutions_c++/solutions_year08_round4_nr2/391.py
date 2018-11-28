#include<iostream>
#include<vector>
#include<algorithm>
using namespace std ;

int area(int xa,int ya,int xb,int yb,int xc,int yc)
{
 return abs((xc-xa)*(yb-ya) - (xb-xa)*(yc-ya)) ;   
}

main()
{
 freopen("a.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;

 int i,j,runs ;
 int ii,jj ;
 
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  int n,m,a ;
  cin >> n >> m >> a ;
  
  vector<int> ret ;
  bool valid = false ;
  for(i=0;i<=n;i++) if(!valid)
   for(j=0;j<=m;j++) if(!valid)
    for(ii=1;ii<=n;ii++) if(!valid)
     for(jj=1;jj<=m;jj++) if(!valid)
     {
      if(area(i,0,0,j,ii,jj) == a)
      {
       valid = true ;
       ret.push_back(i) ;                      
       ret.push_back(0) ;
       ret.push_back(0) ;                      
       ret.push_back(j) ;
       ret.push_back(ii) ;                      
       ret.push_back(jj) ;
       break ;
      }
     }
  
  if(!valid)
  {
   for(i=0;i<=n;i++) if(!valid)
    for(j=i+1;j<=n;j++) if(!valid)
     for(ii=1;ii<=n;ii++) if(!valid)
      for(jj=1;jj<=m;jj++) if(!valid)
      {
       if(area(i,0,j,0,ii,jj) == a)
       {
        valid = true ;
        ret.push_back(i) ;                      
        ret.push_back(0) ;
        ret.push_back(j) ;                      
        ret.push_back(0) ;
        ret.push_back(ii) ;                      
        ret.push_back(jj) ;
        break ;
       }
      }
  }  
     

  if(!valid)
  {
   for(i=0;i<=m;i++) if(!valid)
    for(j=i+1;j<=m;j++) if(!valid)
     for(ii=1;ii<=n;ii++) if(!valid)
      for(jj=1;jj<=m;jj++) if(!valid)
      {
       if(area(0,i,0,j,ii,jj) == a)
       {
        valid = true ;
        ret.push_back(0) ;                      
        ret.push_back(i) ;
        ret.push_back(0) ;                      
        ret.push_back(j) ;
        ret.push_back(ii) ;                      
        ret.push_back(jj) ;
        break ;
       }
      }
  }  
  if(!valid) printf("Case #%d: IMPOSSIBLE\n",t) ;
  else printf("Case #%d: %d %d %d %d %d %d\n",t,ret[0],ret[1],ret[2],ret[3],ret[4],ret[5]) ;
 }
// while(1) ;     
}
