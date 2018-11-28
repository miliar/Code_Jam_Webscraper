/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/12/13 22:52:11
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */
#include <iostream>
#include <fstream>
#include <string.h>
#include <iomanip>


using namespace std;

const int maxlen = 200;

bool checkrow(char p, char s[5][5], int x,int y, int dx, int dy)
{
  int i;
  for (i = 0;i < 4;i ++)
  	if (s[x + dx * i][y + dy * i] != p && s[x + dx * i][y+dy*i] != 'T')
	  return false;
  return true;
}

bool check(char p, char s[5][5])
{
	int i,j;
	for (i = 0;i < 4;i ++) {
	  if (checkrow(p,s,i,0,0,1) || checkrow(p,s,0,i,1,0))
	  return true;
	}
	if (checkrow(p,s,0,0,1,1) || checkrow(p,s,3,0,-1,1))
		return true;
	return false;
}


bool complete(char s[5][5])
{
  int i,j;
  for (i = 0;i < 4;i ++)
  	for (j = 0;j < 4;j ++)
	if (s[i][j] == '.')
		return false;
  return true;
}

const char* result[4] = {"X won","O won","Draw" ,"Game has not completed" };
int main(int argc, char ** argv)
{
	fstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);

    char empty[5];
	char s[5][5];
	int n,i,j,ans;
	fin >> n;
    fin.getline(empty,5);
	for (i = 1;i <= n;i++)
	{
		for (j =0;j <4;j ++)
			fin.getline(s[j],5);
		fin.getline(empty,5);
        int k;
	    for (j =0;j < 4;j ++)
        {
            for (k = 0;k <= 4;k ++)
                cout << s[j][k];
             cout << endl;
         }
		fout << "Case #" << i << ": ";
		if (check('X',s))
			ans = 0;
		 else 
		 if (check('O',s))
		 	ans = 1;
			else if (complete(s))
				ans = 2;
				else ans = 3;
		fout << result[ans] << endl;
	
	}

	fin.close();
	fout.close();
	return 0;
}
