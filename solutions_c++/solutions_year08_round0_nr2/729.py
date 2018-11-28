#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
using namespace std;
 
//double PI =  3.14159265358979323846;
#define ll long long
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define PI pair<int,int>
#define MP make_pair
#define VPI vector<PI >

VI all;


int next(int t) {
    string cas;
    cin>>cas;
    cas[2]=' ';
    stringstream ss;ss<<cas;
    int h, m;
    ss>>h>>m;
    all.PB(60*h+m+t);
    return    60*h+m+t;
}

typedef vector<int> IVECTOR;
typedef priority_queue<int, IVECTOR, greater<int> > IQ;
        

int main() {
    int cases;
    cin>>cases;
    for (int tt=0;tt<cases;tt++) {
        int na,nb,t;
        cin>>t;
        all.clear();
        cin>>na>>nb;
        VPI depsA;
        VPI depsB;
        int t1,t2;
        for (int i=0;i<na;i++) {
            t1=next(0);
            t2=next(t);
            depsA.PB(MP(t1,t2));
        }
        for (int i=0;i<nb;i++) {
            t1=next(0);
            t2=next(t);
            depsB.PB(MP(t1,t2));
        }
        sort(all.begin(),all.end());
        sort(depsA.begin(),depsA.end());
        sort(depsB.begin(),depsB.end());        
      /*  for (int i=0;i<depsA.size();i++) {
            cout<<i<<" :A "<<depsA[i].first<<" "<<depsA[i].second<<endl;    
        }
        for (int i=0;i<depsB.size();i++) {
            cout<<i<<":B "<<depsB[i].first<<" "<<depsB[i].second<<endl;    
        }*/
        int rA=0;int rB=0;
        int A=0;
        int B=0;
        IQ arrA,arrB;
        int da=0;
        int db=0;
        for (int i=0;i<all.size();i++) if (i==0||all[i]!=all[i-1]) {
                while (arrA.size()>0&&arrA.top()==all[i]) {A++; arrA.pop(); /*cout<<"arrived to A "<<all[i]<<endl;*/}
                while (arrB.size()>0&&arrB.top()==all[i]) {B++; arrB.pop(); /*cout<<"arrived to B "<<all[i]<<endl;*/}
                while (da<depsA.size()&&depsA[da].first==all[i]) {
                    A--;
                    arrB.push(depsA[da].second);
                    da++;  
//                    cout<<"odisiel z A, pride o "<<depsA[da-1].second<<endl;
                }
                if (A<0) {rA-=A;A=0;}
                while (db<depsB.size()&&depsB[db].first==all[i]) {
                    B--;
                    arrA.push(depsB[db].second);
 //                   cout<<"odisiel z B, pride o "<<depsB[db].second<<endl;
                    db++;  
                }
                if (B<0) {rB-=B;B=0;}
   //             cout<<A<<" "<<B<<" "<<rA<<" "<<rB<<" at "<<all[i]<<endl;
        }
        cout<<"Case #"<<tt+1<<": "<<rA<<" "<<rB<<endl;

        
        
    }    
    
}
