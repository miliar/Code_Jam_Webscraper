#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;

struct Data {
  int arrival;
  int departure;
  bool fromA;
};

#define For(i,n) for(int i=0;i<(n);++i)

int readtime() {
  int h, m;
  char col;
  cin >> h >> col >> m;
  return h*60+m;
}

int main() {
  int n;
  cin >> n;
  For(c, n) {
    cout << "Case #" << (c+1) << ": ";
    

    int na, nb, ta;
    cin >> ta;
    cin >> na >> nb;
    vector<Data> vd(na+nb);

    priority_queue<PII, vector<PII>, greater<PII> > pq;
    
    For(i, na+nb) {
      vd[i].departure = readtime();
      vd[i].arrival = readtime();
      vd[i].fromA = i<na;
      pq.push(PII(vd[i].departure, i+1));
    }

    int trA=0, trB=0;
    int readyA=0, readyB=0;
    while(not pq.empty()) {
      PII p = pq.top(); pq.pop();

      if (p.second>0) {
	int i = p.second-1;
	if (vd[i].fromA) {
	  if (readyA>0) --readyA;
	  else ++trA;
	}
	else {
	  if (readyB>0) --readyB;
	  else ++trB;
	}
	pq.push(PII(vd[i].arrival+ta, -(i+1)));
      }
      else {
	int i = (-p.second) - 1;
	if (vd[i].fromA) ++readyB;
	else ++readyA;
      }
    }
    cout << trA << " " << trB << endl;
  }

}
