//
// build via command line:
// g++ task.cpp -o task
//
// to run program:
// ./task A-task-data
//
// compiler version: g++ (Ubuntu 4.3.3-5ubuntu4) 4.3.3
//
// Coded by bearded
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

string to(int i, int b) {
    string str;

    while (i > 0) {
        char s[10];
        sprintf(s, "%d", i % b);
        str = s + str;
        i = i/b;
    }
    return str;
}

int main(int argc, char* argv[]) {
  string filename(argv[1]);
  string outfile = filename + ".out";
  string infile = filename + ".in";
  ifstream in(infile.c_str());
  ofstream out(outfile.c_str());

  int n;
  in >> n;

  int m;
  for (int i=1; i<=n; i++) {
      in >> m;
      //vector<int> mas;
      map<int, int> mas;
      int mm = m;
      while (mm > 0) {
        //mas.push_back(mm % 10);
        mas[mm % 10]++;
        mm = mm/10;
      }

      //sort(mas.begin(), mas.end());

      bool bok = true;
      int j;
      for(j=m+1; bok; j++) {
          //vector<int> masc;
          map<int,int> masc;
          int mmc = j;
          while (mmc > 0) {
              int val = mmc % 10;
//              if ((find(mas.begin(), mas.end(), val) != mas.end())||(val == 0))
                //masc.push_back(val);
              masc[val]++;
              mmc = mmc/10;
          }

          mas[0] = 0;
          masc[0] = 0;
          if (masc.size() == mas.size()) {
//          if (masc.size() > 0) {
            //sort(masc.begin(), masc.end());

/*            vector<int>::iterator it = masc.begin();
            vector<int>::iterator it2 = mas.begin();

            bool bbad = false;
            for (it2 = mas.begin(); it2 != mas.end(); it2++, it++) {
                if ((it = find(it, masc.end(), *it2)) == masc.end())
                    bbad = true;
            }*/

            if (equal(mas.begin(), mas.end(), masc.begin()))
                bok = false;
          }
      }
      cout << "Case #" << i << ": " << j-1 << endl;
      out << "Case #" << i << ": " << j-1 << endl;
  }

  return 0;
}
