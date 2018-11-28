#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <utility>
#include <functional>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define REPAB(i,a,b) for((i)=(a);(i)<(int)(b);(i)++)
#define DEC(i,n) for((i)=(n-1);(i)>=0;(i)--)


int a[1003];
int b[1003];

bool intersectan(int n1,int n2){
    return ((a[n1]>a[n2])!= (b[n1]>b[n2]));
}

int main(){
    int casos,n;
    int i,j;
    cin>>casos;

    for (int ncaso=1; ncaso<=casos; ncaso++){
        cin>>n;
        REP(i,n) cin>>a[i]>>b[i];
        int cont=0;
        REP(i,n-1)
            REPAB(j,i+1,n)
                if (intersectan(i,j))
                    cont++;
        cout<<"Case #"<<ncaso<<": "<<cont<<endl;
    }
    return 0;
}
