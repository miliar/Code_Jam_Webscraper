#include <iostream>
using namespace std;
char to[256];
int main(){
    for(int i=0;i<3;i++){
        string in1,in2;
        getline(cin,in1);
        getline(cin,in2);
        for(int j=0;j<in1.size();j++){
            to[in1[j]]=in2[j];
        }
    }
    to['z']='q';
    to['q']='z';
    to[' ']=' ';
    int n;
    cin>>n;
    string in;
    getline(cin,in);
    for(int i=0;i<n;i++){
        cout<<"Case #"<<i+1<<": ";
        getline(cin,in);
        for(int j=0;j<in.size();j++){
            cout<<(char)to[in[j]];
        }
        cout<<endl;
    }
}
