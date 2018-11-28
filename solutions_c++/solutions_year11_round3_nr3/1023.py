#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <functional>
#include <math.h>

using namespace std;

#define in cin
#define out cout
#define pf printf

#define g(name) 	in >> name
#define gi(name)	int name;		   g(name)
#define gl(name)	long name;		   g(name)
#define gll(name) long long name;   g(name)
#define gd(name)	double name; 	   g(name)
#define gc(name)	char name;		   g(name)
#define gb(name)	bool name;		   g(name)
#define gs(name)  string name;      g(name)

#define fri(var, a, b)		for( int var = a; var < b; var++ )
#define frd(var, a, b) 	   for( int var = a; var > b; var-- )
#define frv(var, vec)      for( unsigned int var = 0; var < vec.size(); var++ )
#define frvi(it, vec)      for( typeof(vec.begin()) it = vec.begin(); it != vec.end(); it++ )

#define pb push_back
#define mp make_pair

void runTrial(int trial)
{
   gi(numNotes);
   gi(low);
   gi(high);

   int notes[numNotes];

   fri(i, 0, numNotes)
   {
      g(notes[i]);
   }

   bool yes = false;
   int note;

   fri(i, low, high + 1)
   {
      bool valid = true;

      fri(j, 0, numNotes)
      {
         if(i % notes[j] == 0 || notes[j] % i == 0)
            continue;

         valid = false;
      }

      if(valid)
      {
         yes = true;
         note = i;
         break;
      }
   }

   printf("Case #%d: ", trial);
   if(yes)
      printf("%d\n", note);
   else
      printf("NO\n");
}

int main()
{
   gi(numTrials);

   fri(t, 0, numTrials)
      runTrial(t + 1);

   return 0;
}

