#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <cctype>

using namespace std;

bool outOfRange(int rows,int cols,int i,int j){
  return (i<rows && j<cols)?false:true;
}

int main(){

  //freopen("A-small-attempt2.in","r",stdin);
  freopen("A-large.in","r",stdin);
  freopen("outA.txt","w",stdout);
	
  int cases;
  cin >> cases;

  for(int i=1;i<=cases;i++){
    cout << "Case #"<<i<<": ";

    int rows,cols;
    cin >> rows >> cols;

    char grid[50][50] = {'.'};
    
    for(int i=0;i<rows;i++){
      for(int j=0;j<cols;j++)
	cin >> grid[i][j];
      string s;
      getline(cin,s); // for new line
    }
    bool failed=false;
    for(int i=0;i<rows;i++){
      for(int j=0;j<cols;j++){
	if( grid[i][j] == '#' ){
	  if( outOfRange(rows,cols,i,j) || outOfRange(rows,cols,i+1,j) || outOfRange(rows,cols,i,j+1) || outOfRange(rows,cols,i+1,j+1)  ){
	    failed=true;
	    break;
	  }
	  
	  if( grid[i][j+1]!='#' || grid[i+1][j+1]!='#' || grid[i+1][j]!='#' ){
	    failed=true;
	    break;
	  }
	  
	  grid[i][j]=grid[i+1][j+1]='/';
	  grid[i][j+1]=grid[i+1][j]='\\';
	  j++;
	}
      }
      if(failed)
	break;
    }
    
    
    // print result
    if(failed)
      cout << endl << "Impossible" << endl;
    else{
      cout << endl;
      for(int i=0;i<rows;i++)
	for(int j=0;j<cols;j++)
	  cout << grid[i][j]<<((j==cols-1)?"\n":"");
    }
  }


  return 0;
}
