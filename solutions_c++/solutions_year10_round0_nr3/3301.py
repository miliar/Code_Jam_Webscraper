#include <fstream>
#include <sstream>
#include <iostream>
#include <list>
using namespace std;

int main(int argc, char *argv[])
{
  ifstream file(argv[1]);
  int nbTestCases;
  file >> nbTestCases;
//  cout << nbTestCases<< endl;
  for (int i = 0; i<nbTestCases; ++i ) {
      int R;
      long long k;
      int n;
      file >> R >> k >> n;
      long long money = 0;
      list<int> queue;
      for (int j=0; j<n; ++j) {
          int zgroup;
          file >> zgroup;
          queue.push_back( zgroup );
      }
      list<int> nqueue;
  //    cout << "##########################" << endl;
      for (int j = 0; j<R; ++j) {
          int ck = 0;
          while ( ((ck+queue.front()) <= k) && (!queue.empty())) {
             ck += queue.front();
//             cout << queue.front()<< " ";
             nqueue.push_back( queue.front() );
             queue.pop_front();
          }
          nqueue.insert( nqueue.begin(), queue.begin(), queue.end() );
          queue = nqueue;
          nqueue.clear();
//          cout << endl;
          money += ck;
      }

      cout << "Case #" << i+1 << ": " << money << endl;
//          (( (k % mx ) == (mx-1) ) ? "ON" : "OFF") << endl;
  }
}
