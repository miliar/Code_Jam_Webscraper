#include <stdio.h>
#include <vector>

using namespace std;

int min(int a,int b){return ((a<b)?a:b);}
int max(int a,int b){return ((a>b)?a:b);}

int main(){
    int t;
    scanf("%d",&t);
    for(int cas=0;cas<t;cas++){

    int n; scanf("%d",&n);
    vector<int> d;//dist
    vector<int> l;//intueurs
    vector<int> lmax;
    
    int dd,ll;
    for(int i=0;i<n;i++){scanf("%d %d",&dd,&ll);d.push_back(dd);l.push_back(ll);lmax.push_back(-1);}
    scanf("%d",&dd);d.push_back(dd);lmax.push_back(-1);
    
    
    lmax[0]=d[0];
    for(int i=0;i<n;i++){
        for(int j=i+1;j<=n;j++){
            if(d[j]>d[i]+lmax[i]) break;
            if(lmax[j]==-1)lmax[j]=min(l[j],d[j]-d[i]);
            else lmax[j]=max(lmax[j],min(l[j],d[j]-d[i]));
        }
    }


        printf("Case #%d: %s\n",(cas+1),(lmax[n]==-1)?"NO":"YES"); 
    }
    return 0;
}
