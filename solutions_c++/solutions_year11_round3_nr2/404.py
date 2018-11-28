#include<string.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include <functional>
using namespace std;
main()
{
  int i, j, k, n, total_case;
  cin >> total_case;
  int L, N, C;
  long long t;
  for (int which_case = 1; which_case <= total_case; which_case++) {
    cin >> L >> t >> N >> C;
    vector < int >vc(C);
    for (i = 0; i < C; i++)
      cin >> vc[i];
    //cout<<L<<","<<t<<","<<N<<","<<C<<endl;
    //for(i=0;i<C;i++)cout << vc[i]<<endl;
    vector < int >vn(N);
    i = 0;
    j = 0;
    do {
      vn[i++] = vc[j++];
      if (i == N)
        break;
      if (j == C)
        j = 0;
    } while (1);
    //for(i=0;i<N;i++)cout << vn[i]<<endl;
    long long a = 0;                  //时间
    long long bjsj = 0;
    int cnt = 0;
    for (i = 0; i < N; i++) {
      a += (vn[i] * 2);
      if (a < t)
        continue;
      vector < int >vtmp;
      if (a == t) {
        for (j = i + 1; j < N; j++)
          vtmp.push_back(vn[j]);
        sort(vtmp.begin(), vtmp.end(), greater < int >());
        for (j = 0; j < vtmp.size(); j++) {
          if(L==0)break;
          bjsj += vtmp[j];
          cnt++;
          if (cnt >= L)
            break;
        }
        break;
      }
      if (a > t) {
        for (j = i + 1; j < N; j++)
          vtmp.push_back(vn[j]);
        vtmp.push_back((a - t) / 2);
        sort(vtmp.begin(), vtmp.end(), greater < int >());
        for (j = 0; j < vtmp.size(); j++) {
          if(L==0)break;
          bjsj += vtmp[j];
          cnt++;
          if (cnt >= L)
            break;
        }
        break;
      }
    }
    long long total = 0;
    for (i = 0; i < N; i++) {
      total += vn[i];
    }
    long long result = 0;
    result = total * 2 - bjsj;
    //cout << bjsj << endl;
    cout << "Case #" << which_case << ": " << result << endl;
  }
}
