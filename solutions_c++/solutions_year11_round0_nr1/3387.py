#include<iostream>
#include<cmath>

using namespace std;

struct bot
{
    int bPos;
    int sec;
    bot()
    {
        bPos = 1;
        sec = 0;
    }
    bot(int pos, int seconds)
    {
        bPos = pos;
        sec = seconds;
    }
};

int main()
{

    int t, cont = 1;
    cin>>t;
    while(t--)
    {
        long long seconds = 0;
        long long n;
        cin>>n;
        bot o, b;
        for(long long i=0;i<n;++i)
        {
            char l;
            long long pos;
            cin.ignore();
            cin>>l>>pos;
            if(l == 'O')
            {
                long long dsec = abs(o.sec - seconds), dpos = abs(o.bPos - pos);
                if(dsec <= dpos)
                {
                    if(pos <= seconds || o.sec != 0)
                        seconds += dpos - dsec + 1;
                    else
                        seconds = pos;
                    o.sec = seconds;
                    o.bPos = pos;
                }
                else
                {
                    seconds ++;
                    o.sec = seconds;
                    o.bPos = pos;
                }
            }
            else
            {
                long long dsec = abs(b.sec - seconds), dpos = abs(b.bPos - pos);
                if(dsec <= dpos)
                {
                    if(pos <= seconds || b.sec != 0)
                        seconds += dpos - dsec + 1;
                    else
                        seconds = pos;
                    b.sec = seconds;
                    b.bPos = pos;
                }
                else
                {
                    seconds ++;
                    b.sec = seconds;
                    b.bPos = pos;
                }
            }
        }
        cout<<"Case #"<<cont<<": "<<seconds<<endl;
        ++cont;
    }
    return 0;
}
