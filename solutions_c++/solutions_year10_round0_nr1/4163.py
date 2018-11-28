#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int pow(int a,int b) {
    int ret=1;
    for(int i=0; i<b; i++) ret*=a;
    return ret;
}

int main()
{
    ifstream inp("A-large.in");
    ofstream out("A-large.out");
    int t,n,k;
    inp>>t;
    int i=1;
    while(t>0) {
               inp>>n>>k;
               k++;
               out<<"Case #"<<i<<": ";
               if(k%pow(2,n)==0) out<<"ON"<<endl;
               else out<<"OFF"<<endl;
               i++;
               t--;
    }
    return 0;
}
