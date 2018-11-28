#include <iostream>
#include <vector>


using namespace std;

void vecdumpi(vector<int> vi)
{
 string str = "";
 char num[100];
 for (size_t i=0; i<vi.size(); i++) {
   sprintf(num, "| %02d | %d\n", (int)i, vi[i]);
   str += num;
 }
 cout << str;
}

void vecdumps(vector<string> vs)
{
 string str;
 char num[100];
 for (size_t i=0; i<vs.size(); i++) {
   sprintf(num, "| %02d | %s\n", (int)i, vs[i].c_str());
   str += num;
 }
 cout << str;
}

int main(int argc, char *argv) {
  //  string hoge = "Hello, 
  string hoge;
  int tmpInt, caseNumber;
  int dpArray[1000][100];
  vector<string> engineArray;
  vector<int> queries;

  cin >> caseNumber;

  for (int caseCount=0; caseCount<caseNumber; caseCount++) {
    int engineNum, queryNum;
    engineArray.clear();
    queries.clear();
    cin >> engineNum;
    string tmp;
    getline(cin, tmp);
    for (int j=0; j<engineNum; j++) {
      getline(cin, tmp);
      engineArray.push_back(tmp);
    }

    cin >> queryNum;
    getline(cin, tmp);
    for (int j=0; j<queryNum; j++) {
      getline(cin, tmp);
      for (int k=0; k<engineNum; k++) {
	if (tmp == engineArray[k]) {
	  queries.push_back(k);
	  break;
	}
      }
    }
    //    vecdumpi(queries);
    //    dpArray = malloc(sizeof(int) * 1000 * 100);
    if (queryNum > 0)
    for (int row=0; row<engineNum; row++) {
      if (queries[0] == row) {
	dpArray[0][row] = INT_MAX - 5;
      } else {
	dpArray[0][row] = 0;
      }
    }
    int min;
    int tmpItem;
    for (int col=1; col<queryNum; col++) {
      for (int row=0; row<engineNum; row++) {
	min = INT_MAX;
	for (int i=0; i<engineNum; i++) {
	  tmpItem = dpArray[col-1][i];
	  if (i != row) tmpItem += 1;
	  if (min > tmpItem) {
	    min = tmpItem;
	  }
	}
	if (queries[col] == row) {
	  min = INT_MAX - 5;
	}
	dpArray[col][row] = min;
      }
    }
    int ret = INT_MAX;

    for (int row=0; row<engineNum; row++) {
      if (ret > dpArray[queryNum-1][row]) {
	ret = dpArray[queryNum-1][row];
      }
    }
    if (queryNum == 0) ret = 0;
    cout << "Case #" << (caseCount+1) << ": " << ret << endl;
  }
  return 0;
}

