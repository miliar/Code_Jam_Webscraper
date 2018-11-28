/*
ID: Plagapong
LANG: C++
TASK: havannah
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<map>
#define INF 999999999
#define HEX(X,Y) (((X) << 16) | (Y))
#define XGET(H) ((H) >> 16)
#define YGET(H) ((H) & 65535)

using namespace std;
typedef pair<int, int> II;

int s, m;
int neighbors[10];
int pn[10];
map<int, int> papa;
map<int, int> awesome;
int ringring, bridbrid, forkfork;

inline bool isInside(int xx, int yy) {
  if (xx <= 0 || xx >= 2*s) return false;
  if (xx <= s) {
    return yy > 0 && yy < xx + s;
  } else {
    return yy > xx - s && yy < 2*s;
  }
}

inline bool isInside(int x) {
  return isInside(XGET(x), YGET(x));
}

inline int countBits6(int x) {
  return (x&1) + ((x>>1)&1) + ((x>>2)&1) + ((x>>3)&1) + ((x>>4)&1) + ((x>>5)&1);
}

int findPapa(int x) {
  if (papa[x] != x) {
    papa[x] = findPapa(papa[x]);
  }
  return papa[x];
}

int join(int x, int y) {
  int papaX = findPapa(x);
  int papaY = findPapa(y);
  papa[papaX] = papaY;
  awesome[papaY] |= awesome[papaX];
  return papaY;
}

void preprocess() {
  // Preprocess
  
}

void clearVars() {
  // Clear variables
  papa.clear();
  awesome.clear();
  ringring = bridbrid = forkfork = INF;
}

void process() {
  // Code here!
  int xx, yy, hex;
  int garbage = scanf("%d%d", &s, &m);
  for (int i = 0; i < m; i++) {
    garbage = scanf("%d%d", &xx, &yy);
    hex = HEX(xx, yy);
    //printf("%d %d\n", xx, yy);
    // Create new papa
    papa[hex] = hex;
    // Find awesomeness
    int a = 0;
    if (xx == 2*s-1 && yy == 2*s-1) a |= 1;
    if (xx == s     && yy == 2*s-1) a |= 2;
    if (xx == 1     && yy == s    ) a |= 4;
    if (xx == 1     && yy == 1    ) a |= 8;
    if (xx == s     && yy == 1    ) a |= 16;
    if (xx == 2*s-1 && yy == s    ) a |= 32;

    if (yy == 2*s-1  && s < xx && xx < 2*s-1) a |= 64;
    if (yy-xx == s-1 && 1 < xx && xx < s    ) a |= 128;
    if (xx == 1      && 1 < yy && yy < s    ) a |= 256;
    if (yy == 1      && 1 < xx && xx < s    ) a |= 512;
    if (xx-yy == s-1 && 1 < yy && yy < s    ) a |= 1024;
    if (xx == 2*s-1  && s < yy && yy < 2*s-1) a |= 2048;
    awesome[hex] = a;

    // Find the six neighbors
    for (int j = 0; j < 6; j++) {
      neighbors[j] = -1;
      pn[j] = -1;
    }
    if (isInside(xx+1, yy+1)) neighbors[0] = HEX(xx+1, yy+1);
    if (isInside(xx,   yy+1)) neighbors[1] = HEX(xx,   yy+1);
    if (isInside(xx-1, yy  )) neighbors[2] = HEX(xx-1, yy  );
    if (isInside(xx-1, yy-1)) neighbors[3] = HEX(xx-1, yy-1);
    if (isInside(xx,   yy-1)) neighbors[4] = HEX(xx,   yy-1);
    if (isInside(xx+1, yy  )) neighbors[5] = HEX(xx+1, yy  );
    for (int j = 0; j < 6; j++) {
      if (neighbors[j] != -1 && papa.count(neighbors[j])) pn[j] = findPapa(neighbors[j]);
    }

    // Is there a ring?
    bool isRing = false;
    for (int j = 0; j < 6; j++) {
      if (pn[j] != -1 && pn[j] == pn[(j+2)%6]) {
        if (pn[(j+1)%6] == -1 && (pn[(j+3)%6] == -1 ||
                                         pn[(j+4)%6] == -1 ||
                                         pn[(j+5)%6] == -1)) isRing = true;
      }
      if (pn[j] != -1 && pn[j] == pn[(j+3)%6]) {
        if ((pn[(j+1)%6] == -1 || pn[(j+2)%6] == -1) &&
            (pn[(j+4)%6] == -1 || pn[(j+5)%6] == -1)) isRing = true;
      }
    }
    if (isRing) ringring = min(i, ringring);

    // Join them together
    for (int j = 0; j < 6; j++) {
      int nhex = neighbors[j];
      if (nhex == -1) continue;
      if (!papa.count(nhex)) continue;
      //printf("%x %x", findPapa(hex), findPapa(nhex));
      int newPapa = join(hex, nhex);
      a = awesome[newPapa];
      //printf(" -> %x\n", a);
      if (countBits6(a) >= 2) bridbrid = min(i, bridbrid);
      if (countBits6(a >> 6) >= 3) forkfork = min(i, forkfork);
    }
  }

  int uguu = min(min(ringring, bridbrid), forkfork);
  if (uguu == INF)
    printf("none");
  else if (uguu == ringring) {
    if (uguu == bridbrid) {
      if (uguu == forkfork) printf("bridge-fork-ring in move %d", uguu+1);
      else printf("bridge-ring in move %d", uguu+1);
    } else {
      if (uguu == forkfork) printf("fork-ring in move %d", uguu+1);
      else printf("ring in move %d", uguu+1);
    }
  } else {
    if (uguu == bridbrid) {
      if (uguu == forkfork) printf("bridge-fork in move %d", uguu+1);
      else printf("bridge in move %d", uguu+1);
    } else {
      if (uguu == forkfork) printf("fork in move %d", uguu+1);
      else printf("??? in move %d", uguu+1);
    }
  }
}

int main() {
  preprocess();
  int times;
  cin >> times;
  for (int i = 1; i <= times; i++) {
	cout << "Case #" << i << ": ";
	clearVars();
	process();
	cout << endl;
  }
  return 0;
}
