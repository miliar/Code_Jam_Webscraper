#include <iostream>
#include <vector>

using namespace std;

int main()
{

  int n;
  cin >> n;

  for (int c=1;c<=n;c++) {

    int k;
    cin >> k;
    int s;
    cin >> s;
    int p;
    cin >> p;

    vector<int> arr(k);
    vector<int> rests(k);
    for (int i=0;i<k;i++) {
      cin >> arr[i];
      rests[i] = arr[i]%3;
      arr[i]/=3;
      arr[i] += rests[i] ? 1 : 0;
    }

    int res = 0;

    for (int i=0;i<k;i++) {
      if (arr[i] >= p) {
        res++;
      } else {
        if (arr[i] > 0) {
          if (rests[i] != 1) {
            if ((arr[i] + 1) >= p) {
              if (s > 0) {
                s--;
                res++;
              }
            }
          }
        }
      }
    }

    cout << "Case #" << c << ": " << res << endl;

  }

}
