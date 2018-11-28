#include <iostream>
using namespace std;

#define INPUT_FILE "A.in.txt"
#define OUTPUT_FILE "A.out.txt"

#define DIFF(a,b) (a>b?a-b:b-a)

int main()
{
	freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
	
    int t, nbuttons, button;
    char last_robot, robot;
    int last_button[2];
    int res, time, irobot;
	
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cout << "Case #" << (i+1) << ": ";
		cin >> nbuttons;
		res = 0;
		time = 0;
		last_robot = '-';
		last_button[0] = 1;
		last_button[1] = 1;
		irobot = 1;
		for (int b = 0; b < nbuttons; b++)
		{
			cin >> robot >> button;
			if (robot != last_robot)
			{				
				res += time;
				irobot = !irobot;
				int diff = DIFF(button,last_button[irobot]) - time;				
				time = (diff<0?0:diff) + 1;
				last_robot = robot;	
			}
			else
			{			
				time += DIFF(button,last_button[irobot]) + 1;
			}
			last_button[irobot] = button;
		}
		res += time;
		cout << res << endl;
    }
	return 0;
}
