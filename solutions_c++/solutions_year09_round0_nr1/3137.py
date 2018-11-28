/*
 * alien.cpp
 *
 *  Created on: Sep 3, 2009
 *      Author: chris
 */

#import <cmath>
#import <valarray>
#import <vector>
#import <fstream>
#import <iostream>
#import <string>
#import <vector>
using namespace std;

ofstream fout;
ifstream fin;

class regex {
public:
  vector<string> vect;
  regex(string str,double L) {
    // cout << "begin regex " << str << endl;
    for (double i = 0; i < L; i++) {
      if (str.substr(0,1).compare("(")==0) {
        int index = str.find(")");
        string vec = str.substr(1,index-1);
        // cout << "vec = " << vec << endl;
        vect.push_back(vec);
        str = str.substr(index+1,str.length());
      } else if (str.substr(0,1).compare(")")!=0 && str.substr(0,1).compare("(")!=0) {
        string vec = str.substr(0,1);
        // cout << "vec2 = " << vec << endl;
        vect.push_back(vec);
        str = str.substr(1,str.length());
      }
    }
  }

  int match(vector<string> strvec) {
    int count = 0;
    for (double i = 0; i < strvec.size(); i++) {
      bool t = true;
      for (double j = 0; j < strvec[i].size(); j++) {
        bool f = false;
        for (double k = 0; k < vect[j].size(); k++) {
      //    // cout << strvec[i].substr(j,1) << " " << vect[j] << endl;
       //   // cout << strvec[i].substr(j,1) << " " << vect[j].substr(k,1) << endl;
          if (strvec[i].substr(j,1).compare(vect[j].substr(k,1)) == 0) {
      //      // cout << k << " f is true" << endl;
            f = true;
          }
        }
        if (!f) {
      //    // cout << "t is false" << f << " " << t << endl;
          t = false;
        }
      }
      if (t) {
     //   // cout << "count++" << endl;
        count++;
      }
    }
    return count;
  }
};

int main() {
  // cout << "started" << endl;
  fin.open("/home/chris/Desktop/A-large.in");
  string line;
  vector<string> dict;
  vector<int> results;
  string Lstr,Dstr,Nstr;
  double L,D,N;
  if (fin.is_open()) {
    getline(fin,line);
    int index = line.find(" ");
    char** end;
//    L = strtod(line.c_str(),line.end());
  //  // cout << "L = " << L << endl;
  //  D = strtod(*end,end);
  //  N = strtod(*end,end);
    Lstr = line.substr(0,index);
    L = atof(Lstr.c_str());
  //  L = strtod(Lstr.c_str(),end);
    // cout << "L = " << L << endl;
    line = line.substr(index+1,line.size());
    index = line.find(' ',index);

    Dstr = line.substr(0,index);
   // D = strtod(Dstr.c_str(),end);
    D = atof(Dstr.c_str());
    // cout << "D = " << D << endl;

    line = line.substr(index,line.size());

   // N = strtod(Nstr.c_str(),end);
    N = atof(line.c_str());
    // cout << "N = " << N << endl;

    // cout << L << " " << D << " " << N << endl;

    for (int i = 0; i < D; i++) {
      getline(fin,line);
    //  // cout << line << endl;
      dict.push_back(line);
    }
    fout.open("results.txt");
    for (int i = 0; i < N; i++) {
      getline(fin,line);
      regex newreg(line,L);
     // // cout << line << endl;
      results.push_back(newreg.match(dict));
      // cout << "matches " << newreg.match(dict) << endl;
      fout << "Case #" << i + 1 << ": " << newreg.match(dict) << endl;
    }
     cout << "done" << endl;

  }
}
