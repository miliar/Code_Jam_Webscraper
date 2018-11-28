#include <iostream>
using namespace std;
int t,casen;
int n,p;
char r;
int o_time,o_pos,b_time,b_pos;

int main()
{
    cin>>t;
    for (casen=1; casen<=t; casen++)
    {
        cin>>n;
        o_time=0; o_pos=1;
        b_time=0; b_pos=1;
        for (int i=0; i<n; i++)
        {
            cin>>r>>p;
            if (r=='O')
            {
                int move_time=abs(p-o_pos);
                if (move_time>b_time-o_time)
                    o_time+=move_time+1;
                else
                    o_time=b_time+1;
                o_pos=p;
            }
            else
            {
                int move_time=abs(p-b_pos);
                if (move_time>o_time-b_time)
                    b_time+=move_time+1;
                else
                    b_time=o_time+1;
                b_pos=p;
            }
        }
        cout<<"Case #"<<casen<<": ";
        cout<<(o_time>b_time?o_time:b_time)<<endl;
    }
    return 0;
}

