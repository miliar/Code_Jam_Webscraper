#include <string> 
#include <vector> 
#include <string> 
#include <vector> 
#include <map> 
#include <utility> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <queue> 
#include <stack> 
#include <set> 
#include <sstream> 
#include <algorithm> 
#include <iostream> 
#include <iomanip> 
using namespace std; 
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<double,pair<double,double> >pdpdd;

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        double len,walks,runs,t;
        int n;
        scanf("%lf %lf %lf %lf %d",&len,&walks,&runs,&t,&n);
        //out<<len<<" "<<walks<<" "<<runs<<" "<<t<<" "<<n<<endl;
        vector<pdpdd> v;
        pdpdd temp;
        double dcor=0;
        for(int i=0;i<n;i++){
            double a,b;
            scanf("%lf %lf %lf",&a,&b,&temp.second.first);
            temp.second.second=b-a;
            dcor+=(b-a);
            temp.first=1.0/(runs+temp.second.first);
            v.push_back(temp);
        }
        temp.second.first=0;
        temp.second.second=len-dcor;
        temp.first=1.0/(runs);
        v.push_back(temp);
        
        sort(ALL(v),greater<pdpdd>());
        //for(int i=0;i<v.size();i++)
          //  cout<<v[i].first<<" swi="<<v[i].second.first<<" d="<<v[i].second.second<<endl;
        
        
        double res=0;
        for(int i=0;i<v.size();i++){
            if(t>0){
                double tt=v[i].second.second*v[i].first;
//                cout<<v[i].first<<" swi="<<v[i].second.first<<" d="<<v[i].second.second<<" tt="<<tt<<endl;
                if(t>tt){
                    t-=tt;
                    res+=tt;
                }else{
                    double drec=t*(runs+v[i].second.first);
                    res+=t;
                    t=0;
//                    cout<<"drec="<<drec<<endl;
                    
                    double drem=v[i].second.second-drec;
                    double t2=drem/(walks+v[i].second.first);
                    res+=t2;
                    
                    
                }
            }else{
                res+=v[i].second.second/(walks+v[i].second.first);
            }
        }
        
        printf("%.9lf\n",res);
    }

    return 0;
}

