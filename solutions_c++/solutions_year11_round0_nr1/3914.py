#include <iostream>
#include <string>
#include <cstdio>
#include <vector>

using namespace std ;

int blue_button_sequence[100] ;
int orange_button_sequence[100] ;
char button_push_sequence[200] ;

int blue_cnt ;
int orange_cnt ;
int push_count ;

int
main()
{
	int T = 0, N = 0;
	cin >> T ;
	for (int trial = 0; trial < T; ++trial)
	{
		cin >> N ;
		for (int i = 0; i < N; ++i)
		{
			char bot ;
			int seq ;
			cin >> bot >> seq ;
			button_push_sequence[push_count++] = bot ;
			if ( bot == 'O' || bot == 'o' )
			{
				orange_button_sequence[orange_cnt++] = seq ;
			}
			else if (bot == 'B' || bot == 'b')
			{
				blue_button_sequence[blue_cnt++] = seq ;
			}
		}
		int time = 0 ;
		int blue_pos = 1, blue_buttons_pushed = 0 ;
		int orange_pos = 1, orange_buttons_pushed = 0 ;
		int push = 0 ;
		while(true)
		{
		    if (blue_buttons_pushed < blue_cnt)
		    {
			    if ( blue_button_sequence[blue_buttons_pushed] == blue_pos)
			    {
				    if ( button_push_sequence[push] == 'B' )
				    {
					    ++blue_buttons_pushed ;
					    #ifdef _DEBUG
					    cout << "Blue: Push button " << blue_pos << endl;
					    #endif
				    }
				    else
				    {
					    #ifdef _DEBUG
					    cout << "Blue: Stay at " << blue_pos << endl ;
					    #endif
				    }
			    }
			    else if(blue_button_sequence[blue_buttons_pushed] < blue_pos)
			    {
                    --blue_pos ;
					    #ifdef _DEBUG
					    cout << "Blue: Move to " << blue_pos << endl ;
					    #endif
			    }
			    else
			    {
			        ++blue_pos ;
					    #ifdef _DEBUG
					    cout << "Blue: Move to " << blue_pos << endl;
					    #endif
			    }
            }

            if(orange_buttons_pushed < orange_cnt)
            {
			    if ( orange_button_sequence[orange_buttons_pushed] == orange_pos)
			    {
				    if ( button_push_sequence[push] == 'O' )
				    {
					    ++orange_buttons_pushed ;
					    #ifdef _DEBUG
					    cout << "Orange: Push button " << orange_pos << endl ;
					    #endif
				    }
				    else
				    {
					    #ifdef _DEBUG
					    cout << "Orange: Stay at " << orange_pos << endl;
					    #endif
				    }
			    }
			    else if(orange_button_sequence[orange_buttons_pushed] < orange_pos)
			    {
                    --orange_pos ;
					    #ifdef _DEBUG
					    cout << "Orange: Move to " << orange_pos << endl;
					    #endif
			    }
			    else
			    {
			        ++orange_pos ;
					    #ifdef _DEBUG
					    cout << "orange: Move to " << orange_pos << endl;
					    #endif
			    }
			}
			++time;
			push = blue_buttons_pushed + orange_buttons_pushed ;
			if(push == push_count) break;
		}
		push_count = 0 ;
		blue_cnt = 0 ;
		orange_cnt = 0 ;
		cout << "Case #" << trial + 1 << ": " <<  time << endl;
	}
}
