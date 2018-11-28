#include <iostream>
#include <string>
#include <vector>

using namespace std;

char waterflow(const vector<vector<int> >& alts, vector<string>& res, int startx, int starty, char newlabel, char contlabel)
{
  int H = alts.size();
  int W = alts.front().size();

  int xw = startx;
  int yw = starty;

  do
  {
    res[yw][xw] = newlabel;

    int lowest = alts[yw][xw];

    int newxw = xw;
    int newyw = yw;
    
    if (yw > 0 && alts[yw-1][xw] < lowest)
    {
      lowest = alts[yw-1][xw];
      newxw = xw;
      newyw = yw-1;
    }
    if (xw > 0 && alts[yw][xw-1] < lowest)
    {
      lowest = alts[yw][xw-1];
      newxw = xw-1;
      newyw = yw;
    }
    if (xw < W-1 && alts[yw][xw+1] < lowest)
    {
      lowest = alts[yw][xw+1];
      newxw = xw+1;
      newyw = yw;
    }
    if (yw < H-1 && alts[yw+1][xw] < lowest)
    {
      lowest = alts[yw+1][xw];
      newxw = xw;
      newyw = yw+1;
    }

    xw = newxw;
    yw = newyw;
  }
  while(res[yw][xw] == contlabel);

  return res[yw][xw];
}

int main()
{
  int T = 0;
  cin >> T;
  
  for(int i = 0; i < T; ++i)
  {
    int H = 0;
    int W = 0;
    cin >> H >> W;

    vector<vector<int> > alts(H);

    for (int y = 0; y < H; ++y)
    {
      for (int x = 0; x < W; ++x)
      {
        int t;
        cin >> t;
        alts[y].push_back(t);
      }
    }

    vector<string> res(H, string(W, '0'));
    char nextLabel = 'a';

    for (int y = 0; y < H; ++y)
    {
      for (int x = 0; x < W; ++x)
      {
        if (res[y][x] != '0')
        {
          continue;
        }

        char waterstop = waterflow(alts, res, x, y, nextLabel, '0');

        if (waterstop != nextLabel)
        {
          waterflow(alts, res, x, y, waterstop, nextLabel);
        }
        else
        {
          ++nextLabel;
        }
      }
    }

    cout << "Case #" << (i + 1) << ":" << endl;
    for (int y = 0; y < H; ++y)
    {
      cout << res[y][0];
      for (int x = 1; x < W; ++x)
      {
        cout << ' ' << res[y][x];
      }
      cout << endl;
    }
  }
  
  return 0;
}

