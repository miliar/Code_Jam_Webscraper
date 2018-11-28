#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<cmath>

using namespace std;

int main(){
    ifstream fin("A-small-attempt3.in");
    ofstream fout("A-small-attempt3.out");
    int n;
    fin>>n;
    string s;
    for(int x=1;x<=n;x++){
            fin>>s;
            vector<int> v(s.size());
            int count=0;
            for(int i=0;i<v.size();i++){
                        if(s.find(s[i])==i){
                                            if(i==0)v[v.size()-1-i]=1;
                                            else {v[v.size()-1-i]=count;if(count==0)count++;count++;}
                                            }
                        else v[v.size()-1-i]=v[v.size()-1-s.find(s[i])];
                        }
            if(count==0)count=2;
            long long seconds=0;
            for(int i=0;i<v.size();i++){
                    seconds=seconds+(long long)(pow(double(count),double(i))*v[i]);
                    }
            fout<<"Case #"<<x<<": "<<seconds<<endl;
}
    }
