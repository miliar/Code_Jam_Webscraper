#include <iostream>
#include <vector>
#include <string>
using namespace std;
struct line {
  double a;
  double b;
  double c;
};

double find_intersection (line l1, line l2);

int main (int argc, char *argv[]) {

  int T, N;
  cin >> T;


  for (int t=1; t<=T; t++) {
    long long total_intersection = 0;
    vector <line> lines;
  
    cin >> N;
    // make eqn of all the lines
    for (int n=0; n<N; n++) {
      double y1, y2;
      cin >> y1 >> y2;
      double a, b ,c;
      a = y2 - y1;
      b = -1;
      c = y1;
      line l;
      l.a = a; 
      l.b = b; 
      l.c = c;
      lines.push_back(l);
    }
    // cout << "No of lines " << lines.size();
    // now find out the intersections
    for (int i=0; i<lines.size(); i++) {
      for (int j=i+1; j<lines.size(); j++) {
	double intersection_pt = find_intersection (lines[i], lines[j]);
	//cout << "The intersection is " << intersection_pt << endl;
	if (intersection_pt >0 && intersection_pt <1) {
	  total_intersection++;
	}
      }
    }
    cout << "Case #" << t << ": " << total_intersection << endl;
    lines.clear();
  }
  return 0;
}

double find_intersection (line l1, line l2) {

  //x =   (b1c2 - b2c1) / (a1b2-a2b1)
  double intersection_pt;
  if ((l1.a * l2.b - l2.a * l1.b ) != 0) {
    intersection_pt = (l1.b * l2.c - l2.b * l1.c) / (l1.a * l2.b - l2.a * l1.b );
  } else {
    intersection_pt = 0;
  }

  return  intersection_pt;
}
