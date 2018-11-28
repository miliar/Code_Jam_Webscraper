#include <iostream>
#include <map>
#include <algorithm>
#include <sstream>
#include <vector>
#include <iomanip>
using namespace std;
double op1(const int a, const int b, const vector<double> p)
{
  double correct_prob = 1.0;
  for (int i = 0; i < p.size(); ++i) {
    correct_prob *= p.at(i);
  }

  return correct_prob * (b - a + 1) + (1.0 - correct_prob) * (b - a + b + 2);
}
/*

3 4
1 0.9 0.1
ans: 4.5

keep typing: 0.09*2 + 0.91*7 = 0.18 + 6.37
back1: 0.1*4 + 0.9*9 =
back2: 0.09*6 + 0.91*11
back3:
giveup: 6
*/

double op2(const int a, const int b, const vector<double> p)
{
  double exps = 999999999999999999;
  for (int i = 1; i <= a; ++i) {
    // 1, 2, 3
    double prev_correct_prob = 1.0;
    for (int j = 0; j < a-i; ++j) {
      prev_correct_prob *= p.at(j);
    }
    int num_correct = i * 2 + b - a + 1;
    double exp = prev_correct_prob * num_correct + (1 - prev_correct_prob) * (num_correct + b + 1);
    //cout << "> " << exp << endl;
        // (1.0 - back_correct_prob) * num_correct + (back_correct_prob) * (num_correct + b + 1);
    if (prev_correct_prob == 1.0) {
      exp = num_correct;
    }
    //    cout << ">><<" << exp << endl;
    exps = min(exp, exps);
  }
  return exps; // exp x a
}
double op3(const int a, const int b, const vector<double> p)
{
  double correct_prob = 1.0;
  for (int i = 0; i < p.size(); ++i) {
    correct_prob *= p.at(i);
  }

  if (correct_prob == 1.0) {
    return (b-a+1);
  }

  return 2+b;
}

int main()
{
  // 部分的に打ったが間違っているかもしれないケースの問題. insert でなく wrong char.
  // 1. そのまま打つ. のこりはパーフェクトの確率. 間違っていれば全て打ち直し
  // gu est[E]=4, est[E]guest[E]=10
  // 2. [B]uest[E]=6, 6, 
  // 3. 
  // 3. 一度クリア
  // gu [E(R)]guest[E]=7
  // might have pressed the wrong key while typing one or more of the previous characters

  // each char = 1 keystroke
  // each backspace = 1 keystroke
  // enter (attempt/giveup) = 1 keystroke

  // 最小化したい → keystroke の期待値
  // guest
  // ~~ で 40% のミスの可能性.
  // gu=0.6*0.6, gX=0.6*0.4, Xu=0.4*0.6, XX=0.4*0.4
  // gu est[ENTER] = 4
  // gX
  // guest 2 5. => 7
  // wrong prob.

  int sz, now = 1;
  cin >> sz;
  cin.ignore();

  string line;
  for (int sz_i = 0; sz_i < sz; ++sz_i) {
    int a, b;
    cin >> a >> b;
    vector<double> prob;
    for (int p_i = 0; p_i < a; ++p_i) {
      double p;
      cin >> p;
      prob.push_back(p);
    }

    //
    double expected = 999999999999999999;
    //cout << ">" << op1(a, b, prob) << endl;
    expected = min(op1(a, b, prob), expected);
    //cout << ">" << op2(a, b, prob) << endl;
    expected = min(op2(a, b, prob), expected);
    //cout << ">" << op3(a, b, prob) << endl;
    expected = min(op3(a, b, prob), expected);

    stringstream ss;
    ss << "Case #" << now++ << ": ";
    cout.setf(ios::showpoint);
    cout.setf(ios::fixed, ios::floatfield);
    cout << ss.str() << setprecision(6) << expected << endl;

  }
}
