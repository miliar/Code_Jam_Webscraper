
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <climits>
#include <vector>
using namespace std;

int solve()
{
    int number;
    int sandies[1000];

    cin>>number;
    int xorsum = 0;
    int sum = 0;
    int smalledst = INT_MAX;
    for(int i=0;i<number;++i){
        cin>>sandies[i];
        xorsum ^= sandies[i];
        sum+=sandies[i];
        smalledst = min(smalledst,sandies[i]);
    }

    if(xorsum!=0){
        cout<<"NO";
        return 0;
    }else{
        cout << sum-smalledst;
        return 0;
    }

}

int main()
{
    int casenum;
    cin>>casenum;
    for(int i=0;i<casenum;++i){
        cout<<"Case #"<<(i+1)<<": ";
        solve();
        cout<<endl;
    }
}

