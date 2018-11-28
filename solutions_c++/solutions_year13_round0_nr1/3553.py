#include <stdio.h>
#include <iostream>
#include <fstream>

// OPTIONAL
#include <math.h>
#include <limits.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main(int argc, const char *argv[])
{
  ifstream read("input.in");
  ofstream write;
  write.open ("output.out");
  // STARTS HERE

  int n;
  read >> n;
  char b_x[4][4], b_o[4][4], cur;
  bool x_w, o_w;

  for (int case_no = 1; case_no <= n; ++case_no) {
    bool end = true;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        read >> cur;
        if(cur=='.')
          end = false;
        if(cur=='T')
        {b_x[i][j] = 'X'; b_o[i][j] = 'O';}
        else
        {b_x[i][j] = b_o[i][j] = cur;}
      } // end for j 
    } // end for i 

    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        cout << b_x[i][j];
      } // end for j 
      cout << endl;
    } // end for i 
    cout << endl;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        cout << b_o[i][j];
      } // end for j 
      cout << endl;
    } // end for i 
    for (int i = 0; i < 4; ++i) {
      x_w = o_w = true;
      for (int j = 1; j < 4; ++j) {
        if(b_x[i][0]!=b_x[i][j] || b_x[i][j] != 'X')
        {x_w = false;}
        if(b_o[i][0]!=b_o[i][j] || b_o[i][j] != 'O')
        {o_w = false;}
      } // end for j 
      if(x_w || o_w)
      {
        cout << "break 1" << endl;
        break;
      }
    } // end for i 

    if(!x_w && !o_w)
      for (int i = 0; i < 4; ++i) {
        x_w = o_w = true;
        for (int j = 1; j < 4; ++j) {
          if(b_x[0][i]!=b_x[j][i] || b_x[j][i] != 'X')
          {x_w = false;}
          cout << b_o[0][i] << " " << b_o[j][i] << " "
            << j << " " << i << endl;
          if(b_o[0][i]!=b_o[j][i] || b_o[j][i] != 'O')
          {o_w = false;}
        } // end for j 
        if(x_w || o_w)
        {
          cout << "break 2" << endl;
          break;
        }
      } // end for i 

    if(!x_w && !o_w)
    {
      x_w = o_w = true;
      for (int j = 1; j < 4; ++j) {
        if(b_x[0][0]!=b_x[j][j] || b_x[j][j] != 'X')
        {x_w = false;}
        if(b_o[0][0]!=b_o[j][j] || b_o[j][j] != 'O')
        {o_w = false;}
      } // end for j 
      if(x_w || o_w)
      {
        cout << "break 3" << endl;
      }
    }

    if(!x_w && !o_w)
    {
      x_w = o_w = true;
      for (int j = 1; j < 4; ++j) {
        if(b_x[3][0]!=b_x[3-j][j] || b_x[3-j][j] != 'X')
        {x_w = false;}
        if(b_o[3][0]!=b_o[3-j][j] || b_o[3-j][j] != 'O')
        {o_w = false;}
      } // end for j 
      if(x_w || o_w)
      {
        cout << "break 4" << endl;
      }
    }

    // END HERE
    write << "Case #" << case_no << ": ";

    // ANSWER HERE
    if(x_w)
      write <<"X won\n";
    else if (o_w)
      write << "O won\n";
    else if(!end)
      write << "Game has not completed\n";
    else
      write << "Draw\n";

  } // end for case_no 
  return 0;
}
