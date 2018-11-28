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
#include <cstring>
#include <climits>
using namespace std;

int main(){
    string str;
    int t,no=1;
    scanf("%d",&t);
    while(t--){
        cin>>str;
        string out;
        int zero=0;
        for(int i=0;i<str.size();i++)
            if(str[i]=='0')zero++;
        printf("Case #%d: ",no++);
        if(!next_permutation(str.begin(),str.end())){
            sort(str.begin(),str.end());
            cout<<str[zero];
            for(int i=1;i<=zero+1;i++)cout<<"0";
            for(int i=zero+1;i<str.size();i++)cout<<str[i];
            cout<<endl;
        }
        else cout<<str<<endl;


    }
    return 0;
}

