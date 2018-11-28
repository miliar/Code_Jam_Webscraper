#include <iostream>
#include <queue>

using namespace std;


int main()
{
    int num_test_cases = 0;
    cin >> num_test_cases;
    string junk;
    getline(cin, junk);

    for(int i = 1; i <= num_test_cases; i++)
    {
        int rides_per_day = 0, capacity = 0, num_groups = 0;
        cin >> rides_per_day >> capacity >> num_groups;
        getline(cin, junk);
        queue<int> groups;
        for(int j = 0; j < num_groups; j++)
        {
            int temp;
            cin >> temp;
            groups.push(temp);
        }
        getline(cin, junk);

        int total = 0;
        for(int j = 0; j < rides_per_day; j++)
        {
            int room_left = capacity;
            queue<int> on_board;
            while(groups.size() > 0 && room_left - groups.front() >= 0)
            {
                total += groups.front();
                room_left -= groups.front();
                on_board.push(groups.front());
                groups.pop();
            }

            while(on_board.size() > 0)
            {
                groups.push(on_board.front());
                on_board.pop();
            }
        }
        
        cout << "Case #" << i << ": " << total << "\n";
    }
    
    return 0;
}
