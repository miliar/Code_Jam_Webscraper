#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;

int L=0, TC, T, N;
int J=0;
char TEM;   
int NUM;

int main()
{
  scanf("%d",&TC);
  for (L;L<TC;L++)
  {
    int j = 0;
    vector<int> orange, blue;
    vector<char> order;
    for (scanf("%d ", &N);j<N;++j)
    {
      scanf("%c %d ",&TEM, &NUM);
      if (TEM == 'O')
      {
        //cout << "O" << " " << NUM << "|";
        order.push_back('O');
        orange.push_back(NUM);
      }
      else
      {
        //cout << "B" << " " << NUM << "|";
        order.push_back('B');
        blue.push_back(NUM);
      }
    }
    for (int i = 0; i<orange.size(); ++i)
    {
      //cout << orange[i] << " ";
    }

    // do something
    int time = 0;
    int bp = 0, op = 0;
    int O=1, B=1;
    for (int i = 0; i<order.size(); ++i)
    {
      bool push=0;
      while (!push)
      {
        if(blue.size())
        {
          if (blue[bp]>B)
            ++B;
          else if (blue[bp]<B)
            --B;
          else if (order[i] == 'B')
          {
            push = 1;
            ++bp;
          }
        }

        if(orange.size())
        {
          if (orange[op]>O)
            ++O;
          else if (orange[op]<O)
            --O;
          else if (order[i] == 'O')
          {
            push = 1;
            ++op;
          }
        }
        ++time;
      }
    }
    cout << "Case #" << L+1 << ": " << time << endl;
  }
}
