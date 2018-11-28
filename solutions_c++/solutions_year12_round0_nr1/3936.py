#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    freopen("Round_1A_A_small.in","r",stdin);
    freopen("Round_1A_A_small.out","w",stdout);
    //freopen("Round_1A_A_large.in","r",stdin);
    //freopen("Round_1A_A_large.out","w",stdout);
    int times,count=0;
    cin>>times;getchar();
    while(times--)
    {
        string line;
        getline(cin,line);
        for(int i=0;i<line.length();i++)
        {
            switch(line[i])
            {
                case 'a': line[i]='y'; break;
                case 'b': line[i]='h'; break;
                case 'c': line[i]='e'; break;
                case 'd': line[i]='s'; break;
                case 'e': line[i]='o'; break;
                case 'f': line[i]='c'; break;
                case 'g': line[i]='v'; break;
                case 'h': line[i]='x'; break;
                case 'i': line[i]='d'; break;
                case 'j': line[i]='u'; break;
                case 'k': line[i]='i'; break;
                case 'l': line[i]='g'; break;
                case 'm': line[i]='l'; break;
                case 'n': line[i]='b'; break;
                case 'o': line[i]='k'; break;
                case 'p': line[i]='r'; break;
                case 'q': line[i]='z'; break;
                case 'r': line[i]='t'; break;
                case 's': line[i]='n'; break;
                case 't': line[i]='w'; break;
                case 'u': line[i]='j'; break;
                case 'v': line[i]='p'; break;
                case 'w': line[i]='f'; break;
                case 'x': line[i]='m'; break;
                case 'y': line[i]='a'; break;
                case 'z': line[i]='q'; break;
            }
        }
        cout<<"Case #"<<++count<<": "<<line<<endl;
    }
    return 0;
}
