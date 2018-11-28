#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <set>
#include <map>
#include <deque>
#include <sstream>
using namespace std;
typedef vector<string> vs;
typedef vector<vector<string> > vvs;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;

struct mapPt
{
   int x;
   int y;
   int ht;
   bool isSink;
   mapPt* finalDest;
   char tag;
   vector<mapPt*> flowsToMe;
};

class qcomp
{
   public:
      bool operator()(const std::pair<int,mapPt*> &i1, const std::pair<int,mapPt*> &i2) const
      {
         return (i1.first > i2.first);
      }
};

int main()
{
   int numTests;
   cin>>numTests;

   for (int t=1; t<=numTests; t++)
   {
      int a,b, c1,c2, x;
      cin>>a>>b;
      mapPt ***terr = (mapPt***) new mapPt**[a];
      for (c1=0; c1<a; c1++)
         terr[c1] = (mapPt**) new mapPt*[b];

      // read in and populate
      vector<pair<int, mapPt*> > q;
      for (c1=0;c1<a;c1++)
         for (c2=0;c2<b;c2++)
         {
            cin>>x;
            mapPt* n = new mapPt;
            n->x = c1;
            n->y = c2;
            n->ht = x;
            n->tag = ' ';
            n->finalDest = NULL;
            n->isSink = false;
            n->flowsToMe.clear();
            q.push_back(make_pair(x,n));
            terr[c1][c2]=n;
         }

      // sort and filter down to sinks
      sort(q.begin(), q.end(), qcomp());
      vector<pair<int, mapPt*> >::iterator ii;
      for (ii = q.begin(); ii != q.end(); ++ii)
      {
         mapPt *i = ii->second;
//         cout<<"x,y = "<<i->x<<" "<<i->y<<endl;
         int dest[4] = {99999,99999,99999,99999};
         if (i->x != 0) dest[0] = (terr[i->x-1][i->y]->ht < terr[i->x][i->y]->ht ? terr[i->x-1][i->y]->ht : 99999);
         if (i->y != 0) dest[1] = (terr[i->x][i->y-1]->ht < terr[i->x][i->y]->ht ? terr[i->x][i->y-1]->ht : 99999);
         if (i->y != b-1) dest[2] = (terr[i->x][i->y+1]->ht < terr[i->x][i->y]->ht ? terr[i->x][i->y+1]->ht : 99999);
         if (i->x != a-1) dest[3] = (terr[i->x+1][i->y]->ht < terr[i->x][i->y]->ht ? terr[i->x+1][i->y]->ht : 99999);
//         cout<<"dest = "<<dest[0]<<" "<<dest[1]<<" "<<dest[2]<<" "<<dest[3]<<endl;
         int m = min(min(dest[0],dest[1]), min(dest[2],dest[3]));
//         cout<<"m="<<m<<endl;
         i->flowsToMe.push_back(i);

         if (m==99999) 
            i->isSink = true;
         else
         {
            mapPt *fDest;
            if (dest[0]==m)
               fDest = terr[i->x-1][i->y];
            else if (dest[1]==m)
               fDest = terr[i->x][i->y-1];
            else if (dest[2]==m)
               fDest = terr[i->x][i->y+1];
            else
               fDest = terr[i->x+1][i->y];

//            cout<<"dest = "<<fDest->x<<" "<<fDest->y<<endl<<endl;
            for (vector<mapPt*>::iterator jj = i->flowsToMe.begin(); jj != i->flowsToMe.end(); ++jj)
               fDest->flowsToMe.push_back(*jj);
            i->flowsToMe.clear();
         }
      }

      // back annotate final destinations for each point
      for (ii = q.begin(); ii != q.end(); ++ii)
      {
         if (! ii->second->isSink) continue;
         for (vector<mapPt*>::iterator jj = ii->second->flowsToMe.begin(); jj != ii->second->flowsToMe.end(); ++jj)
            (*jj)->finalDest = ii->second;
      }

      // fill in tags
      char nextTag = 'a';
      for (c1=0;c1<a;c1++)
         for (c2=0;c2<b;c2++)
         {
            if (terr[c1][c2]->tag == ' ')
            {
               for (vector<mapPt*>::iterator jj = terr[c1][c2]->finalDest->flowsToMe.begin(); jj != terr[c1][c2]->finalDest->flowsToMe.end(); ++jj)
                  (*jj)->tag = nextTag;
               nextTag++;
            }
         }

      // print answer, free memory as we go
      cout<<"Case #"<<t<<":"<<endl;
      for (c1=0;c1<a;c1++)
      {
         for (c2=0;c2<b;c2++)
         {
            if (c2>0) cout<<" ";
            cout<<terr[c1][c2]->tag;
            delete terr[c1][c2];
         }
         delete [] terr[c1];
         cout<<endl;
      }
      delete [] terr;
   }

   return 0;
}

