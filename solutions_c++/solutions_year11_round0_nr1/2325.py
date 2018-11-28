#include <iostream>
#include <queue>


const int MAX_BUTTONS=1000;

using namespace std;

//Orange == 0
//Blue == 1

int main ()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests_count;
    cin >> tests_count;
    
    for (int test_num=0; test_num<tests_count; test_num++)
    {
        char robot_color[MAX_BUTTONS];
        int button_num[MAX_BUTTONS];
        
        int buttons_count;
        cin >> buttons_count;
        for (int i=0; i<buttons_count; i++)
            cin >> robot_color[i] >> button_num[i];
        
        int orange_position=1;
        int blue_position=1;
        
        int orange_last_time=0;
        int blue_last_time=0;
        
        for (int i=0; i<buttons_count; i++)
        {
            if (robot_color[i]=='O')
            {
                orange_last_time=max(orange_last_time+abs(orange_position-button_num[i])+1, blue_last_time+1);
                orange_position=button_num[i];
            }
            else
            {
                blue_last_time=max(blue_last_time+abs(blue_position-button_num[i])+1, orange_last_time+1);
                blue_position=button_num[i];
            }
        }
        cout << "Case #" << test_num+1 << ": " << max(orange_last_time, blue_last_time) << endl;
    }
    
    return 0;
}

