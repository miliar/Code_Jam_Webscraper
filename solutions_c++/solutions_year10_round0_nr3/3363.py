#include <queue>
#include <iostream>

using namespace std;

int main()
{
  unsigned int CASES;
  cin >> CASES;

  for (unsigned int k = 0; k < CASES; ++k) {
    unsigned long money = 0;

    unsigned int RIDES, CAPACITY, GROUPS;
    cin >> RIDES >> CAPACITY >> GROUPS;

    queue<unsigned int> line;
    queue<unsigned int> rollercoaster;

    for (unsigned int g = 0; g < GROUPS; g++) {
      unsigned int group_size;
      cin >> group_size;
      line.push(group_size);
    }

    for (unsigned int ride = 0; ride < RIDES; ride++) {
      //cout << "ride " << (ride + 1) << endl;
      unsigned int cap_so_far = 0;
      
      bool accepting = true;
      while (accepting) {
        if (line.empty()) {
          break;
        }

        unsigned int group = line.front();

        if (cap_so_far + group <= CAPACITY) {
          line.pop();
          rollercoaster.push(group);
          //cout << "accepting a group of size " << group << " (CAP: " << CAPACITY << ")" << endl;
          money += group;
          cap_so_far += group;
        } else {
          accepting = false;
        }
      }

      while(!rollercoaster.empty()) {
        unsigned int p = rollercoaster.front();
        line.push(p);
        rollercoaster.pop();
      }
    }
    cout << "Case #" << (k + 1) << ": " << money << endl;
  }
}
