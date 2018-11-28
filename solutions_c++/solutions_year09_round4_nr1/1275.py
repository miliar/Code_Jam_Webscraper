#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int cur[40];
    queue<int> q;
    int coden, t;
    cin >> t;
    // define vars
    int n;
    int i, j, k;
    string inp;
    int temp;
    int minn;
    int ans = -1;

    for (coden = 1; coden <= t; coden++)
    {
        cin >> n;
        for (i = 0; i < n; i++)
        {
            cin >> inp;
            //cout << "inp = " << inp;
            temp = 0;
            for (j = 0; j < inp.size(); j++)
            {
                if (inp[j] == '1')
                    temp = j;
            }
            cur[i] = temp;
            q.push(temp);
            //cout << temp;
        }
        q.push(0);
        //cout << ": " << 0; 

        //int end = 0;
        ans = -1;
        while(!q.empty())
        {
            for (i = 0; i < n; i++)
            {
                cur[i] = q.front(); q.pop();
            }
            minn = q.front(); q.pop();
            for (i = 0; i < n; i++)
            {
                if (cur[i] > i)
                    break;
            }
            if (i == n) //find ans
            {
                if (ans == -1 || ans > minn)
                    ans = minn;
                continue;
            }
            // cur[i] > i
            // swap cur[i] and cur[i+1]
            /*
            for (j = 0; j < n; j++)
            {
                if (j == i) q.push(cur[i+1]);
                else if (j == i+1) q.push(cur[i]);
                else q.push(cur[j]);
            }
            q.push(minn + j - i);
            */
            //for (j = i+1; j < n; j++)
            for (j = i+1; j <= n; j++)
            {
                if (cur[j] <= i)
                {
                    // swap cur[i] and cur[j]
                    for (k = 0; k < n; k++)
                    {
                        if (k == i)
                            q.push(cur[j]);
                        else
                            if (k > i && k <= j)
                                q.push(cur[k - 1]);
                            else
                                q.push(cur[k]);
                    }
                    q.push(minn + j - i);
                }
            }
        }

        // output result
        cout << "Case #" << coden << ": " << ans << endl;
    }
    return 0;
}

