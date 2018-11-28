#include <cmath>
#include <cstdio>
#include <algorithm>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <utility>
#include <vector>
#include <deque>
#include <list>
#include <iostream>
#include <iomanip>
#include <stdint.h>



using namespace std;


string doCase(istream & in)
{
  ostringstream resultstr;
  int32_t N;
  in >> N;
  vector<int32_t> peakrefs;
  vector<int64_t> peakheights;
  for(int32_t i = 1; i < N; i++)
  {
    int32_t myi;
    in >> myi;
    peakrefs.push_back(myi);
  }

  int64_t last_height = 50000000ll;
  int64_t h = 50000000ll;
  peakheights.push_back(last_height);

  for(int32_t j = 1; j < N; j++)
  {
    int64_t  minval = 1ll;
    int64_t  maxval = 1000000000ll;
    maxval--;

    for(int32_t k = 0; k < j; k++)
    {
      int32_t visindex = peakrefs[k]-1;
      if(visindex > j)
      {
        if(j < (int) peakrefs.size())
          if(peakrefs[j]-1 > visindex)
            return "Impossible";
        continue;
      }
      else if(visindex == j)
      {
        //make this things minimum just taller than all in between as projected
        int32_t diff = j-k;
        for(int32_t kk = k+1; kk < j; kk++)
        {
          int32_t middiff = kk-k;
          int64_t kh = peakheights[k];
          int64_t kkh = peakheights[kk];
          int64_t hd = kkh-kh;
          int64_t projh = (((hd * diff)) / middiff) + 1 + kh; //rounded up projheight
          if (minval < projh)
          {
            //cout << "Minupdate:" << k << " " << kk << " " << j << endl;
            minval = projh;
          }
        }
      }
      else if(visindex < j)
      {
        //make this things maximum just shorter than projected peak
        int32_t diff = j-k;
        int32_t middiff = visindex-k;
        int64_t kh = peakheights[k];
        int64_t kkh = peakheights[visindex];
        int64_t hd = kkh-kh;
        int64_t projh;
        if (hd < 0)
        {
          projh = kh  + (((hd * diff)+1) / middiff)  - 1; //has to be exactly or smaller
        }
        else
        {
          projh = (((hd * diff)) / middiff) + kh ; //has to be exactly or smaller
        }
        if (maxval > projh)
          maxval = projh;
      }
    }
    if(minval > maxval)
    {
      /*for(uint32_t p= 0; p < peakheights.size(); p++)
      {
        if(p)
          cout << " ";
        cout << peakheights[p];
      }
      cout << endl;
      cout << minval << "," << maxval << endl;*/
      return "BAD Impossible";
    }


    if(j == (int)peakrefs.size())
      h = last_height;
    else
    {
      int32_t previ = peakrefs[j-1]-1;
      int32_t thisi = peakrefs[j]-1;
        
      if(previ == thisi)
      {
        h = last_height - 2000;
      }
      else if(previ > thisi)
      {
        h = last_height-6000;
      }
      else
      {
        h = last_height + 6000;
      }
    }


    if(h <= maxval && h >= minval)
    {
      //stay at the last height if it works
    }
    else if(minval > h)
    {
      h = minval;
    }
    else
    {
      h = maxval;
    }
    //cout << minval << "," << maxval << endl;
    peakheights.push_back(h);
    last_height = h;

  }
  for(uint32_t p= 0; p < peakheights.size(); p++)
  {
    if(p)
      resultstr << " ";
    resultstr << peakheights[p];
  }

  
  return resultstr.str();
}

int main() {
  uint64_t T;
  cin >> T;
  for (uint64_t Ti = 1; Ti <= T; ++Ti) {
    cout << "Case #" << Ti << ": " << doCase(cin) << endl;
  }
  return 0;
}
