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

char mat[105][105];
double wp[105];
double owp[105];
double oowp[105];

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d:\n",tt);
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%s",mat[i]);
        
        for(int i=0;i<n;i++){
            double tot=0,win=0;
            for(int j=0;j<n;j++)
                if(mat[i][j]!='.'){
                    tot++;
                    if(mat[i][j]=='1')
                        win++;
                }
            wp[i]=0;
            if(tot!=0) wp[i]=win/tot;
        }
        
        for(int i=0;i<n;i++){
            double tot=0,win=0;
            for(int j=0;j<n;j++)
                if(mat[i][j]!='.'){
                    double tot2=0,win2=0;
                    for(int k=0;k<n;k++)
                        if(k!=i&&mat[j][k]!='.'){
                            tot2++;
                            if(mat[j][k]=='1')
                                win2++;
                        }
                    
                    if(tot2!=0) win+=win2/tot2;
                    tot++;
                }
            owp[i]=0;
            if(tot!=0) owp[i]=win/tot;
        }
        
        for(int i=0;i<n;i++){
            double tot=0,win=0;
            for(int j=0;j<n;j++)
                if(mat[i][j]!='.'){
                    win+=owp[j];
                    tot++;
                }
            oowp[i]=0;
            if(tot!=0) oowp[i]=win/tot;
        }
        
        for(int i=0;i<n;i++)
            printf("%.12lf\n",wp[i]*.25+owp[i]*.5+oowp[i]*.25);
        
    }

    return 0;
}
