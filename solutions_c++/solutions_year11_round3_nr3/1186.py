#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <stdio.h>
#include <string.h>


using namespace std;


int main()
{
    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        int N, L, H, x;
        cin>>N>>L>>H;
        vector <int> arr;
        while(N--){
            cin>>x;
            arr.push_back(x);
        }
        int num=-1;
        for (int i=L;i<=H;i++){
            bool found = true;
            for (int j=0;j<arr.size();j++){
                if (arr[j]%i !=0 && i%arr[j]!=0)
                    found=false;
            }
            if (found){
                num = i;
                break;
            }
        }
        cout<<"Case #"<<cas<<": ";
        if (num==-1)
            cout<<"NO"<<endl;
        else
            cout<<num<<endl;
            
    }

}

