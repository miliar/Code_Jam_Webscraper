#include <string>
#include <iostream>
#include <list>
#include <cstdio>

using namespace std;

const int A=-1, B=1;

int toMin(int hours, int mins)
{
   return mins+hours*60;
}

class Trip
{
 public:
   int e;          // Station
   int dep, arr;   // minutes
   int train;      // train assigned to this trip
   Trip(int e_, int dep_, int arr_): e(e_), dep(dep_), arr(arr_), train(0) {}
   bool operator<(Trip &aTrip)
   {
      if(dep==aTrip.dep) return arr<aTrip.arr;
      else return dep<aTrip.dep;
   } 
};

void assingTrain(list<Trip> &tt, int train, int e, int arrive, int ta)
{
   list<Trip>::iterator cur = tt.begin();
   list<Trip>::iterator end = tt.end();
   while((cur!=end) && (cur->train!=0 || cur->e!=e || cur->dep<arrive)) cur++;
   if(cur!=end)
   {
      cur->train = train;
      assingTrain(tt, train, -e, cur->arr+ta, ta);
   }
}

int main()
{
   int nProblem;
   cin >> nProblem;

   for(int iProblem=1; iProblem<=nProblem; iProblem++)
   {
      list<Trip> tt; // Time table

      int ta;
      cin >> ta;

      int na, nb;
      cin >> na >> nb;

      int trA=0, trB=0;

      char line[80];
      cin.getline(line,80);

      for(int ia=0; ia<na; ia++)
      {
         cin.getline(line,80);
         int dh, dm, ah, am;
         sscanf(line,"%d:%d %d:%d", &dh, &dm, &ah, &am);

         tt.push_back(Trip(A, toMin(dh,dm),toMin(ah,am)));
      }

      for(int ib=0; ib<nb; ib++)
      {
         cin.getline(line,80);
         int dh, dm, ah, am;
         sscanf(line,"%d:%d %d:%d", &dh, &dm, &ah, &am);

         tt.push_back(Trip(B, toMin(dh,dm),toMin(ah,am)));
         tt.sort();
      }

      list<Trip>::iterator cur = tt.begin();
      list<Trip>::iterator end = tt.end();

      int train = 1; // Next train to assign
      while(cur!=end)
      {
         cur->train = train;
         if(cur->e==A) trA++;
         else          trB++;
         assingTrain(tt, train, -cur->e, cur->arr+ta, ta);
         train++; 
         while(cur!=end && cur->train!=0) cur++;
      }

      cout << "Case #" << iProblem << ": " << trA << " " << trB << endl;
   }   
}

//======================================================================== END
