#include <string>
#include <iostream>
#include<fstream>
using namespace std;

const string result[] = {"X won","O won","Draw","Game has not completed"};


int di2(char a[4][4])
{
  char ch = a[0][3];
  if(ch == 'T')
      ch = a[1][2];
  int j = 3;
  
  for(int i=0 ; i<4 ; ++i,--j)
  {
      if(a[i][j] == 'T')
		continue;
      if(a[i][j] != ch || a[i][j] == '.')
		return -1;
  }
  if(ch == 'O')
		return 1;
	return 0;

}


int coloums(char a[4][4],int j){
  char ch = a[0][j];
  if(ch == 'T')
      ch = a[1][j];
      
  for(int i=0 ; i<4 ; ++i)
  {
    if(a[i][j] == 'T')
		continue;
      if(a[i][j] != ch || a[i][j] == '.')
		return -1;
	}
	if(ch == 'O')
		return 1;
	return 0;
}
int row(char a[4][4],int i){
  char ch = a[i][0];
  if(ch == 'T')
      ch = a[i][1];
  for(int j=0 ; j<4 ; ++j){
    if(a[i][j] == 'T')
		continue;
      if(a[i][j] != ch || a[i][j] == '.')
		return -1;
  }
  if(ch == 'O')
		return 1;
	return 0;
}


int di1(char a[4][4])
{
  char ch = a[0][0];
  if(ch == 'T')
      ch = a[1][1];
      
  for(int i=0 ; i<4 ; ++i)
  {
    if(a[i][i] == 'T')
		continue;
      if(a[i][i] != ch || a[i][i] == '.')
		return -1;
  }
  
  if(ch == 'O')
		return 1;
	return 0;
	
}

int main(){
	ifstream in ("A-small-attempt1 (1).in");
	ofstream out ("first.txt");
  int t;
  in >> t;
  char a[4][4];
  for(int tc=1; tc<=t ; ++tc){
    int win = 0;
    bool flag = false;
    for(int i=0 ; i<4 ; ++i)
      for(int j=0 ; j<4 ; ++j)
		in >> a[i][j];
    for(int i=0 ; i<4 ; ++i){
      int a1 = row(a,i);
      if(a1 != -1){
		  out << "Case #" << tc << ": " << result[a1] << endl;
	  flag = true;
	  break;
      }
      a1 = coloums(a,i);
      if(a1 != -1){
	  out << "Case #" << tc << ": " << result[a1] << endl;
	  flag = true;
	  break;
      }
    }
    if(flag)
      continue;
    int a1 = di1(a);
    if(a1 != -1){
		out << "Case #" << tc << ": " << result[a1] << endl;
		continue;
    }
    a1 = di2(a);
    if(a1 != -1){
		out << "Case #" << tc << ": " << result[a1] << endl;
		continue;
    }
    a1 = 0;
    
    for(int i=0 ; i<4 ; ++i){
      for(int j=0 ; j<4 ; ++j){
			if(a[i][j] == '.'){
	  			a1 = 1;
	 			 break;
			}
    	}
    }
    if(a)
       out << "Case #" << tc << ": " << result[3] << endl;
    else
       out << "Case #" << tc << ": " << result[2] << endl;
  }
  return 0;
}
