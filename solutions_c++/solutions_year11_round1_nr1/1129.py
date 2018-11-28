#include <iostream>
#include <fstream>

using namespace std;

int gcd(int a, int b)
{
    while(a!=0)
    {
        b = b % a;
        int tmp = a;
        a = b;
        b = tmp;
    }
    return b;
}

int s(int a, int b)
{
    int c=gcd(a,b);
    return a*b/c;
}

bool solve(unsigned long long N, int pd, int pg)
{
    if((pg == 0 && pd != 0)|| 
       (pg == 100 && pd != 100))
        return false;
    if((pg == 0 && pd == 0) ||
        (pg == 100 && pd == 100))
        return true;
    int bd = s(pd, 100)/pd;
    int bg = s(pg, 100)/pg;
    if(bd > N ) return false;
    return true;
}
int main(int argc, char **argv)
{
    ifstream in(argv[1]);
    ofstream out("output.txt");
    int n;
    in >> n;
    for(int i = 0; i < n; i++)
    {
        unsigned long long N;
        int pd, pg;
        in>>N>>pd>>pg;
        out<<"Case #"<<i+1<<": ";
        if(solve(N, pd, pg))
        {
            out<<"Possible";
        }
        else
        {
            out<<"Broken";
        }
        out<<endl;
    }
    return 0;
}
