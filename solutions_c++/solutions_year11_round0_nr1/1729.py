#include <iostream>
#include <queue>
using namespace std;

class Robot
{
public:
  int pos;
  queue<int> seq;

  Robot()
  {
    pos = 1;
  }
};

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t < T+1; ++t) {
    int N;
    cin >> N;

    Robot O, B;
    queue<char> color;
    for (int i = 0; i < N; ++i) {
      char c;
      int n;
      cin >> c >> n;
      if (c == 'O')
	O.seq.push(n);
      else
	B.seq.push(n);
      color.push(c);
    }

    int ans = 0;
    while (N) {
      if (color.front() == 'O' && O.pos == O.seq.front()) {
	color.pop();
	O.seq.pop();
	--N;

	if (B.pos > B.seq.front())
	  --B.pos;
	else if (B.pos < B.seq.front())
	  ++B.pos;
      } else if (color.front() == 'B' && B.pos == B.seq.front()) {
	color.pop();
	B.seq.pop();
	--N;

	if (O.pos > O.seq.front())
	  --O.pos;
	else if (O.pos < O.seq.front())
	  ++O.pos;
      } else {
	if (O.pos > O.seq.front())
	  --O.pos;
	else if (O.pos < O.seq.front())
	  ++O.pos;

	if (B.pos > B.seq.front())
	  --B.pos;
	else if (B.pos < B.seq.front())
	  ++B.pos;
      }
      ++ans;
    }

    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
