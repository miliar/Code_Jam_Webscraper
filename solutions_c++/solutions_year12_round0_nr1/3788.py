/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/14/2012 18:21:16
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

int main(int argc, char ** argv)
{
  int i,j;
  char maps[26];
  bool check[26];
  string eg[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
  string ego[3] = {"our language is impossible to understand",
  	"there are twenty six factorial possibilities","so it is okay if you want to just give up"};

  for (i = 0;i < 26;i ++)
    check[i] = true;
  for (i = 0;i < 3;i ++)
    for (j = 0;j < eg[i].length(); j++) 
	  if (ego[i][j] != ' ')
	  {
	  maps[eg[i][j] - 'a'] = ego[i][j];

//	  cout << ego[i][j] -'a' << endl;
	  check[eg[i][j] - 'a'] = false;
	}
  maps[25] = 'q';
  maps['q' - 'a'] = 'z';
  check['q' - 'a' ] =false;
  check['z' - 'a' ] = false;
  for (i = 0;i < 26;i ++)
    cout << (char)('a' + i) << " " <<  maps[i]<< endl;
 

  for (i = 0;i < 26;i ++)
    if (check[i]) {
//	  cout << (char)('a' + i) << endl;
	}


	fstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);
	int n;
	char s[maxlen];
	fin >> n;
		fin.getline(s,200);
	//cout << n << endl;
	for (i = 1;i <= n;i ++)
	{
				
		fin.getline(s,200);
		fout << "Case #" << i << ": ";
		int len = strlen(s);
		cout << len << endl;
		for (j = 0;j < len; j ++) 
		  if (s[j] != ' ') 
		  {
		  fout << maps[s[j] - 'a'];
		  } else {
		    fout << s[j];
		  }
		fout << endl;
	}
	fin.close();
	fout.close();
  return 0;
}
