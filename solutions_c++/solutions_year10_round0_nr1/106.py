#include <iostream>
#include <fstream>
using namespace std;

int main()
{

fstream In("a-large.in", ios::in);
fstream Out("a-large.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{

int N, K;

In >> N >> K;

Out << "Case #" << h+1 << ": " << (((K+1)%(1<<(N))) ? "OFF" : "ON") << endl;

}

In.close();

Out.close();

return 0;

}
 
