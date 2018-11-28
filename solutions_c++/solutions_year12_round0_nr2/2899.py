#include <iostream>
#include <string>
using namespace std;

int solv(int t[],int N,int &S,int P) {
    int count=0;
    for (unsigned int i = 0; i < N; i ++)
    {
        if(t[i] >=29 ) { if(10>= P) count++;continue;}
        if(t[i]<2) {if(t[i]>= P) count++; continue;}
        if( t[i] % 3 == 2) {
            //Do the boundary first.
            if(t[i]/3+1 >= P ) count++;
            if(t[i]/3+2 == P && S >0) {count++;S--;} 
        } else {
            if( t[i]/3+1 > P) count++;
            if( t[i]/3+1 == P ) {
                if(t[i] %3 ==0 && S>0) { count++; S--;}
                if(t[i] %3 ==1 ) count++;
            }
        }
    }
    //
    return count;
}

//-----------Start Fri Apr 13 19:39:26 EDT 2012------------------

int main() {
    int nTestCases;
    int N,S,P;
    int t[100];
    string line;
    cin>>nTestCases;
    getline(cin,line);
    for(int iCase=0;iCase< nTestCases;iCase++) {
        cin>>N>>S>>P;
        for (unsigned int i = 0; i < N; i ++)
        {
            cin>>t[i];
        }
        //inmplement
        cout<<"Case #"<<iCase+1<<": "<<solv(t,N,S,P)<<endl;
    }
}
