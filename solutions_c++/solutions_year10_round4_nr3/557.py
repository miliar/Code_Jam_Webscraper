#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
using namespace std;

void proliferate(vector<vector<bool> > & arr) 
{
  
  for (int i=arr.size()-1;i>=1;i--) {

    for (int j=arr[i].size()-1;j>=1;j--) {

      if (arr[i][j] == true) {
	if (!arr[i][j-1] && !(arr[i-1][j])) {
	  arr[i][j] = false;
	};
      } else {
	if (arr[i][j-1] && (arr[i-1][j])) {
	  arr[i][j] = true;
	};	
      };

    };
    
  };

};

bool vazio (vector<vector<bool> > & arr) 
{

  for (int i=arr.size()-1;i>=1;i--) {
    for (int j=arr[i].size()-1;j>=1;j--) {

      if (arr[i][j]) {
	return false;
      };

    };
  };

  return true;

};

int main()
{

  int n;
  cin >> n;

  for (int cas=1;cas<=n;cas++) {

    
    int r;
    cin >> r;

    vector<vector<bool> > arr(101,vector<bool>(101,false));

    for (int i=0;i<r;i++) {
      int x1,x2,y1,y2;
      cin >> x1  >> y1 >> x2 >> y2;
      for (int j=x1;j<=x2;j++) {
	for (int k=y1;k<=y2;k++) {
	  arr[j][k] = true;
	};
      };
    };

    int count = 0;

    while (!vazio(arr)) {

      proliferate(arr);

      count++;

    };

    cout << "Case #"<<cas << ": " << count << endl;

  };

  return 0;

};
