#include <string>
#include <fstream>
#include<iostream.h>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

int main()
{
    int n=0,s=0,q=0,count=0;
    string str="",temp="";
    set<string> q1;
    ifstream file("C:\\A-large.in");
    getline( file, str );
    n=atoi(str.c_str());
    for (int i=0;i<n;i++){
        count=0;
        getline( file, str );
        s=atoi(str.c_str());
        for (int j=0;j<s;j++)
            getline( file, str );
        getline( file, str );
        q=atoi(str.c_str());
        for (int j=0;j<q;j++){
            getline( file, str );
            q1.insert(str);
            if(q1.size()==s){
                             count++;
                             q1.clear();
                             q1.insert(str);
            }
        }
        q1.clear();
        cout<< "Case #"<<(i+1)<<": "<<count<<endl;
    }
    file.close();
    return 0;
}
