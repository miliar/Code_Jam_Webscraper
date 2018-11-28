#include<iostream>

using namespace std;

int abs(int x)
{
    if(x>=0)
        return x;
    else
        return -x;
}

int main()
{
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int ans=0;
        int round;
        cin>>round;
        int o=1;
        int b=1;
        int time=0;
        char pre='x';
        for(int i=0;i<round;i++)
        {
            char c;
            int tmp;
            cin>>c;
            cin>>tmp;
            if(c=='B')
            {
                int d = abs(b-tmp);
                if(pre == 'B' or pre == 'x')
                {
                    time += d;
                    ans += d;
                }
                else
                {
                    if(time < d)
                    {
                        ans += d-time;
                        time = (int)abs(time-d);
                    }
                    else
                        time = 0;
                }
                b = tmp;
                pre = 'B';
                ans += 1;
                time += 1;
            }
            if(c=='O')
            {
                int d = abs(o-tmp);
                if(pre == 'O' or pre == 'x')
                {
                    time += d;
                    ans += d;
                }
                else
                {
                    if(time < d)
                    {
                        ans += d-time;
                        time = abs(time-d);
                    }
                    else
                        time = 0;
                }
                o = tmp;
                pre = 'O';
                ans += 1;
                time += 1;
            }
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
