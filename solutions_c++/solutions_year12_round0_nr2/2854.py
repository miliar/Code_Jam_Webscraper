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
    ofstream fout ("B-large.out");
    ifstream fin ("B-large.in");

int testcases;
fin>>testcases;
for (int tests=1;tests<=testcases;tests++){
int ans=0;
int num,surp,check;
fin>>num>>surp>>check;
int triplet[num];
for (int i=0;i<num;i++)fin>>triplet[i];
for (int i=0;i<num;i++){
    int temp=triplet[i]/3;
    if (check==0 || check==1 && triplet[i]>0){
        ans++;
        continue;
    } 
    if (temp>=check && (triplet[i]!=0 && triplet[i]!=1)){
        ans++;
        continue;
    }
    if (triplet[i]==1 || triplet[i]==0)continue;
    if (triplet[i]%3!=0 && check==temp+1){
        ans++;
        continue;
    }
    if (surp<=0)continue;
    if (temp<check-2)continue;
    if (triplet[i]%3==2){
        if (temp==check-2){
            ans++;
            surp--;
            continue;
        }
        continue;
    }
    if (temp==check-1){
        ans++;
        surp--;
        
    }
    
    
}

//cout<<"Case #"<<tests<<": "<<ans<<endl;
fout<<"Case #"<<tests<<": "<<ans<<endl;
} 

//system("pause");
return 0;
}
