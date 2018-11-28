#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set> 
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <list>
using namespace std;

int main()
{
  ifstream ins("testcase");
  ofstream ous("result");
  string line;
  getline(ins,line);
  int caseNum = atoi(line.c_str());
  for (int i = 0 ; i < caseNum; i++) {
    getline(ins,line);
    stringstream ss(line);
    int n,k;
    string result;
    ss>>n;
    ss>>k;
    char martix[n][n];
    cout<<n<<" "<<k<<endl;
    //red = 1, blue =2. empty = 0
    for (int j = 0; j < n; j ++) {
      getline(ins,line);
      list<char> row;
      for (int l = 0; l < n; l ++) {
	if (line[l] == '.') {
	  row.push_front('.');
	}
	else if (line[l] == 'R') {
	  row.push_back('R');
	}
	else {
	  row.push_back('B');
	}
      }
      list<char>::iterator itr = row.begin();
      for(int l = 0;itr != row.end();itr++, l++) {
	martix[j][l] = *itr;
	cout<<martix[j][l];
      }
      cout<<endl;
    }
    bool red = false,blue = false;
    for (int j = n - 1; j >= 0; j --) {
      int countR =0; 
      int countB = 0;
      int count = 0;
      for (int l = 0; l < n; l ++) {
	if (martix[l][j] == 'R') {
	  count ++;
	  countB = 0;
	  countR ++;
	  if (countR == k) {
	    red = true;
	  }
	}
	else if (martix[l][j] == 'B') {
	  count ++;
	  countR = 0;
	  countB ++;
	  if (countB == k) {
	    blue = true;
	  }
	}
	else {
	  countR = 0;
	  countB = 0;
	}
      }
      if (count < k) break;
    }
    cout<<"red:"<<red<<"  blue:"<<blue<<endl;
    for (int j = n - 1; j >= 0; j --) {
      int countR =0; 
      int countB = 0;
      int count = 0;
      for (int l = 0; l < n; l ++) {
	if (martix[j][l] == 'R') {
	  count ++;
	  countB = 0;
	  countR ++;
	  if (countR == k) {
	    red = true;
	  }
	}
	else if (martix[j][l] == 'B') {
	  count ++;
	  countR = 0;
	  countB ++;
	  if (countB == k) {
	    blue = true;
	  }
	}
	else {
	  countR = 0;
	  countB = 0;
	}
      }
      if (count < k) break;
    }
    cout<<"red:"<<red<<"  blue:"<<blue<<endl;
    for (int j = 0; j < n; j ++) {
      int countR =0; 
      int countB = 0;
      int count = 0;
      for (int l = 0; l <= j; l ++) {
	if (martix[n-1-l][n-1-j+l] == 'R') {
	  count ++;
	  countB = 0;
	  countR ++;
	  if (countR == k) {
	    red = true;
	  }
	}
	else if (martix[n-1-l][n-1-j+l] == 'B') {
	  count ++;
	  countR = 0;
	  countB ++;
	  if (countB == k) {
	    blue = true;
	  }
	}
	else {
	  countR = 0;
	  countB = 0;
	}
      }
    }
    cout<<"red:"<<red<<"  blue:"<<blue<<endl;
    for (int j = 0; j < n; j ++) {
      int countR =0; 
      int countB = 0;
      int count = 0;
      for (int l = 0; l <= j; l ++) {
	if (martix[j-l][l] == 'R') {
	  count ++;
	  countB = 0;
	  countR ++;
	  if (countR == k) {
	    red = true;
	  }
	}
	else if (martix[j-l][l] == 'B') {
	  count ++;
	  countR = 0;
	  countB ++;
	  if (countB == k) {
	    blue = true;
	  }
	}
	else {
	  countR = 0;
	  countB = 0;
	}
      }
    }
    cout<<"red:"<<red<<"  blue:"<<blue<<endl;
    for (int j = 0; j < n; j ++) {
      int countR =0; 
      int countB = 0;
      int count = 0;
      for (int l = 0; l <= j; l ++) {
	if (martix[l][n-1-j+l] == 'R') {
	  count ++;
	  countB = 0;
	  countR ++;
	  if (countR == k) {
	    red = true;
	  }
	}
	else if (martix[l][n-1-j+l] == 'B') {
	  count ++;
	  countR = 0;
	  countB ++;
	  if (countB == k) {
	    blue = true;
	  }
	}
	else {
	  countR = 0;
	  countB = 0;
	}
      }
    }
    cout<<"red:"<<red<<"  blue:"<<blue<<endl;
    for (int j = 0; j < n; j ++) {
      int countR =0; 
      int countB = 0;
      int count = 0;
      for (int l = 0; l <= j; l ++) {
	if (martix[n-1-j+l][l] == 'R') {
	  count ++;
	  countB = 0;
	  countR ++;
	  if (countR == k) {
	    red = true;
	  }
	}
	else if (martix[n-1-j+l][l] == 'B') {
	  count ++;
	  countR = 0;
	  countB ++;
	  if (countB == k) {
	    blue = true;
	  }
	}
	else {
	  countR = 0;
	  countB = 0;
	}
      }
    }
    cout<<"red:"<<red<<"  blue:"<<blue<<endl<<endl;
    string rtn;
    if (red&&blue)
      rtn = "Both";
    else if (red)
      rtn = "Red";
    else if (blue)
      rtn = "Blue";
    else rtn = "Neither";
    ous<<"Case #"<< i + 1 << ": "<<rtn<<endl;
    //getchar();
  }
}





