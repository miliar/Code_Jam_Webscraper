#include <iostream>
#include <utility>
#include <map>
#include <string>
#include <list>
#include <vector>
#include <set>

typedef char robot;
typedef std::list<robot> robotlist_t;
typedef std::list<unsigned int> buttonlist_t;

void do_ai(robot rob, unsigned int& pos, bool &inc, bool mystep,
    unsigned int mybutton) {
  //std::cout << rob << " " << pos << " " << mybutton  << " ";
  bool did_step = false;
  if (pos < mybutton) {
    ++pos;
    did_step = true;
    //    std::cout << "+";
  } else if (pos > mybutton) {
    --pos;
    did_step = true;
    //std::cout << "-";
  }

  if (mystep && !did_step) {
    //std::cout << "press";
    inc = true;
  }
  if (!did_step && !inc) {
    //  std::cout << "stay";
  }
  //std::cout << "\n";
}

int main() {

  unsigned int T;
  std::cin >> T;

  for (unsigned int t = 0; t < T; ++t) {

    unsigned int N;
    std::cin >> N;

    robotlist_t order;
    buttonlist_t O_buttons;
    buttonlist_t B_buttons;

    for (unsigned int n = 0; n < N; n++) {
      char c;
      std::cin >> c;
      unsigned int b;
      std::cin >> b;
      order.push_back(c);
      if (c == 'O')
        O_buttons.push_back(b);
      else
        B_buttons.push_back(b);
    }

    robotlist_t::iterator step = order.begin();
    buttonlist_t::iterator O_step = O_buttons.begin();
    buttonlist_t::iterator B_step = B_buttons.begin();
    unsigned int O_pos = 1;
    unsigned int B_pos = 1;

    unsigned int time = 0;

    while (step != order.end()) {
      //std::cout << time << " ";
      bool incO = false, incB = false;
      if (O_step != O_buttons.end())
        do_ai('O', O_pos, incO, *step == 'O', *O_step);
      if (incO)
        ++O_step;

      if (B_step != B_buttons.end())
        do_ai('B', B_pos, incB, *step == 'B', *B_step);
      if (incB)
        ++B_step;

      if (incO || incB) {
        ++step;
      }
      ++time;
    }

    std::cout << "Case #" << t + 1 << ": " << time;

    std::cout << "\n";
  }

  return 0;
}
