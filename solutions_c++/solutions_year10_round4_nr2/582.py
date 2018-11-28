#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
using namespace std;


int main()
{

  int n;

  cin >> n;

  for (int cas =1;cas<=n;cas++) {

    int p;
    cin >> p;
   
    vector<int> arr((1<<p),0);

    vector<vector<int> > calcarr2(arr.size(),vector<int> (p+1,-1));

    for (int i=0;i<arr.size();i++) {
      cin >> arr[i];
      calcarr2[i][arr[i]] = 0;
    };

    for (int i = arr.size()/2;i>0;i/=2) {

      vector<vector<int> > calcarr(arr.size(),vector<int> (p+1,-1));
      
      for (int j=0;j<i;j++) {
	int min = -1;
	int nul;
	cin >> nul;
	for (int k=0;k<=p;k++) {

	  int min = -1;
	  //	  calcarr2[j*2-1][k];
	  if (calcarr2[j*2][k] >= 0) {
	    for (int l=k;l<=p;l++) {
	      if (calcarr2[j*2+1][l] >= 0) {
		if (min == -1) {
		  min = calcarr2[j*2+1][l] + calcarr2[j*2][k] + nul;
		} else {
		  if (calcarr2[j*2+1][l] + calcarr2[j*2][k] + nul < min) {
		    min = calcarr2[j*2+1][l] + calcarr2[j*21][k] + nul;
		  };
		};
	      };
	    };
	  };
	  
	  if (calcarr2[j*2][k+1] >= 0) {
	    for (int l=k+1;l<=p;l++) {
	      if (calcarr2[j*2+1][l] >= 0) {
		if (min == -1) {
		  min = calcarr2[j*2+1][l] + calcarr2[j*2][k+1];
		} else {
		  if (calcarr2[j*2+1][l] + calcarr2[j*2][k+1] < min) {
		    min = calcarr2[j*2+1][l] + calcarr2[j*2][k+1];
		  };
		};
	      };
	    };
	  };
	  
	  if (calcarr2[j*2+1][k] >= 0) {
	    for (int l=k;l<=p;l++) {
	      if (calcarr2[j*2][l] >= 0) {
		if (min == -1) {
		  min = calcarr2[j*2][l] + calcarr2[j*2+1][k] + nul;
		} else {
		  if (calcarr2[j*2][l] + calcarr2[j*2+1][k] + nul < min) {
		    min = calcarr2[j*2][l] + calcarr2[j*2+1][k] + nul;
		  };
		};
	      };
	    };
	  };
	  
	  if (calcarr2[j*2+1][k+1] >= 0) {
	    for (int l=k+1;l<=p;l++) {
	      if (calcarr2[j*2][l] >= 0) {
		if (min == -1) {
		  min = calcarr2[j*2][l] + calcarr2[j*2+1][k+1];
		} else {
		  if (calcarr2[j*2][l] + calcarr2[j*2+1][k+1] < min) {
		    min = calcarr2[j*2][l] + calcarr2[j*2+1][k+1];
		  };
		};
	      };
	    };
	  };

	  calcarr[j][k] = min;

	};	
	
      };

      calcarr2 = calcarr;

    };
    
    int min = 1024*1000000;

    for (int l=0;l<=p;l++) {
      if (calcarr2[0][l] >= 0) {
	if (min > calcarr2[0][l]) {
	  min = calcarr2[0][l];
	};
      };
    };

    cout << "Case #" << cas << ": " << min << endl;

  };

  return 0;

};
