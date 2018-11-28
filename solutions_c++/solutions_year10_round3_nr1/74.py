/**
   File: main.cpp

   (c) Copyright Albert Graells Rovira

   $Id$
*/

#include <iostream>
#include <vector>
#include <cmath>

#define x first
#define y second
#define EPS 1e-9

using namespace std;

typedef pair<int,int> pii;

pii operator+(const pii &a,const pii &b){ return pii(a.x+b.x,a.y+b.y); }
pii operator-(const pii &a,const pii &b){ return pii(a.x-b.x,a.y-b.y); }
int operator*(const pii &a,const pii &b){ return a.x*b.x+a.y*b.y; }
ostream &operator<<(ostream &out,pii &a){ out << "(" << a.x << "," << a.y << ")"; return out;}
istream &operator>>(istream &in, pii &a){ in >> a.x >> a.y; return in;}
int     det(const pii &a,const pii &b){ return a.x*b.y-a.y*b.x; }
int  isleft(const pii &a,const pii &b,const pii &c){ return det(b-a,c-a);}
double dist(const pii &a,const pii &b){ return sqrt((a-b)*(a-b));}

bool overlap(const pii &a1,const pii &a2,const pii &b){
    if(isleft(a1,a2,b)==0 and abs(dist(a1,b)+dist(b,a2)-dist(a1,a2))<EPS) return true;
    return false;
}

bool inter(pii a1,pii a2,pii b1,pii b2){
  if(det(a2-a1,b2-b1)==0) return false;
  double t= det(b1-a1,b2-b1)/(double)det(a2-a1,b2-b1);
  double u=-det(a2-a1,b1-a1)/(double)det(a2-a1,b2-b1);
  if(-EPS<=t and t<=1+EPS and -EPS<=u and u<=1+EPS) return true;
  return false;
}

bool intersect(pii a, pii b) {
    return inter(pii(0, a.first), pii(1, a.second), pii(0, b.first), pii(1, b.second));
}

int calcResult() {
    int M;
    cin >> M;
    vector<pii> v(M);
    for (int i = 0; i < M; i++) cin >> v[i].first >> v[i].second;

    int iCnt = 0;

    for (int i = 0; i < M; i++) {
        for (int j = i+1; j < M; j++) {
            iCnt += intersect(v[i], v[j]);
        }
    }
    return iCnt;
}

int main()
{
    int N;
    cin >> N;
    for (int k = 1; k <= N; k++) {
        cout << "Case #" << k << ": ";
        cout << calcResult() << endl;
    }
    return 0;
}
