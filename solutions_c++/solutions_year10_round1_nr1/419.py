#include <iostream>
#include <vector>
#include <string>
using namespace std;

string calc(vector<string> & arr, int k) {

  //  vector<vector<vector<int> > > re(4,vector<vector<int> >(arr.size(),vector<int>(arr.size(),0)));
  
  for (int i=0;i<arr.size();i++) {
    for (int j = arr[i].size() - 1;j>=0;j--) {
      for (int l=j+1;l<arr[i].size();l++) {
	if (arr[i][l] == '.') {
	  arr[i][l] = arr[i][l-1];
	  arr[i][l-1] = '.';
	} else {
	  break;
	};
      };
    };
  };

  bool r = false;
  bool b = false;

  for (int i=0;i<arr.size();i++) {
    char cur = '.';
    int size = 0;
    for (int j=0;j<arr.size();j++) {
      if (arr[i][j] != '.') {
	if (arr[i][j] == cur) {
	  size++;
	} else {
	  cur = arr[i][j];
	  size = 1;
	};
	if (size == k) {
	  if (cur == 'B') {
	    b = true;
	  } else {
	    r = true;
	  };
	};
      };
    };

    cur = '.';
    size = 0;
    for (int j=0;j<arr.size();j++) {
      if (arr[j][i] != '.') {
	if (arr[j][i] == cur) {
	  size++;
	} else {
	  cur = arr[j][i];
	  size = 1;
	};
	if (size == k) {
	  if (cur == 'B') {
	    b = true;
	  } else {
	    r = true;
	  };
	};
      };
    };

  };

  vector<int> re1(arr.size(),0);

  for (int j=0;j<arr.size();j++) {
    if (arr[0][j] != '.') {
      re1[j] = 1;
    } else {
      re1[j] = 0;
    };
  };
  for (int i=1;i<arr.size();i++) {
    vector<int> re3(arr.size(),0);
    if (arr[i][0] != '.') {
      re3[0] = 1;
    } else {
      re3[0] = 0;
    };
    for (int j=1;j<arr.size();j++) {
      if (arr[i][j] != '.') {
	if (arr[i][j] == arr[i-1][j-1]) {
	  re3[j] = re1[j-1] + 1;
	} else {
	  re3[j] = 1;
	};
	if (re3[j] == k) {
	  if (arr[i][j] == 'B') {
	    b = true;
	  } else {
	    r = true;
	  };
	};
      } else {
	re3[j] = 0;
      };
    };
    re1 = re3;
  };

  re1.clear();
  re1.resize(arr.size(),0);

  for (int j=0;j<arr.size();j++) {
    if (arr[0][j] != '.') {
      re1[j] = 1;
    } else {
      re1[j] = 0;
    };
  };
  for (int i=1;i<arr.size();i++) {
    vector<int> re3(arr.size(),0);
    if (arr[i][arr.size()-1] != '.') {
      re3[arr.size()-1] = 1;
    } else {
      re3[arr.size()-1] = 0;
    };
    for (int j=0;j<arr.size()-1;j++) {
      if (arr[i][j] != '.') {
	if (arr[i][j] == arr[i-1][j+1]) {
	  re3[j] = re1[j+1] + 1;
	} else {
	  re3[j] = 1;
	};
	if (re3[j] == k) {
	  if (arr[i][j] == 'B') {
	    b = true;
	  } else {
	    r = true;
	  };
	};
      } else {
	re3[j] = 0;
      };
    };
    re1 = re3;
  };  
  
  if (b) {
    if (r) {
      return "Both";
    } else {
      return "Blue";
    };
  } else {
    if (r) {
      return "Red";
    } else {
      return "Neither";
    };
  };

};

int main() 
{

  int n;
  cin >> n;

  for (int i=0;i<n;i++) {

    int m,k;
    cin >> m;
    cin >> k;

    vector<string> arr(m);
    
    for (int j=0;j<m;j++) {
	cin >> arr[j];
    };

    string res = calc(arr,k);

    cout << "Case #" << i+1 << ": " << res << endl;

  };

  return 0;

};
