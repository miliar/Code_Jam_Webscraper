#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;


struct CheckPoint
{
 bool isO_;
 int  pos_;
};


int main_(int iTest)
{

int count = 0;
cin >> count;

vector<CheckPoint> vCheck(count);
vector<long> vTime(count);

for(int i = 0; i < count; ++i)
{
char c;
int n;
cin >> c;
cin >> n;

vCheck[i].isO_ = c == 'O';
vCheck[i].pos_ = n;
}

bool IsFirstSwitch = true;
int PrevSwitchIndex = -1;

vTime[0] = vCheck[0].pos_ - 1 + 1;

//cout << vTime[0] << endl;

for(int i = 1; i < vCheck.size(); ++i)
{

if(vCheck[i-1].isO_ != vCheck[i].isO_)
{
  CheckPoint Prev;
  long preTime = 0;
  if(PrevSwitchIndex == -1)
  {
    Prev.pos_ = 1;
  }
  else
  {
    Prev = vCheck[PrevSwitchIndex];
    preTime = vTime[PrevSwitchIndex];
  }

  vTime[i] = max(vTime[i-1] + 1, preTime + abs(Prev.pos_- vCheck[i].pos_) + 1);

  PrevSwitchIndex = i-1;
}
else
{
  vTime[i] = vTime[i-1] + abs(vCheck[i].pos_ - vCheck[i-1].pos_) + 1;
}

  //cout << vTime[i] << endl;

}

printf("Case #%d: %ld\n", iTest, vTime.back());

}


int main()
{

int nTest = 0;
cin >> nTest;

for(int i = 0; i < nTest; ++i)
{
main_(i+1);
}


return 0;
}
