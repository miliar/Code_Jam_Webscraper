#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
char A[100][100];
int P[100];
int G[100];
double W[100];
double O[100];
double OO[100];
int main(){
    int nc;
    cin>>nc;
    for(int k=0;k<nc;k++){
        int n;
        cin>>n;
        memset(P,0,sizeof(P));
        memset(G,0,sizeof(G));
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cin>>A[i][j]; 
            }    
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(A[i][j]!='.'){
                    P[i]++;
                    if(A[i][j]=='1')G[i]++;    
                }
            }
            if(P[i])W[i]=(1.*G[i])/P[i];
            else W[i]=0;
        }
        for(int i=0;i<n;i++){
            double ac=0.;
            int ct=0;
            //cout<<i<<endl;
            for(int j=0;j<n;j++){
                if(A[i][j]!='.'){
                    ct++;
                    if(A[i][j]=='1'){
                        if(P[j]>1)ac+=((G[j])*1.)/(P[j]-1);
                    }
                    else{
                        if(P[j]>1)ac+=(1.0*(G[j]-1))/(P[j]-1);   
                    }
                    //cout<<G[j]<<" "<<P[j]<<" "<<ac<<" "<<A[i][j]<<" "<<(1.0*(G[j]-1))/(P[j]-1)<<endl;
                }
            }
            O[i]=ac/ct;
        }
        for(int i=0;i<n;i++){
            double ac=0.;
            int ct=0;
            for(int j=0;j<n;j++){
                if(A[i][j]!='.'){
                    ac+=O[j];
                    ct++;    
                }
            }
            OO[i]=ac/ct;
        }
        cout<<"Case #"<<k+1<<":"<<endl;
        for(int i=0;i<n;i++){
            //cout<<W[i]<<" "<<O[i]<<" "<<OO[i]<<endl;
            cout<<0.25*W[i] + 0.50*O[i] + 0.25*OO[i]<<endl;
        }
    }    
}
