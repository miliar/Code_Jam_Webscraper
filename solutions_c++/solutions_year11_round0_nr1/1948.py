#include <iostream>
#include <string>
#include <cstdio>


using namespace std;



int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for(int i = 0; i < t; ++i)
    {
        int n;
        cin >> n;
        int cuTime = 0;
        int lastO  = 1, timeO = 0, lastB = 1, timeB = 0;
        while(n --)
        {
            string name;
            int p;
            cin >> name >> p;
            if(name == "O")
            {
                int dis = p - lastO;
                if(dis < 0)
                    dis = -dis;
                if(dis <= cuTime - timeO)
                    ++ cuTime;
                else
                    cuTime += dis - cuTime + timeO + 1;
                lastO = p;
                timeO = cuTime;
            }
            else
            {
                int dis = p - lastB;
                if(dis < 0)
                    dis = -dis;
                if(dis <= cuTime - timeB)
                    ++ cuTime;
                else
                    cuTime += dis - cuTime + timeB + 1;
                lastB = p;
                timeB = cuTime;
            }
        }
        cout << "Case #" << i + 1 << ": ";
        cout << cuTime << endl;
    }

    return 0;
}
