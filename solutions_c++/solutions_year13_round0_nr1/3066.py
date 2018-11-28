#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <utility>
#include <algorithm> // sort, max_element, random_shuffle, remove_if, lower_bound 
#include <functional>
#include <fstream>
using namespace std;
char a[4][4];
int main()
{
  int test_cases;
  ifstream fin;
  fin.open("A-large.txt");
  fin>>test_cases;
  int nums;
  int j=1;
  ofstream fout;
  fout.open("output.txt");
  int num=1;
  while(test_cases>0)
  {
    int ans=-1;
    int dotn=0;
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
         fin>>a[i][j];
      int cnt1=0,cnt2=0;

    for(int i=0;i<4;i++)
    { 
      cnt1=0;
      cnt2=0;

      for(int j=0;j<4;j++)
        if(a[i][j]=='X')
          cnt1++;
        else if(a[i][j]=='O')
          cnt2++;
        else if(a[i][j]=='T')
        {
          cnt1++;
          cnt2++;
        }
        else
          dotn++;
      if(cnt1==4)
        ans = 0;
      if(cnt2==4)
        ans = 1;
    }
    if(ans==-1)
    {
    for(int j=0;j<4;j++)
    {
            cnt1=0;
      cnt2=0;

      int cnt1=0,cnt2=0;
      for(int i=0;i<4;i++)
        if(a[i][j]=='X')
          cnt1++;
        else if(a[i][j]=='O')
          cnt2++;
        else if(a[i][j]=='T')
        {
          cnt1++;
          cnt2++;
        }
        else
          dotn++;
      if(cnt1==4)
        ans = 0;
      if(cnt2==4)
        ans = 1;
    }

    }
          cnt1=0;
      cnt2=0;

    if(ans==-1)
    for(int i=0;i<4;i++)
    {
        if(a[i][i]=='X')
          cnt1++;
        else if(a[i][i]=='O')
          cnt2++;
        else if(a[i][i]=='T')
        {
          cnt1++;
          cnt2++;
        }
        else
          dotn++;
    }
          if(cnt1==4)
        ans = 0;
      if(cnt2==4)
        ans = 1;

          cnt1=0;
      cnt2=0;

    if(ans==-1)
    for(int i=0;i<4;i++)
    {
        if(a[i][3-i]=='X')
          cnt1++;
        else if(a[i][3-i]=='O')
          cnt2++;
        else if(a[i][3-i]=='T')
        {
          cnt1++;
          cnt2++;
        }
        else
          dotn++;
    }
          if(cnt1==4)
        ans = 0;
      if(cnt2==4)
        ans = 1;
    fout<<"Case #"<<num++<<": ";
    if(ans==0)
      fout<<"X won"<<endl;
    else if(ans==1)
      fout<<"O won"<<endl;
    else if(dotn==0)
      fout<<"Draw"<<endl;
    else
      fout<<"Game has not completed"<<endl;
    test_cases--;
  }
  return 0;
}