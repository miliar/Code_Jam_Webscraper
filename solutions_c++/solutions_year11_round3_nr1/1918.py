#include <iostream>
#include <string>
#include <sstream>
#include <vector> 
#include <list>

using namespace std;





int main() {
  string parameters;
  std::getline(cin, parameters);
  
  int numberOfCases;
  std::istringstream stream(parameters);
  stream >> numberOfCases;


  for (int caseNum = 0; caseNum < numberOfCases; ++caseNum) { 
    std::getline(cin, parameters);

    int rows;
    int columns;
    
    stream = std::istringstream(parameters);
    stream >> rows;
    stream >> columns;

    vector<string> pictureLines(rows);

    vector< vector<int> > resultPic(rows);
    for (int i = 0; i < rows; ++i) {
      resultPic[i] = vector<int>(columns);
    }

    bool ok = true;

    for (int i = 0; i < rows; ++i) {
      std::getline(cin, pictureLines[i]);
    }


    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < columns; ++j) {
        if (pictureLines[i][j] == '.') {

          if (i == 0 && j == 0) {
            continue;
          }

          if ((i > 0 && j > 0 && resultPic[i-1][j-1] == 1) || (i > 0 && resultPic[i-1][j] == 1) || (j > 0 && resultPic[i][j-1] == 1)) {
            ok = false;
            break;
          }
        }

        if (pictureLines[i][j] == '#' && ok) {
            if (i == 0 && j == 0) {
              resultPic[i][j] = 1;
              if ( i == rows - 1 || j == columns - 1) 
                ok = false;
              continue;
            }

            if (i == 0) {
              if (resultPic[i][j-1] == 1) {
                resultPic[i][j] = 2; 
                continue;
              }
              
              else {
                resultPic[i][j] = 1; 
                if ( i == rows - 1 || j == columns - 1 ) 
                  ok = false;
                continue;
              }
            }

            if (j == 0) {
              if (resultPic[i - 1][j] == 1) {
                resultPic[i][j] = 3; 
                continue;
              }
              else {
                resultPic[i][j] = 1; 
                if ( (i == rows - 1 || j == columns - 1)) 
                ok = false;
                continue;}
            }


            if (resultPic[i-1][j-1] == 1) {
              resultPic[i][j] = 4;
              continue;
            }

            if (resultPic[i-1][j] == 1) {
              resultPic[i][j] = 3;
              continue;
            }

            if (resultPic[i][j - 1] == 1) {
              resultPic[i][j] = 2;
              continue;
            }

            if ( i == rows - 1 || j == columns - 1 ) 
                  ok = false;
            resultPic[i][j] = 1;
        }
      }
    }

    cout << "Case #" << caseNum + 1 << ":" << endl;

    if (!ok) {
      cout << "Impossible" << endl;
    }
    else {
      for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
          switch (resultPic[i][j]) {
          case 0:
            cout << '.';
            break;
          case 1:
            cout << '/';
            break;
          case 2:
            cout << "\\";
            break;
          case 3:
            cout << '\\';
            break;
          case 4:
            cout << "/";
          }
        }
        cout << endl;
      }
    }
  }
  return 0;
}
