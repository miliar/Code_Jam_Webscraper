#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
  int T,N,S,p;
  cin >> T;
  bool surprising[] = {false,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,
    true,true,true,true,true,true,false,false};
  int biggestonsurprise[] = {0,0,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,0,0};
  int biggestonnonsurprise[] = {0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10};
  int result;
  for (int i = 1; i <= T; ++i)
  {
    result = 0;
    cin >> N >> S >> p;
    vector<int> total(N);
    for (int j = 0; j < N; ++j)
      cin >> total[j];
    sort(total.begin(),total.begin()+total.size());
    for (int j = total.size()-1; j >= 0; j--)
    {
      if (S)
      {
        if (biggestonnonsurprise[total[j]] >= p)
          result++;
        else if (surprising[total[j]])
        {
          S--;
          if (biggestonsurprise[total[j]] >= p)
            result++;
        }
      }
      else
      {
        if (biggestonnonsurprise[total[j]] >= p)
          result++;
      }
    }
    cout << "Case #" << i << ": " << result << endl;
  }
  return 0;
}
