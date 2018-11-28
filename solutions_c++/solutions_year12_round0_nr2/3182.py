#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <list>
#include <utility>
#include <string>

class Found{};

using namespace std;

bool f(int nmb, int p)
{
    return nmb>=(3*p-2);
}

bool g(int nmb, int p)
{
    return p>1 && nmb>=(3*p-4);
}

int main()
{
    ifstream in("C:\\Users\\Olexandr\\Desktop\\B-large.in");
    ofstream out("C:\\Users\\Olexandr\\Desktop\\output.txt");
    int T;
    in>>T;

    for(int t=0; t<T; t++)
    {
        out<<"Case #"<<(t+1)<<": ";
        //code here:
        int N,S,p;
        in>>N>>S>>p;
        int result=0;
        for(int i=0; i<N; i++)
        {
            int nmb;
            in>>nmb;
            if(f(nmb, p))
                result++;
            else if(S!=0 && g(nmb,p))
            {
                result++;
                S--;
            }
        }
        out<<result<<endl;
    }
    //system("pause>nul");
    return 0;
}