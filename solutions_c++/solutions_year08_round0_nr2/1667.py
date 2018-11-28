#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <algorithm>

#define INFINITUM 1000
#define NON_VALID (-1)

using namespace std;

int useda[120];
int usedb[120];

int n;

int tdist(int f, int s, int t) {
 if (f - s - t < 0)
  return NON_VALID;
 return f - s - t;
}

int main(void) {
 vector< pair<int,int> > arrive, leave;
 pair<int,int> x;
 int k, u, v, i, j, r, s, mini, nexti, l, minit, found;
 int na, nb, t;
 ifstream fin("prob2.in");

 fin >> n;
 fin.ignore(INFINITUM, '\n');

 for (k = 1; k <= n; k++) {
  fin >> t;
  fin.ignore(INFINITUM, '\n');

  fin >> na >> nb;
  fin.ignore(INFINITUM, '\n');

  for (j = 0; j < na; j++) {
   fin >> u;
   fin.ignore(INFINITUM, ':');
   fin >> v;
   r = 60*u+v;

   fin >> u;
   fin.ignore(INFINITUM, ':');
   fin >> v;
   s = 60*u + v;

   x.first = r;
   x.second = s;

   arrive.push_back(x);
  }

  for (j = 0; j < nb; j++) {
   fin >> u;
   fin.ignore(INFINITUM, ':');
   fin >> v;
   r = 60*u+v;

   fin >> u;
   fin.ignore(INFINITUM, ':');
   fin >> v;
   s = 60*u + v;

   x.first = r;
   x.second = s;

   leave.push_back(x);
  }

  sort(arrive.begin(), arrive.end());
  sort(leave.begin(), leave.end());

  for (i = 0; i < 120; i++)
   useda[i] = 0;
  for (i = 0; i < 120; i++)
   usedb[i] = 0;


  r = 0;
  for (i = 0; i < na; i++) {
   found = 0;
   for (j = 0; j < nb; j++) {
    minit = tdist(arrive[i].first, leave[j].second, t);
    if (minit != NON_VALID)
     if (found && mini > minit && !useda[j]) {
      mini = minit;
      nexti = j;
      useda[j] = 1;
      useda[nexti] = 0;
     } else if (!found && !useda[j]) {
      mini = minit;
      nexti = j;
      useda[j] = 1;
      found = 1;
     }
   }
   if (!found)
    r++;
  }

  l = 0;
  for (i = 0; i < nb; i++) {
   found = 0;
   for (j = 0; j < na; j++) {
    minit = tdist(leave[i].first, arrive[j].second, t);
    if (minit != NON_VALID)
     if (found && mini > minit && !usedb[j]) {
      mini = minit;
      nexti = j;
      usedb[j] = 1;
      usedb[nexti] = 0;
     } else if (!found && !usedb[j]) {
      mini = minit;
      nexti = j;
      usedb[j] = 1;
      found = 1;
     }
   }
   if (!found)
    l++;
  }

  arrive.clear();
  leave.clear();

  cout << "Case #" << k << ": " << r << " " << l << endl;
 }
}
