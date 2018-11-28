#include<assert.h>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>
#include<cstring>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf

class TargetHolder
{
  public:
  int curPos;
  vector<int> target;

  TargetHolder()
  {
      target.clear();
      curPos = 1;
  }
  void SetCurPos(int dist)
  {
    if ( target.size() == 0) re;
    int toMove = abs(target[0]-curPos);
    if ( dist>=toMove)
        curPos = target[0];
    else
        curPos = curPos + dist* ((target[0]-curPos)>0?1:-1);

  }
  int GetMoveVal(int nextPos)
  {
     int retVal = abs(nextPos - curPos);
     curPos = nextPos;
     target.erase(target.begin()); // remove from target
     re retVal;
  }
};

int main()
{
 //freopen("sample.in","r",stdin);
 freopen("a.in","r",stdin);
 freopen("a.ans","w",stdout);

 int t;
 sf("%d",&t);
 int kase=1;
 while (t--)
 {
     TargetHolder orange,blue;

     vector<int> mainTarget;
     int n;
     sf("%d",&n);

     while  ( n--)
     {
         char name[10];
         int target;
         sf("%s %d",name,&target);
         if ( name[0] == 'O')
            orange.target.pb(target), mainTarget.pb(-target);
        else
            blue.target.pb(target), mainTarget.pb(target);
     }

     int sum=0;
     int i;
     for(i=0;i<mainTarget.size();i++)
     {
        int retVal;
        if ( mainTarget[i] < 0 )
            retVal= orange.GetMoveVal(abs(mainTarget[i])), blue.SetCurPos(retVal+1);
        else
            retVal = blue.GetMoveVal(abs(mainTarget[i])), orange.SetCurPos(retVal+1);
        sum += retVal;
        sum++;
     }
     pf("Case #%d: %d\n",kase++,sum);
 }
 return 0;
}
