#include<sstream>
#include<iostream>
#include<vector>
#include<cmath>
#include<string>
#include <algorithm>
using namespace std;
vector<int> values;
int sum=0;
vector<bool> taken;
int mx=0;
int calcTaken(bool took){
              int val = 0;
              for (int i=0 ; i<values.size() ; i++)
                  if (taken[i] == took){
                     val+=values[i];
                  }
              return val;
}

int calcBin(bool took){
              int val = 0;
              for (int i=0 ; i<values.size() ; i++)
                  if (taken[i]==took){
                     val^=values[i];
                  }
              return val;
}

void dp(int cur){
     
    if (cur == values.size()){
            return;
    }
    if (calcBin(true) == calcBin(false)){
       mx = calcTaken(true);
    }
    //cout<<"cur = "<<cur<<endl;
     //system("pause");
    dp(cur+1);
    taken[cur] = true;
    dp(cur+1);
    taken[cur] = false;
}
int main(){
    freopen("C-small-attempt1.in","rt",stdin);
    freopen("c.out","wt",stdout);
    int n,tmp;
    cin>>n;
    
    for (int w=0; w<n ; w++){
        int t;
        cin>>t;
        values.clear();
        taken.clear();
        sum=0;
        mx = 0;
        for (int i=0 ; i<t ; i++){
            cin>>tmp;
            values.push_back(tmp);
            taken.push_back(false);
        }
        
        sort(values.rbegin(),values.rend());
        
        
        dp(0);
        if (mx == 0){
           cout<<"Case #"<<(w+1)<<": NO\n";
        }else{
              cout<<"Case #"<<(w+1)<<": "<<mx<<endl;
        }
        
    }
    //system("pause");
    return 0;
}
