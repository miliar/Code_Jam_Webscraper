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
typedef long long ll;
typedef double point[2];
typedef point polygon[1000005];
#define X 0
#define Y 1

#define E 0
#define N 1
#define W 2
#define S 3

int dy[4]={0,1,0,-1};
int dx[4]={1,0,-1,0};
int lef[4]={N,W,S,E};
int rig[4]={S,E,N,W};

polygon P;

bool InPoly(point &q,int n){
int rcross,lcross,i1; rcross=lcross=0;
bool rstrad,lstrad;
double x;
for(int i=0;i<n;i++){
//El punto es un vertice
if(P[i][X]==q[X]&&P[i][Y]==q[Y])
return true;
i1=(i-1+n)%n;
rstrad=(P[i][Y]>q[Y])!=(P[i1][Y]>q[Y]);
lstrad=(P[i][Y]<q[Y])!=(P[i1][Y]<q[Y]);
if(rstrad||lstrad){
x=(q[Y]*(P[i][X]-P[i1][X])
-P[i1][Y]*P[i][X]
+P[i1][X]*P[i][Y])/
(P[i][Y]-P[i1][Y]);
if(rstrad&&x>q[X]) rcross++;
if(rstrad&&x<q[X]) lcross++;
}
}
//El punto esta en una arista
if((rcross%2)!=(lcross%2)) return true;
//Estrictamente interior
if((rcross%2)==1) return true;
else return false;
}

#define M 105

int arr[5005][5005];

int main(){
    int test;
    scanf("%d",&test);
    for(int t=0;t<test;t++){
        printf("Case #%d: ",t+1);
        string pat;
        string s;
        int rep;
        int nn;
        cin>>nn;
        for(int i=0;i<nn;i++){
            cin>>s>>rep;
            for(int  j=0;j<rep;j++)
                pat+=s;
        }
        int cx,cy,cdir=N;
        cx=cy=0;
        int n=1;
        P[0][X]=P[0][Y]=0;
        for(int i=0,sz=pat.size();i<sz;i++){
            switch(pat[i]){
                case 'F': cx+=dx[cdir];
                          cy+=dy[cdir];
                          break;
                case 'L': 
                        P[n][X]=cx;
                        P[n][Y]=cy;
                        n++;
                        cdir=lef[cdir];
                        break;
                case 'R':
                        P[n][X]=cx;
                        P[n][Y]=cy;
                        n++;
                        cdir=rig[cdir];
                        break;
            }
        }
        
        /*double total=0.0;
        
        for(int i=0;i<n;i++){
            int j=(i+1)%n;
            total+=P[i][X]*P[j][Y]-P[j][X]*P[i][Y];
        }
        
        
        if(total<0) {
            point temp;
            for(int i=0;i<n/2;i++){
                temp[X]=P[i][X]; temp[Y]=P[i][Y];
                P[i][X]=P[n-1-i][X];  P[i][Y]=P[n-1-i][Y];
                P[n-1-i][X]=temp[X];  P[n-1-i][Y]=temp[Y];
            }
        }*/
        
        for(int i=0;i<n;i++){
            //cout<<P[i][X]<<' '<<P[i][Y]<<endl;
            P[i][X]+=M;
            P[i][Y]+=M;
        }
        memset(arr,0,sizeof(arr));
        for(int i=0;i<2*M;i++)
            for(int j=0;j<2*M;j++){
                point pmed;
                pmed[X]=double(i)+.5;
                pmed[Y]=double(j)+.5;
                if(InPoly(pmed,n)){                    
                    arr[i][j]=1;
                    //cout<<"=="<<i<<' '<<j<<endl;
                }             
            }
        
        
        int res=0;
        
        for(int i=0;i<2*M;i++)
            for(int j=0;j<2*M;j++)
                if(!arr[i][j]){
                    bool found=false;        
                    for(int k=0;k<i;k++) if(arr[k][j]) {found=true; break;}
                    if(!found) goto nex;
                    found=false;
                    for(int k=i+1;k<2*M;k++) if(arr[k][j]) {found=true; break;}
                    if(!found) goto nex;
                    res++; continue;

nex:
                    found=false;
                    for(int k=0;k<j;k++) if(arr[i][k]) {found=true; break;}
                    if(!found) continue;
                    found=false;
                    for(int k=j+1;k<2*M;k++) if(arr[i][k]) {found=true; break;}
                    if(!found) continue;

                    res++;                    
                }
        printf("%d\n",res);
    }
}
