#include <iostream>
#include <fstream>
#include <cassert>
#include <stdint.h>

using namespace std;
typedef uint64_t money_t;

class queue_t
{
    public:
    int N,cur;
    static const int maxN=1000;
    int groups[maxN];
    void read(istream &in)
    {
        cur=0;
        in>>N;
        assert(N<=maxN);
        for (int i=0;i<N;++i)
        {
            in>>groups[i];
        }
        assert(!in.fail());
    }
    int top()
    {
        return groups[cur];
    }
    void next()
    {
        ++cur;
        if (cur==N)
            cur=0;
    }
    money_t next_ride(int kPeoples)
    {
        money_t S=0;
        int first_seating=cur;
        while(S<=kPeoples-top())
        {
            S+=top();
            next();
            if (cur==first_seating)
                break;
        }
        return S;
    }
} ;

int main()
{
    queue_t queue;
    int Tlines;
    ifstream fin("in");
    ofstream fout("out");
    fin>>Tlines;
    for(int t=1;t<=Tlines;++t)
    {
        cout<<t<<"\n";
        int Rrides,Kpeoples;
        fin>>Rrides>>Kpeoples;
        assert(!fin.fail());
        queue.read(fin);
        money_t Sum=0;
        for (int r=0;r<Rrides;++r)
        {
            Sum+=queue.next_ride(Kpeoples);
        }
        fout<<"Case #"<<t<<": "<<Sum<<'\n';
    }
    return 0;
}
