#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int lines;
    cin >> lines;
    for (int i = 0; i < lines; i++) {
        int rounds, capacity, groups;
        cin >> rounds >> capacity >> groups;
        queue<int> visitors;
        int temp;
        for (int j = 0; j < groups; j++) {
            cin >> temp;
            visitors.push(temp);
        }
        int money = 0;
        for (int j = 0; j < rounds; j++) {
            int place = capacity;
            for (int k = 0; k < groups; k++) {
                if (!visitors.empty() && visitors.front()<=place) {
                    money += visitors.front();
                    place -= visitors.front();
                    visitors.push(visitors.front());
                    visitors.pop();
                } else {
                    break;
                }
            }
        }
        cout << "Case #" << i+1 << ": " << money << "\n";
    }

    return 0;
}
