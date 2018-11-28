#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int n;
vector<char> let;
vector<int> num;
vector<int> os, bs;
int but_o, but_b, pos_o, pos_b, pos, _time;


void atualiza_b()
{
  if(bs.size() > 0)
     if(bs[pos_b] > but_b) but_b++;
     else if(bs[pos_b] < but_b) but_b--;
}

void atualiza_o()
{
  if(os.size() > 0)
     if(os[pos_o] > but_o) but_o++;
     else if(os[pos_o] < but_o) but_o--;
}


int main(void)
{

  int N;
  cin >> N;

  for(int c=1; c<=N; c++)
  {

    cin >> n;
    let.clear();
    num.clear();
    os.clear();
    bs.clear();

    for(int i = 0; i < n; i++)
    {
      char c;
      int k;
      cin >> c >> k;
      num.push_back(k);
      let.push_back(c);
      if(c == 'O') os.push_back(k);
      else bs.push_back(k);
    }

    but_o=but_b=1; 
    pos_o=pos_b=pos=_time=0;

    while(pos < num.size())
    {
      _time++;
      if(let[pos] == 'O' && but_o == num[pos])
      {
        pos++;
        pos_o++;
        atualiza_b();
     }
      else if(let[pos] == 'B' && but_b == num[pos])
      {
        pos++;
        pos_b++;
        atualiza_o();
      }
      else
      {
        atualiza_b();
        atualiza_o();
      }
    }

    printf("Case #%d: %d\n",c,_time);
  }
  return 0;
}
