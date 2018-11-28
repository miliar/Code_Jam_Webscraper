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
typedef pair<int,int> pii; 

typedef int point[2];

#define X 0
#define Y 1

int Area2(point a,point b,point c){
    return a[X]*(b[Y]-c[Y])-a[Y]*(b[X]-c[X])+(b[X]*c[Y]-b[Y]*c[X]);
}

int main(){
    int test;
    scanf("%d",&test);
    for(int t=0;t<test;t++){
        point a,b,c;
        printf("Case #%d: ",t+1);
        a[X]=a[Y]=0;        
        int n,m,A;
        scanf("%d %d %d",&n,&m,&A);
        bool pos=false;
        for(b[X]=0;b[X]<=n;b[X]++)
        for(b[Y]=0;b[Y]<=m;b[Y]++)
        for(c[X]=0;c[X]<=n;c[X]++)
        for(c[Y]=0;c[Y]<=m;c[Y]++){
            if(Area2(a,b,c)==A){
                printf("%d %d %d %d %d %d",a[X],a[Y],b[X],b[Y],c[X],c[Y]);
                pos=true;
                goto sal;
            }
        }
sal:    if(!pos) printf("IMPOSSIBLE");
        printf("\n");        
    }
}
