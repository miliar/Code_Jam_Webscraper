#include <cstdio>
#include <vector>
#include <cstring>
#include <utility>
#include <algorithm>
using namespace std;

int n;
vector<int> all;
char a[105][105];

double wp(int k, vector<int>& u = all){
    double sum=0;
    int cnt=0;
    for(int i=0;i<int(u.size());i++){
        if(a[k][u[i]]=='.') continue;
        if(a[k][u[i]]=='1') sum++;
        cnt++;
    }
    if(!cnt) return 0; else return sum/cnt;
}

double owp(int k, vector<int>& u = all){
    double sum=0;
    int cnt=0;
    vector<int> r=u;
    r.erase(find(r.begin(),r.end(),k));
    for(int i=0;i<int(u.size());i++){
        if(a[k][u[i]]=='.') continue;
        sum+=wp(u[i],r);
        cnt++;
    }
    if(!cnt) return 0; else return sum/cnt;
}

double oowp(int k, vector<int>& u = all){
    double sum=0;
    int cnt=0;
    vector<int> r=u;
    r.erase(find(r.begin(),r.end(),k));
    for(int i=0;i<int(u.size());i++){
        if(a[k][u[i]]=='.') continue;
        sum+=owp(u[i]);
        cnt++;
    }
    if(!cnt) return 0; else return sum/cnt;
}

int main(){
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++){
        printf("Case #%d:\n",t);
        scanf("%d",&n);
        all.clear();
        for(int i=0;i<n;i++) scanf("%s",a[i]);
        for(int i=0;i<n;i++) all.push_back(i);
        for(int i=0;i<n;i++)
            printf("%.14f\n",wp(i)*0.25+owp(i)*0.5+oowp(i)*0.25);
    }
}
