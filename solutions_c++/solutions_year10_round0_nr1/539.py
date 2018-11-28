#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>

using namespace std;

int T;
int N,K;
//ofstream out;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-small.out","w",stdout);
    //ofstream out("output.txt");
    cin>>T;
    int caseID = 0;
    while (T--){
        cin>>N>>K;
        //binary form ok K
        bool ok = false;
        if (K % (1<<N) == (1<<N)-1) ok = true;
        cout<<"Case #"<<++caseID<<": ";
        if (ok) cout<<"ON"<<endl;
        else cout<<"OFF"<<endl;
    }
    //out.close();
    return 0;
}
