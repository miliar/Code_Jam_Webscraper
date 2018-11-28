#include <iostream>
#include <list>

using namespace std;

int main(void)
{
    int t;
    
    cin >> t;
    for (int i=0; i<t; i++)
    {
        int n;
        list<pair<char, int> > task_q;
        list<int> o_q;
        list<int> b_q;
        int o_pos = 1;
        int b_pos = 1;

        cin >> n;
        for (int j=0; j<n; j++)
        {
            pair<char, int> p;
            cin >> p.first;
            cin >> p.second;
            task_q.push_back(p);
            if (p.first == 'O')
                o_q.push_back(p.second);
            else
                b_q.push_back(p.second);
        }
        cout <<"Case #"<<i+1<<": ";
        int time = 0;
        while (!task_q.empty())
        {
            time ++;
            if (task_q.front().first == 'O')
            {
                if (o_pos == task_q.front().second)
                {
                    task_q.pop_front();
                    o_q.pop_front();
                }
                else
                {
                    if (o_pos > task_q.front().second)
                        o_pos --;
                    else
                        o_pos ++;
                }
                if (b_pos >b_q.front())
                    b_pos --;
                else if (b_pos < b_q.front())
                    b_pos ++;
            }
            else if (task_q.front().first == 'B')
            {
                if (b_pos == task_q.front().second)
                {
                    task_q.pop_front();
                    b_q.pop_front();
                }
                else
                {
                    if (b_pos > task_q.front().second)
                        b_pos --;
                    else
                        b_pos ++;
                }
                if (o_pos >o_q.front())
                    o_pos --;
                else if (o_pos < o_q.front())
                    o_pos ++;
            }
        }
        cout << time<<endl;
    }
    return 0;
}
