#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(){
    int n;
    string line;
    getline(cin, line);
    istringstream iss2(line);
    iss2>>n;
    for(int i=0;i<n;i++)
    {
        int num;
        string line;
        getline(cin, line);
        istringstream iss1(line);
        iss1>>num;
        getline(cin, line);
        istringstream iss(line);
        int sum=0;
        int min=0;
        int x=0;
        for(int j=0;j<num;j++){
                int cno;
                iss>>cno;
                sum+=cno;                                
                if(j==0) 
                {
                      x=cno;
                      min=cno;
                }
                else 
                {
                      x = x ^ cno;
                      if(cno<min) min=cno;
                }
        }
        int value=sum-min;
        cout<<"Case #"<<i+1<<": ";
        if(x!=0) cout<<"NO"<<endl;
        else cout<<value<<endl;
    }
    return 0;
}
