#include <fstream>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;


int solve(queue<char> &tqueue, queue<int> &oqueue, queue<int> &bqueue)
{
    int op = 1;
    int bp = 1;
    int clock = 0;
    while(!tqueue.empty())
    {
        clock++;
        bool omove = true;
        bool bmove = true;
        if(tqueue.front() == 'O' 
         && oqueue.front() == op)
        {
            tqueue.pop();
            oqueue.pop();
            omove = false;
        }
        else if(tqueue.front() == 'B'
         && bqueue.front() == bp)
        {
            tqueue.pop();
            bqueue.pop();
            bmove = false;
        }

        if(bmove && !bqueue.empty())
        {
            if(bqueue.front() > bp)
                bp++;
            if(bqueue.front() < bp)
                bp--;
        }
        if(omove && !oqueue.empty())
        {
            if(oqueue.front() > op)
                op++;
            if(oqueue.front() < op)
                op--;
        }
    }
    return clock;
}

int main(int argc, char ** argv)
{
    ifstream in(argv[1]);
    ofstream out("output.txt");
    int n;
    in >> n;
    cout<<n<<endl;
    for(int i = 1; i <= n; i++)
    {
        int total;
        in >> total;
        cout<<total<<endl;
        queue<int> oqueue;
        queue<int> bqueue;
        queue<char> tqueue;
        char t; int p;
        for(int j = 0; j < total; j++)
        {
            in >> t >> p;
            tqueue.push(t);
            if(t == 'O')
                oqueue.push(p);
            else
                bqueue.push(p);
        }
        int ans = solve(tqueue, oqueue, bqueue);
        cout<<ans<<endl;
        out<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
