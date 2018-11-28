#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <stack>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
double EPS=1e-10;
double EQ(double a,double b){
    return abs(a-b)<EPS;
}
void fast_stream(){
  std::ios_base::sync_with_stdio(0);
}

typedef pair<double,int> pdi;

double s[1001];
int N;
double sum;

bool cmp(const pdi p1,const pdi p2){
    if(!EQ(p1.first,p2.first))return p1.first<p2.first;
    else{
        return p1.second<p2.second;
    }
}

bool check(double as,int idx){
    s[idx]+=(as/100)*sum;
    double left=sum-(as/100)*sum;
    for(int i=0;i<N;i++){
        if(i==idx)continue;
        double a=s[idx]-s[i];
        if(!EQ(a,0)&&a>0)left-=a;
    }
    s[idx]-=(as/100)*sum;
    if(!EQ(left,0)&&left>0)return false;
    return true;
}

void solve(){
    int T;
    cin>>T;
    for(int p=0;p<T;p++){
        vector<double> res;
        cin>>N;
        sum=0;
        for(int i=0;i<N;i++){
            cin>>s[i];
            sum+=s[i];
        }
        for(int i=0;i<N;i++){
            double ub=100;
            double lb=0;
            for(int q=0;q<200;q++){
                double mid=(ub+lb)/2;
                if(check(mid,i))ub=mid;
                else lb=mid;
            }
            res.push_back(ub);
        }
        cout<<"Case #"<<p+1<<":";
        for(int i=0;i<N;i++)
            printf(" %.10f",res[i]);
        cout<<endl;
    }
}
