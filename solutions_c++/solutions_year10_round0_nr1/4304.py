#include <iostream>
#include <fstream>
#include <memory.h>
#include <cstdlib>
#define ON 1
#define OFF 0
using namespace std;

void go(bool* s,int len)
{
    for(int i=0;;)
    {
        if(i>=len) break;
        if(s[i]==ON&&i<len) s[i++]=OFF;
        else if(s[i]==OFF&&i<len) {s[i]=ON;break;}
    }
}
bool check(bool* s,int len)
{
    int i=0;
    while(i<len)
    {
        if(s[i]==OFF) return false;
        else i++;
    }
    return true;
}

int main()
{
    ifstream cin("A-small-attempt0.in");
    ofstream cout("a.out");
    int T,N,K,c=1;
    cin>>T;
    while(T--)
    {
        cin>>N>>K;
        bool s[N];
        memset((void*)s,OFF,N);
        for(int i=0;i<K;i++) go(s,N);
        cout<<"Case #"<<c++<<": "<<(check(s,N)?"ON":"OFF")<<endl;
    }
    return 0;
}
