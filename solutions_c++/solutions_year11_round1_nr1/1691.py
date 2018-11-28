#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int hcf_function(int m,int n)
{
    int temp,reminder;
    if(m<n)
    {
        temp=m;
        m=n;
        n=temp;
    }
    while(1)
    {
        reminder=m%n;
        if(reminder==0)
                return n;
        else
                m=n;
        n=reminder;
    }
}


int main(){
    int n;
    string line;
    getline(cin, line);
    istringstream iss2(line);
    iss2>>n;
    for(int i=0;i<n;i++)
    {
        string line;
        getline(cin, line);
        istringstream iss1(line);
        int a,b,c;
        iss1>>a;
        iss1>>b;
        iss1>>c;
        if(c==0||c==100) {
         if(b==0&&c==0||b==100&&c==100)
         cout<<"Case #"<<i+1<<": "<<"Possible"<<endl;
         else 
         cout<<"Case #"<<i+1<<": "<<"Broken"<<endl;
         }
        else
        {
         if(100/hcf_function(100,b)<=a)
         cout<<"Case #"<<i+1<<": "<<"Possible"<<endl;
         else
         cout<<"Case #"<<i+1<<": "<<"Broken"<<endl;
        }
    }
    return 0;
}
