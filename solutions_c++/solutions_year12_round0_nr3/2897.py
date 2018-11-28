#include <vector>
#include <fstream>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
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
#define eps=1e-8
using namespace std;

//correct

int main(){
    ofstream fout ("C-small-attempt0.out");
    ifstream fin ("C-small-attempt0.in");

int testcases;
fin>>testcases;
for (int tests=1;tests<=testcases;tests++){
    double elapTime;
clock_t beginT, endT;



beginT = clock();

    long long start,end;
    fin>>start>>end;
    map <long long int,long long int> count;
    
    for (long long i=start;i<=end;i++){
        string temp;
        long long num=i;
        while (num>0){
            temp+=num%10+'0';
            num/=10;
        }
        string arr[temp.size()];
        arr[0]=temp;
        for (int i=1;i<temp.size();i++){
            arr[i]=arr[i-1];
            arr[i].erase(arr[i].size()-1,1);
            arr[i].insert(0,1,arr[i-1][arr[i-1].size()-1]);
            
        }
        sort(arr,arr+arr[0].size());
        long long value=0;
        temp=arr[0];
        for (int i=temp.size()-1;i>=0;i--){
            value*=10;
            value+=temp[i]-'0';
        }
        /* map<long long int, long long int>::iterator it=count.begin();
        it=count.find(value);
        if (it==count.end()){
            count[value]=1;
        }
        else  */
        count[value]++;
    }

  
  long long ans=0;
  map<long long int, long long int>::iterator it=count.begin();
for (;it!=count.end();it++){
    long long val=(*it).second;
    ans+=(long long)val*(val-1)/2;
    //cout<<(*it).first<<" "<<(*it).second<<endl;
}
//cout<<"Case #"<<tests<<": "<<ans<<endl;
fout<<"Case #"<<tests<<": "<<ans<<endl;

endT = clock();

elapTime = ((double)(endT - beginT)*1000)/CLOCKS_PER_SEC;
cout<<elapTime<<endl; 
//system("pause");
} 

//system("pause");
return 0;
}
