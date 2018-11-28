#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
using namespace std;
string convertlong(long long number){
    stringstream ss;
    ss << number;
    return ss.str();
}
string shift(string number){
    for(unsigned i=1;i<number.size();++i)
        swap(number[i],number[i-1]);
    return number;
}
vector<string> data;
int main(void){
    long long t,cnt=0;
    cin>>t;
    while(t--){
        data.clear();
        long long cases=0;
        string x,y;
        cin>>x>>y;
        string xr(x.rbegin(),x.rend()),yr(y.rbegin(),y.rend());
        for(long long i=atoi(x.c_str());i<=(atoi(y.c_str()));++i){
            string temp(convertlong(i));
            data.push_back(temp);
        }
        for(unsigned i=0;i<data.size();++i){
            string temp=shift(data[i]);
            while(temp!=data[i]){
                if(atoi(temp.c_str())<=atoi(y.c_str()) && atoi(data[i].c_str())<atoi(temp.c_str())){
                    cases++;
                }
                temp=shift(temp);
            }
        }
        cout<<"Case #"<<++cnt<<": "<<cases<<endl;
    }
    return 0;
}
