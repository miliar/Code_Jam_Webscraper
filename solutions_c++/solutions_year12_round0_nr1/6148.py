#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORI(i,b) FOR(i,0,b)


int main(int argc, char* argv[])
{
    ifstream input(*argv,ifstream::in);
    ofstream output("output.out",ofstream::out);
    char mapping[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t;
    input >> t;
    cout << t;
    char buf[101];
    input.getline(buf,101);
    FORI(i,t)
    {
        input.getline(buf,101);
        output << "Case #" << i+1 << ": ";

        // output
        FORI(j,strlen(buf))
        {
            if(buf[j]!=' '){output << mapping[buf[j]-'a'];}
            else{output << ' ';}
        }
        output << endl;

    }
    return 0;
}
