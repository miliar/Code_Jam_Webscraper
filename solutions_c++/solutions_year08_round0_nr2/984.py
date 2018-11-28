#include <iostream>
#include <string>
#include <cstdio>
#include <list>
#include <queue>

using namespace std;

int main()
{
    int num_of_cases;
    int count = 0;
    string line;
    getline(cin, line);
    num_of_cases = atoi(line.c_str());
    while(num_of_cases > count)
    {
        ++count;
        int delay, num_A = 0, num_B = 0;
        priority_queue<int, deque<int>, greater<int> > req_A, req_B, avail_A, avail_B;
        getline(cin, line);
        delay = atoi(line.c_str());
        getline(cin, line);
        sscanf(line.c_str(), "%d %d", &num_A, &num_B);
//        cout << "Delay, num_A, num_B are :" << delay <<", " << num_A <<", " << num_B << endl;
        int hour_Dep, hour_Arr, min_Dep, min_Arr;

        for(int i=0; i < num_A; ++i)
        {
            getline(cin, line);
            sscanf(line.c_str(), "%d:%d %d:%d", &hour_Dep, &min_Dep, &hour_Arr, &min_Arr);
            min_Dep += 60 * hour_Dep;
            min_Arr += 60 * hour_Arr;
            req_A.push(min_Dep);
            avail_B.push(min_Arr + delay);
        }

        for(int i=0; i < num_B; ++i)
        {
            getline(cin, line);
            sscanf(line.c_str(), "%d:%d %d:%d", &hour_Dep, &min_Dep, &hour_Arr, &min_Arr);
            min_Dep += 60 * hour_Dep;
            min_Arr += 60 * hour_Arr;
            req_B.push(min_Dep);
            avail_A.push(min_Arr + delay);
        }
        num_A = num_B = 0;

        while(req_A.size() && req_B.size())
        {
            if(req_A.top() < req_B.top())
            {
                ++num_A;
                if(avail_A.size())
                {
                    if(req_A.top() >= avail_A.top())
                    {
                        --num_A;
                        avail_A.pop();
                    }
                }
                req_A.pop();
            }
            else
            {
                ++num_B;
                if(avail_B.size())
                {
                    if(req_B.top() >= avail_B.top())
                    {
                        --num_B;
                        avail_B.pop();
                    }
                }
                req_B.pop();
            }
        }

        if(req_A.size())
        {
            while(req_A.size())
            {
                ++num_A;
                if(avail_A.size() && (req_A.top() >= avail_A.top()))
                {
                    --num_A;
                    avail_A.pop();
                }
                req_A.pop();
            }           
        }

        if(req_B.size())
        {
            while(req_B.size())
            {
                ++num_B;
                if(avail_B.size() && (req_B.top() >= avail_B.top()))
                {
                    --num_B;
                    avail_B.pop();
                }
                req_B.pop();
            }           
        }


        cout << "Case #" << count << ": " << num_A << " " << num_B << endl; 
    }
    return 0; 
}
