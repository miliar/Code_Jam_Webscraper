#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef queue<int>  INTQUEUE;
int g[1000];


void append(INTQUEUE& q1, INTQUEUE& q2){
    while(!q2.empty()){
        int temp = q2.front();
        q1.push(temp);  
        q2.pop();
    }  
}

/*void initial(INTQUEUE q, int g[],int n){
     
}*/

int process(int r,int k,int n,int a[1000], INTQUEUE& q1, INTQUEUE& q2){
    int sum = 0;
      
    for (int i=1; i<=n;i++){
        q1.push(a[i]);    
    }
    
      //  q1.push(2);
        //    q1.push(4);
    for (int i=1; i<=r; i++){
        int money = 0;
        while ((money<=k)){
            if (q1.empty()){
                break;    
            }
            int temp = q1.front();
            if ((money + temp) > k){    
                break;
            }
            else{
                money = money + temp;
                q2.push(temp);  
                q1.pop();
                 
            }
        }  
        sum += money;  
        append(q1,q2);
    }
    return sum;
}
int main(){
    
    ifstream fin;
    fin.open("C-small-attempt0.IN");
    ofstream fout;
    fout.open("cuong.txt");
    int t;
    fin >> t;
    int r,k,n;
    for (int i=1;i<=t;i++){
        INTQUEUE q1;
        INTQUEUE q2;
        fin >> r>>k>>n;
        for (int j=1; j<=n;j++){
            fin >> g[j];
        }
        
        fout << "Case #"<<i<<": "<<process(r,k,n,g,q1,q2)<<endl;
    }
//    system("pause");

    return 0;
}
