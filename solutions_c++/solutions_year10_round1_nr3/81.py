#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

#define llong long long

int A1,A2, B1, B2;

int locs[2000001];

double RATIO=(1.0+sqrt(5.0))/2.0;

llong eval(double n) {
    llong ret=2+(llong)floor((n+1)*RATIO) - (llong)floor((n+2)*RATIO);
    return ret;
    //cout<<ret;
}

void preprocess() {
    //for(int i=0;i<100;i++) eval(i);
    locs[2]=locs[3]=1;
    for(int i=4;i<=2000000;i++) {
        //cout<<"*********"<<i<<": ";
        llong cur=eval(i-2), next=eval(i-1);
        //cout<<cur<<','<<next<<endl<<endl;
        if(cur==next&&next==0) {
            locs[i]=locs[i-1]+1;
        } else {
            locs[i] = locs[i+1]=locs[i-1]+1;
            i++;
        }
    }
    //for(int i=2;i<100;i++) cout<<locs[i]<<endl;
}

llong bIntersect(llong a1, llong a2) {
    if(a1>a2) return 0;
    llong x1=a1, y1=a2;
    llong x2=B1, y2=B2;
    if(x2<x1) {
        swap(x1,x2);
        swap(y1,y2);
    }
    //cout<<x1<<','<<y1<<"*****"<<x2<<','<<y2<<endl;
    if(!(x2>=x1&&x2<=y1)) return 0;
    llong low=x2;
    llong high=min(y1,y2);
    return high-low+1;
}

llong getRange(llong A) {
    llong start1=1;
    llong start2=locs[A];

    llong start3=locs[A]+A+1;
    llong start4=B2;

    return bIntersect(start1, start2) + bIntersect(start3, start4);
}

llong ones(int pos) {
    llong ret=B2-B1+1;
    if(B1==1) ret--;
    return ret;
}

llong solve() {
    llong ret=0;
    for(int i=A1;i<=A2;i++) {
        if(i==1) ret+=ones(i);
        else ret+=getRange(i);
    }
    return ret;
}

int main() {
    preprocess();
    //return 0;
    int cases;
    cin>>cases;
    for(int c=1;c<=cases;c++) {
        cin>>A1>>A2>>B1>>B2;
        cout<<"Case #"<<c<<": "<<solve()<<endl;
    }
}
