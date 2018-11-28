#include <iostream>

using namespace std;

/*
  Return 1 if Googlers score t can contain p.
  Return 2 if Googlers score t can contain p but t is a surprising score.
  Otherwise returns 0.
*/

int is_greather_then_p(int p, int t)
{
    // Explicit check for p lower than 3 to avoid division by 0
    if(p == 0)
        return 1;

    if(p == 1){
        if(t >= 1)
            return 1;
        else return 0;
    }
    
    if(p == 2){
        if(t >= 4)
            return 1;
        if(t >= 2)
            return 2;
        return 0;
    }

    // Check for p bigger or equal than 3
    if((t / p) >= 3)
        return 1;

    if((t / (p - 1)) >= 4)
        return 1;
    if((t / (p - 1)) == 3 && (t % (p - 1)) >= 1)
        return 1;

    if((t / (p - 2)) >= 4)
        return 2;
    if((t / (p - 2)) == 3 && (t % (p - 2)) >= 2)
        return 2;

    return 0;
}

int main(int argc, char *argv[])
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n, s, p;
        int result = 0;
        cin >> n;
        cin >> s;
        cin >> p;
        for (int j = 0; j < n; ++j)
        {
            int t_i;
            cin >> t_i;
            if(is_greather_then_p(p, t_i) == 1)
                result++;
            if(is_greather_then_p(p, t_i) == 2 && s > 0){
                --s;
                result++;
            }
        }
        cout << "Case #" << i+1 << ": " << result << endl;
    }

    return 0;
}
