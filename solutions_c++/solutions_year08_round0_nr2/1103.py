#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    
    int N;
    cin >> N;
    for(int t=1; t<=N; t++) {

        int T;
        cin >> T;
        
        int timetableA[2000], timetableB[2000];
        for(int x=0; x<2000; x++) timetableA[x]=timetableB[x]=0;
        
        int AB, BA;
        cin >> AB >> BA;
        
        for(int x=0; x<AB; x++) {
            string a,b;
            cin >> a;
            timetableA[(a[0]-'0')*600+(a[1]-'0')*60+(a[3]-'0')*10+(a[4]-'0')]--;
            cin >> a;
            timetableB[(a[0]-'0')*600+(a[1]-'0')*60+(a[3]-'0')*10+(a[4]-'0')+T]++;
        }
        
        for(int x=0; x<BA; x++) {
            string a,b;
            cin >> a;
            timetableB[(a[0]-'0')*600+(a[1]-'0')*60+(a[3]-'0')*10+(a[4]-'0')]--;
            cin >> a;
            timetableA[(a[0]-'0')*600+(a[1]-'0')*60+(a[3]-'0')*10+(a[4]-'0')+T]++;
        }
        
        int rA=0, rB=0;
        
        for(int x=1; x<2000; x++) {
            rA = min( rA, timetableA[x]+=timetableA[x-1] );
            rB = min( rB, timetableB[x]+=timetableB[x-1] );
        }

        cout << "Case #" << t << ": " << -rA <<" " << -rB << endl;
    }
}
