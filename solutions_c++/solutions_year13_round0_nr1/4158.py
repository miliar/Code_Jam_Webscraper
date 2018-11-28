//
//  main.cpp
//  googleCode
//
//  Created by Kirill on 13/04/2013.
//  Copyright (c) 2013 Kirill. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

fstream out;

bool gameCheck(int score, bool isT, int num)
{
  if (score == 4 || (score == 3 && isT))
  {
    out << "Case #" << num <<": X won" <<'\n';
    return true;
  }
  else if (score == -4 || (score == -3 && isT))
  {
    out << "Case #" << num <<": O won" <<'\n';
    return true;
  }
  return false;
}

void doit(int & score, bool & isT, bool & isDot, char a)
{
  if (a == 'X')
    ++score;
  else if (a == 'O')
    --score;
  else if (a == 'T')
    isT = true;
    else
      isDot = true;
}

void pro(vector<string> & v, int num)
{
  bool isDot = false;
  for (int i = 0; i < v.size();++i)
  {
    int score = 0;
    bool isT = false;
    for (int j = 0; j < v[i].size(); ++j)
    {
      doit(score, isT, isDot, v[i][j]);
    }
    if (gameCheck(score, isT, num))
      return;
  }
  //vertical
  for (int i = 0; i < v.size();++i)
  {
    int score = 0;
    bool isT = false;
    for (int j = 0; j < v[i].size(); ++j)
    {
      doit(score, isT, isDot, v[j][i]);
    }
    if (gameCheck(score, isT, num))
      return;
  }
  int score = 0;
  bool isT = false;
  for (int i = 0; i < 4; ++i)
  {
    doit(score, isT, isDot, v[i][i]);
  }
  if (gameCheck(score, isT, num))
    return;
  score = 0;
  isT = false;
  for (int i = 0; i < 4; ++i)
  {
      doit(score, isT, isDot, v[3-i][i]);
  }
  if (gameCheck(score, isT, num))
    return;
  if (isDot)
    out << "Case #" << num <<": Game has not completed" <<'\n';
  else
    out << "Case #" << num <<": Draw" <<'\n';
}

int main(int argc, const char * argv[])
{
  fstream myfile;
  out.open("out.txt");
  myfile.open ("A-large.in");
  int num;
  myfile >> num;
  for (int i = 0; i < num;++i)
  {
    string tmp;
    vector<string> v;
    for (int j = 0; j < 4; ++j)
    {
      myfile >> tmp;
      v.push_back(tmp);
      tmp.clear();
    }
    pro(v, i + 1);
  }
  myfile.close();
  out.close();
  return 0;
}

