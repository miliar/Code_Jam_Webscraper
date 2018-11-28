/* {{{ */
#include<cstdio>
#include<climits>
#include<cmath>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
#include<list>
#include<sstream>
#include<set>
#include<queue>
#include<vector>
#include<string>
#include<fstream>
#include<istream>
#include<iostream>
#include<bitset>
using namespace std;
/* }}}  */

typedef long long ll;
typedef unsigned long long ull;

bool dothey(int y1,int y2,int y3,int y4,pair<double,double> &p){
        double m1=(y2-y1)/10000.0,m2=(y4-y3)/10000.0;
//        printf("y1-y2 = %d,y3-y4=%d\n",y1-y2,y3-y4);
        if(y1-y2==y3-y4) return false;
        assert(fabs(m1-m2)>1e-9);
        double x=(y3-y1)/(m1-m2);
 //       printf("x is %.3g,m1,m2=%.3g,%.3g\n",x,m1,m2);
        if(x<=0) return false;
        if(x>=10000) return false;
        p.first=x;
        p.second=m1*x +y1;
        return true;
}

int main(int argc,char **argv){
    int NC,tc;
    cin >> NC;
    for(tc=1;tc<=NC;tc++){
            int N,i,j;
            cin >> N;
            vector<pair<int,int> > v;
            for(i=0;i<N;i++){
                    int y1,y2;
                scanf(" %d %d",&y1,&y2);
                v.push_back(make_pair(y1,y2));
            }
            set<pair<double,double> > S;
            for(i=0;i<N;i++){
                for(j=i+1;j<N;j++){
                        pair<double,double > pr;
                        if(dothey(v[i].first,v[i].second,v[j].first,v[j].second, pr)){
                             S.insert(pr);   
                            }
                }
            }
                printf("Case #%d: %d\n",tc,S.size());
    }
    return 0;
}

