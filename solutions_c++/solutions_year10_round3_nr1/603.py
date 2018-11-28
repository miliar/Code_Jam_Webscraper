/*
 * Google code jam 2010 / Round 1C
 * Task A: Rope Intranet
 *
 * Created by Krisztian Balog on 5/23/10.
 */

#include <iostream>
#include <vector>
using namespace std;


int main(int argc, char* argv[]) {
    
  int T = 0;
  cin >> T;
  
  for (int c=0;c<T;c++) {
    int N;
    
    cin >> N;
    
    vector< int > a;
    vector< int > b;
    
    for (int i=0;i<N;i++) {
      int ax;
      int bx;
      cin >> ax;
      cin >> bx;
      
      a.push_back(ax);
      b.push_back(bx);
    }
    
    int s = 0;
    
    for (int i=0;i<N;i++)
      for (int j=i+1;j<N;j++)
        if ((a[i]>a[j] && b[i]<b[j]) || (a[i]<a[j] && b[i]>b[j])) s++;
    
    // output
    cout << "Case #" << (c+1) << ": " << s << endl;
  }
    
  return 0;
}
