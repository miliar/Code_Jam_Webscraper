#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(){

    int n;
    string line;
    getline(cin, line);
    istringstream iss(line);
    iss>>n;
    
    for(int i=0;i<n;i++)
    {
        int num;
        string line;
        getline(cin, line);
        istringstream iss(line);
        iss>>num;
        num++;
        int nos[num];
        bool done[num];
        string line1;
        getline(cin, line1);
        istringstream iss1(line1);
        for(int j=1;j<num;j++)
        {
              done[j]=false;
              iss1>>nos[j];
        }
        float count=0;
        for(int j=1;j<num;j++)
        {
             int tcount=0;
             int present=j;
             while(done[present]==false)
             {
              done[present]=true;
              present=nos[present];
              tcount++;
             }
             if(tcount>1)  count+=tcount;
        }
        cout<<"Case #"<<i+1<<": "<<count<<endl;
    }
    return 0;
}
