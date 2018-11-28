#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

double dist(double x1, double y1, double x2, double y2) {
  return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

double calc_rad(vector<double> &a, vector<double> &b) {
  return (dist(a[0],a[1],b[0],b[1])+a[2]+b[2])/2.0;
}

int main() {
  cout.precision(6);
  cout.setf(ios::fixed);
  int C;
  cin >> C;
  for (int iC=1; iC<=C; ++iC) {
    int n;
    cin >> n;
    vector<vector<double> > pl(n,3);
    for (int i=0; i<n; ++i) {
      cin >> pl[i][0] >> pl[i][1] >> pl[i][2];
    }
    double ans=-1.0;
    if (n==1) {
      ans=pl[0][2];
    }
    else if (n==2) {
      ans=max(pl[0][2],pl[1][2]);
    }
    else if (n==3) {
      ans=max(calc_rad(pl[0],pl[1]),pl[2][2]);
      ans=min(ans,max(calc_rad(pl[0],pl[2]),pl[1][2]));
      ans=min(ans,max(calc_rad(pl[1],pl[2]),pl[0][2]));
    }
    cout << "Case #" << iC << ": " << ans << endl;
  }
}
