#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef long double ldouble;
using namespace std;
int main(){
    int64 test,caseID,i,j;
    cin>>test;
    for(caseID=1;caseID<=test;caseID++){
            int64 n, cnt=0;
            cin>>n;
            int64 point [n][2];
            for(i=0;i<n;i++)
                            cin>>point[i][0]>>point[i][1];
            for(i=0;i<n;i++){
                    for(j=0;j<n;j++){
                             if(point[j][0]<point[i][0] && point[j][1]>point[i][1])
                                                        cnt++;
                    }
            }
            cout<<"Case #"<<caseID<<": "<<cnt<<endl;
    }
    return 0;
}
