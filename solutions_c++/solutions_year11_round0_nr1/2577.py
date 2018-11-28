#include <iostream>
#include <cstdlib>

int main() {
    using namespace std;
    int T, N;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int last_position[2] = {1, 1};
        int last_time[2] = {0, 0};
        char bot_name;
        int bot_id, bot_position;
        int time = 0, add_time = 0;
        cin >> N;
        for (int j = 0; j < N; ++j) {
            cin >> bot_name >> bot_position;
            bot_id = (bot_name == 'O')? 0: 1; 
            add_time = abs(bot_position - last_position[bot_id]) - (time - last_time[bot_id]);
            time +=  ((add_time>0)? add_time: 0) + 1;
            last_position[bot_id] = bot_position;
            last_time[bot_id] = time;
        }
        cout << "Case #" << i + 1 << ": " << time << endl;
    }
}
