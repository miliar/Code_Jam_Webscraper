#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;
int main()
{
  int T; cin >> T;
  for (int now = 1; now <= T; ++now) {
    stringstream ss;
    ss << "Case #" << now << ": ";
    int N, S, p;
    cin >> N >> S >> p;
    int ans = 0, ans_dec = 0;
    for (int i = 0; i < N; ++i) {
      int max_one;
      int tmp;
      cin >> tmp;
      max_one = (tmp == 0) ? 0 : static_cast<int>(ceil(tmp / 3.0));
      if (max_one >= p) ans++;
      if (max_one == p - 1 && max_one != 0) ans_dec++;
    }
    ss << ans + min(ans_dec, S);
    // N: # of Googlers
    // S: # of suprsing triplet of scores
    // p:
    // N integers t_i (total points of the googlers)
    cout << ss.str() << endl;
    // ���Ĥ� total points -> suprising �ο���given ->
    // ���ʤ��Ȥ� p ����� maximum number
    // 3 1 5 ... 15 13 11 -> 3
    // 15/3=5, 5 5 5/ 13/3=4.33, 4 4 3/ 11/3=3.66 3 4 4
    // 2 ��������Ȥ����ʤ��Τ� not suprising �� 3 ��ʬ�Ϸ���Ū��
    // 15 13 11..
    // 15 ... 5 5 5
    // 13 ... 4 4 5
    // 11 ... 3 4 4
    // ���Τޤޤ��� 2 ������ 1 �Ĥ��� suprising ���䤻��. 5-1 �� max ��õ���ƥԥå�
    // ... Ans: 3
  }
}
