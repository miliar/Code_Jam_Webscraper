#include <iostream>
#include <algorithm>

namespace CodeJam {
  namespace BotTrust {
    int abs(int value) {
      return value < 0 ? -value : value;
    }

    class Bot {
    public:
      Bot(): position(1), time(0) {
      }

      void addTime(int time) {
	this->time += time;
      }

      int push(int position) {
	int time = std::max(0, abs(this->position - position) - this->time) + 1;

	this->time = 0;
	this->position = position;
	
	return time;
      }

    private:
      int position;
      int time;
    };

    class Task {
    public:
      int solve(Bot& orange, Bot& blue) {
	int time;

	if(bot == 'O') {
	  time = orange.push(button);
	  blue.addTime(time);
	} else {
	  time = blue.push(button);
	  orange.addTime(time);
	}

	return time;
      }

    private:
      char bot;
      int button;

      friend std::istream& operator>>(std::istream&, Task&);
    };

    std::istream& operator>>(std::istream& is, Task& t) {
      return is >> t.bot >> t.button;
    }    

    void solveCase(int c) {
      int time = 0;
      Bot orange, blue;

      int n; 
      std::cin >> n;
      
      for(int i = 0; i < n; i++) {
	Task task;
	std::cin >> task;

	time += task.solve(orange, blue);
      }

      std::cout << "Case #" << c << ": " << time << std::endl;
    }

    void solveAll() {
      int k; std::cin >> k;

      for(int i = 1; i <= k; i++) {
	solveCase(i);
      }
    }
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);

  CodeJam::BotTrust::solveAll();

  return 0;
}
