#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;

typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define NL printf("\n");
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define sqr(x) ((x)*(x))
#define myabs(x) (((x)<0)?(-(x)):(x))
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)

#define dlong unsigned long long int  /* 64b for unix    : %llu  */
// #define dlong __int64              /* 64b for windows : %I64u */

#define INF 1000000000

int N;
int T;
int NA, NB;
char dTime [7];
char aTime [7];

struct trip {
  int dd, dh, dm;
  int ad, ah, am;
  int sStart;
  int sAt;

  trip (int _dd, int _dh, int _dm, int _ad, int _ah, int _am, int _sStart, int _sAt) {
    dd = _dd; dh = _dh; dm = _dm;
    ad = _ad; ah = _ah; am = _am;
    sStart = _sStart;
    sAt = _sAt;
  }
};

struct comp {
  bool operator () (const trip* t1, const trip* t2) {
    if (t1->dd > t2->dd) return true;
    if (t1->dd < t2->dd) return false;
    if (t1->dh > t2->dh) return true;
    if (t1->dh < t2->dh) return false;
    if (t1->dm > t2->dm) return true;
    if (t1->dm < t2->dm) return false;
    if (t1->ad > t2->ad) return true;
    if (t1->ad < t2->ad) return false;
    if (t1->ah > t2->ah) return true;
    if (t1->ah < t2->ah) return false;
    if (t1->am > t2->am) return true;
    if (t1->am < t2->am) return false;
    return true;
  }
};

int main () {

  priority_queue<trip*,vector<trip*>,comp> Q;

  scanf("%d\n",&N);
  FORU(i,0,N-1) {
    scanf("%d\n",&T);
    scanf("%d %d\n",&NA,&NB);
    FORU(j,0,NA-1) {
      scanf("%s %s\n",dTime,aTime);
      int dh = (dTime[0]-'0')*10+(dTime[1]-'0');
      int dm = (dTime[3]-'0')*10+(dTime[4]-'0');
      int ah = (aTime[0]-'0')*10+(aTime[1]-'0');
      int am = (aTime[3]-'0')*10+(aTime[4]-'0');
      Q.push(new trip(0,dh,dm,0,ah,am,0,0));
    }

    FORU(j,0,NB-1) {
      scanf("%s %s\n",dTime,aTime);
      int dh = (dTime[0]-'0')*10+(dTime[1]-'0');
      int dm = (dTime[3]-'0')*10+(dTime[4]-'0');
      int ah = (aTime[0]-'0')*10+(aTime[1]-'0');
      int am = (aTime[3]-'0')*10+(aTime[4]-'0');
      Q.push(new trip(0,dh,dm,0,ah,am,1,1));
    }

    int tA = 0, tB = 0;
    int aA = 0, aB = 0;
    int allTrips = NA+NB;

    while(!Q.empty()) {
      trip* elem = Q.top();
      Q.pop();

      //cout << elem->dd << ":" << elem->dh << ":" << elem->dm << " " <<
      //        elem->ad << ":" << elem->ah << ":" << elem->am << " [" << elem->sStart << "] at [" << elem->sAt << "]\n";

      if (elem->sAt == 0) {     // at station A
        if (elem->ad == -1) {   // train from B
          ++aA;
        } else {
          if (aA == 0) {        // new train needed
            ++tA;
          } else {
            --aA;
          }
          elem->dd = elem->ad;
          elem->dh = elem->ah;
          elem->dm = elem->am;
          elem->dm += T;
          if (elem->dm >= 60) elem->dh += 1;
          if (elem->dh >= 24) elem->dd += 1;
          elem->dm %= 60;
          elem->dh %= 24;
          elem->ad = -1;
          elem->sAt = 1;
          Q.push(elem);
          --allTrips;
        }
      } else {                  // at station B
        if (elem->ad == -1) {   // train from A
          ++aB;
        } else {
          if (aB == 0) {        // new train needed
            ++tB;
          } else {
            --aB;
          }
          elem->dd = elem->ad;
          elem->dh = elem->ah;
          elem->dm = elem->am;
          elem->dm += T;
          if (elem->dm >= 60) elem->dh += 1;
          if (elem->dh >= 24) elem->dd += 1;
          elem->dm %= 60;
          elem->dh %= 24;
          elem->ad = -1;
          elem->sAt = 0;
          Q.push(elem);
          --allTrips;
        }
      }

      if (allTrips == 0) break;
    }

    while(!Q.empty()) {
      trip* elem = Q.top();
      delete elem;
      Q.pop();
    }

    printf ("Case #%d: %d %d\n",i+1,tA,tB);
  }

  return 0;
}
