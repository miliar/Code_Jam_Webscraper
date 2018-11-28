#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int calcXOR(vector<int> & v){
    int val = 0;
    for (vector<int>::iterator it = v.begin(); it!= v.end(); it++)
        val^= *it;
    return val;
}

int calcAdd(vector<int>& v){
    int val = 0;
    for (vector<int>::iterator it = v.begin(); it!= v.end(); it++)
        val += *it;
    return val;
}

int partition(vector<int> arr, int num){
    vector<int> arr1; //brother
    vector<int> arr2; //sister

    int i=0;
    for (vector<int>::iterator it = arr.begin(); it!=arr.end(); it++,i++){
        if (num&((1<<i))){
            arr1.push_back(*it);
        }else{
            arr2.push_back(*it);
        }
    }
    int bb = calcXOR(arr1);
    int bs = calcXOR(arr2);
    int sb = calcAdd(arr1);
    int ss = calcAdd(arr2);

    if (bb == bs && ss >= sb)
        return ss;
    return -1;
}

void go(vector<int> arr){
    int max = (1<<arr.size()) - 1;
    int d=0;
    int maxNum = 0;
    for (int i=1; i<max; i++){
        int p = partition(arr,i);
        if (p>0){
            maxNum = std::max(maxNum,p);
            d = 1;
        }
    }
    if (!d){
        cout<<": NO"<<endl;
    }
    else{
        cout<<": "<<maxNum<<endl;
    }
}

int main(){
    int t,num, temp;
    cin>>t;
    for (int i=0; i<t; i++){
        cin>>num;
        vector<int> arr;
        for (int j=0; j<num; j++){
            cin>>temp;
            arr.push_back(temp);
        }
        cout<<"Case #"<<i+1;
        go(arr);
    }
    return 0;
}
