#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int main(){
        freopen("a.in","rt",stdin);
        freopen("a.out","wt",stdout);
    int n;
    cin>>n;
    for (int i=0; i<n ; i++){
        int lastB=1,lastO=1,lastBT=0,lastOT=0;
        char last='a';
        int t,val,time=0;
        cin>>t;
        char ch;
        for (int j=0 ;j<t ; j++){
            cin>>ch;
            if (ch == '\n')cin>>ch;
            cin>>val;
            if (ch == 'O'){
                   int req = abs(val-lastO)+1;
                   if (lastOT+req <=time)time++;
                   else time = lastOT + req;
                   lastO = val;
                   lastOT = time;
            }
            if (ch == 'B'){
                   int req = abs(val-lastB)+1;
                   if (lastBT+req <=time)time++;
                   else time = lastBT+req;
                   lastB = val;
                   lastBT = time;
                   last = ch;
            }
        }
        cout<<"Case #"<<(i+1)<<": "<<time<<endl;
    }
    //system("pause");
    return 0;
}
