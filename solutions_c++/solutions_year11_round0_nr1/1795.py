#include <iostream>
#include <vector>

int main()
{
  bool blue[100];
  int button[100];
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    std::cin >> N;
    for (int n = 0; n < N; ++n) {
      char B;
      std::cin >> B;
      blue[n] = B == 'B';
      std::cin >> button[n];
    }

    int b = 1;
    int o = 1;
    int tot_time = 0;
    int time_b = 0;
    int time_o = 0;
    for (int n = 0; n < N; ++n) {
      int x = blue[n] ? b : o;
      int cur_time = x - button[n];
      if (cur_time < 0)
	cur_time = -cur_time;
      if (blue[n]) {
	cur_time -= time_b;
	if (cur_time < 0)
	  cur_time = 0;
	time_b = 0;
	++cur_time;
	time_o += cur_time;
	b = button[n];
      } else {
	cur_time -= time_o;
	if (cur_time < 0)
	  cur_time = 0;
	time_o = 0;
	++cur_time;
	time_b += cur_time;
	o = button[n];
      }
      tot_time += cur_time;
    }

    std::cout << "Case #" << t << ": " << tot_time << std::endl;
  }
}
