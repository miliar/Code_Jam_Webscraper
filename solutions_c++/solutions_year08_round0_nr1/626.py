#include <algorithm>
#include <iostream>
#include <string>
#include <map>
using namespace std;

int NTest;
map<string,int> SlotName;
bool Mark[101];

int main()
{
  //freopen("input","rt",stdin);
  scanf("%d",&NTest);
  for(int test=1;test<=NTest;test++)
  {
    string buff;
    int NSlot,NAsk,Answer=0,UsedCount=0,input;
    SlotName.clear();
    scanf("%d ",&NSlot);
    fill(Mark,Mark+NSlot,false);
    for(int q=0;q<NSlot;q++)
    {
      getline(cin,buff);
      SlotName[buff]=q;
    }
    scanf("%d ",&NAsk);
    for(int q=0;q<NAsk;q++)
    {
      getline(cin,buff);
      input=SlotName[buff];
      if(!Mark[input])
      {
	UsedCount++;
	Mark[input]=true;
      }
      if(UsedCount==NSlot)
      {
	UsedCount=1;
	Answer++;
	fill(Mark,Mark+NSlot,false);
	Mark[input]=true;
      }
    }
    printf("Case #%d: %d\n",test,Answer);
  }
  return 0;
}
