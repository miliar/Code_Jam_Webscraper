#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream input("A-large.in");
    assert(input.is_open());
    ofstream output("A-large.out");
    assert(output.is_open());

    int T;
    input>>T;
    for(int caseNum=0;caseNum<T;caseNum++)
    {
        unsigned long int N,K,tmp;
        input>>N>>K;
        tmp = 1<<N;
        string answer = K%tmp==tmp-1?"ON":"OFF";
        output<<"Case #"<<caseNum+1<<": "<<answer<<endl;
    }
    input.close();
    output.close();
    return 0;
}