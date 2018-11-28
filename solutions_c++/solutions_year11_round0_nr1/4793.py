#include <iostream>
#include <vector>
#include <utility>
#include <cmath>

using namespace std;

//[button][bot - 0 orange, 1 blue]sequence[][2];

vector<pair < char, int> > sequence;

int main()
{
    int num_cases, seq_length,button, curr_pos, time, spare, dist, delta;
    char bot, last_moved = 'a';
    cin >> num_cases;
    // cout << num_cases << endl;
    int orange, blue;
    for(int i  = 0; i < num_cases; i ++)
    {
        spare = 0;
        time = 0;
        orange = 1;
        blue = 1;
        cin >> seq_length;

        //read sequence
        for(int j = 0; j < seq_length; j++)
        {
            cin >> bot >> button;
            sequence.push_back(make_pair(button, bot));
        }

        //algorithm
        for(unsigned int j = 0; j < sequence.size(); j++)
        {
            //cout<<time<<endl;
            //cout<<"botovi su na pozicijama "<<orange<<" i "<<blue<<endl;
            bot = sequence[j].second;
            button = sequence[j].first;
            //cout<< "trenutno gledam "<<bot<<" na "<<button<<endl;
            if(bot == 'O')
            {
                curr_pos = orange;
            }
            else
            {
                curr_pos = blue;
            }



            dist = abs(button - curr_pos);
            //cout<<"pozicija je "<<curr_pos<<" ,a udaljenost "<<dist<<endl;
            if(last_moved != bot)
            {

                //cout<<"nije mican zadnji put"<<endl;
                if(spare >= dist)
                {
                    time++;
                    spare = 1;

                    if(bot == 'O')
                    {
                        orange = button;
                    }
                    else
                    {
                        blue = button;
                    }
                    //cout<<"vec je na mjestu"<<endl;
                    last_moved = bot;
                    continue;
                }
                delta = abs(dist - spare);
                if(delta < 0){
                    delta = 0;
                }
                spare = delta + 1;
                time += delta + 1;
                if(bot == 'O')
                {
                    orange = button;
                }
                else
                {
                    blue = button;
                }

                //continue;

            }
            else
            {
                time += dist + 1;
                spare += dist + 1;
                if(bot == 'O')
                {
                    orange = button;
                }
                else
                {
                    blue = button;
                }

            }





            last_moved = bot;

        }



        cout << "Case #"<<i+1<<": "<<time<<endl;
        sequence.clear();
    }
    return 0;
}
