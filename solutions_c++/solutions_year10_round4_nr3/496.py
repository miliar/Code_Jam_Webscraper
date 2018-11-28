#include<iostream>
#include<set>
#define mp make_pair

using namespace std;

int G[2000][2000];

   set<pair<int,int> > used;

   set<int> x;
   set<int> y;

    pair<int,int> all[2000000], all2[2000000];
    int np, n2;

void solve()
{
   int n;

   used.clear();

   scanf("%d", &n);
   for( int i = 0; i < n; ++i )
   { 
    int x, y, x2, y2;

    scanf("%d%d%d%d", &x, &y, &x2, &y2);
    for( int i = x; i <= x2; ++i )
     for( int j = y; j <= y2; ++j )
      used.insert(mp(i,j));
   }

   int br = 0;
   while( used.begin() != used.end() )
   {

    x.clear();
     y.clear();

   for( set<pair<int,int> > :: iterator i1 = used.begin(); i1 != used.end(); ++i1){
     pair<int,int> tmp;

     

     tmp = (*i1);
 
     //printf("pyha %d %d\n",tmp.first,tmp.second);
     x.insert(tmp.first);
     y.insert(tmp.second);
   }

   np = 0;
   for( set<int> :: iterator i1 = x.begin(); i1 != x.end(); ++i1 )
   for( set<int> :: iterator j1 = y.begin(); j1 != y.end(); ++j1 )
   {
     int p, q ;
     p = *i1; q = *j1; 
    //printf("probva %d %d\n",p,q);
      if( used.find( mp(p,q) ) == used.end() )
      if( used.find( mp(p-1,q) ) != used.end() )
      if( used.find( mp(p,q-1) ) != used.end() )
      {
       all[np++] = mp(p,q);//printf("success\n");
      }
    }

    n2 = 0;
    for( set<pair<int,int> > :: iterator i1 = used.begin(); i1 != used.end(); ++i1){
     pair<int,int> tmp;

     

     tmp = (*i1);
     if( used.find(mp(tmp.first-1,tmp.second)) == used.end() )
     if( used.find(mp(tmp.first,tmp.second-1)) == used.end() )
     {
      //printf("maha %d %d\n",tmp.first,tmp.second);
      all2[n2++] = tmp;
      //used.erase(i1);
     }
   }

    for( int i = 0; i < np; ++i ) used.insert(all[i]);
    for( int i = 0; i < n2; ++i ) used.erase(all2[i]);
    //printf("bau bau\n");
    br++;
   }
 
   printf("%d\n",br);
}
int main()
{
    int t;
    scanf("%d", &t);

    for( int i = 1; i <= t; ++i )
    {
     printf("Case #%d: ",i); solve();
    }
return 0;
}
