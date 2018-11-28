#include <iostream>
#include <vector>
#include <cassert>

struct Button {
  Button() {}
  Button(char bo, int bu): bot(bo), button(bu) {}

  char bot;
  int button;
};

std::vector<Button> sequence;
std::vector<int> OSeq;
std::vector<int> BSeq;

int compute() {
  int ptr = 0;
  int Optr = 0;
  int Bptr = 0; // the next ones to hit

  int Oloc = 1;
  int Bloc = 1;

  int steps = 0;
  while(ptr < sequence.size()) {
    assert(Optr < OSeq.size() || Bptr < BSeq.size());
    steps++;

    const Button b = sequence[ptr];
    if(b.bot == 'O') {
      if(b.button == Oloc) {
	ptr++;
	Optr++;
      } else if(b.button < Oloc) {
	Oloc--;
      } else if(b.button > Oloc) {
	Oloc++;
      }

      if(Bptr < BSeq.size()) {
	if(BSeq[Bptr] < Bloc) {
	  Bloc--;
	} else if(BSeq[Bptr] > Bloc) {
	  Bloc++;
	}
      }
    } else if(b.bot == 'B') {
      if(b.button == Bloc) {
	ptr++;
	Bptr++;
      } else if(b.button < Bloc) {
	Bloc--;
      } else if(b.button > Bloc) {
	Bloc++;
      }

      if(Optr < OSeq.size()) {
	if(OSeq[Optr] < Oloc) {
	  Oloc--;
	} else if(OSeq[Optr] > Oloc) {
	  Oloc++;
	}
      }
    }
  }
  return steps;
}

int main()
{
  int T;
  std::cin >> T;
  for(int i=0;i<T;i++) {
    sequence.clear();
    OSeq.clear();
    BSeq.clear();

    int N;
    std::cin >> N;
    for(int j=0;j<N;j++) {
      char bot;
      std::cin >> bot;
      int button;
      std::cin >> button;
      sequence.push_back(Button(bot, button));
      if(bot == 'O')
	OSeq.push_back(button);
      else if(bot == 'B')
	BSeq.push_back(button);
      else
	assert(false);
    }

    int x = compute();
    std::cout << "Case #" << i+1 << ": " << x << "\n";
  }

  return 0;
}
