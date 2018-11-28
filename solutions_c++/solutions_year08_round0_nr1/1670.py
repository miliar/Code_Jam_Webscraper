#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <algorithm>

#define INFINITUM 1000
#define NON_VALID (-1)

using namespace std;

int useda[100];
int usedb[100];

int n;

int tdist(int f, int s, int t) {
 if (f - s - t < 0)
  return NON_VALID;
 return f - s - t;
}

int main(void) {
 vector< pair<int,int> > arrive, leave;
 pair<int,int> x;
 int k, u, v, i, j, r, s, mini, nexti, l, minit;
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

  for (i = 0; i < 100; i++)
   useda[i] = 0;
  for (i = 0; i < 100; i++)
   usedb[i] = 0;


  r = 0;
  for (i = 0; i < na; i++) {

   if (nb == 0) {
    r++;
    continue;
   }

   mini = tdist(arrive[i].first, leave[0].second, t);
   nexti = 0;
   if (useda[0])
    mini = NON_VALID;
   else if (mini != NON_VALID)
    useda[0] = 1;

   for (j = 1; j < nb; j++) {
    minit = tdist(arrive[i].first, leave[j].second, t);

    if (mini > minit && minit != NON_VALID && !useda[j]) {
     if (!(nexti == 0 && mini == NON_VALID))
      useda[nexti] = 0;
     mini = minit;
     nexti = j;
     useda[j] = 1;
    }
   }

   if (mini == NON_VALID)
    r++;
  }

  l = 0;
  for (i = 0; i < nb; i++) {

   if (na == 0) {
    l++;
    continue;
   }

   mini = tdist(leave[i].first, arrive[0].second, t);
   nexti = 0;
   if (usedb[0])
    mini = NON_VALID;
   else if (mini != NON_VALID)
    usedb[0] = 1;

   /*
   if (i == 1) {
    cout << "i : " << i << " j : " << 0 << endl;
    cout << "leave[i].first : " << leave[i].first << "\tarrive[0].second : " << arrive[0].second << endl;
    cout << "mini : " << mini << endl;
   }
   */


   for (j = 1; j < na; j++) {
    minit = tdist(leave[i].first, arrive[j].second, t);

    if (mini > minit && minit != NON_VALID && !usedb[j]) {
     if (!(nexti == 0 && mini == NON_VALID))
      usedb[nexti] = 0;
     mini = minit;
     nexti = j;
     usedb[j] = 1;
    }
   }

   if (mini == NON_VALID)
    l++;
  }

  arrive.clear();
  leave.clear();

  cout << "Case #" << k << ": " << r << " " << l << endl;
 }
}
