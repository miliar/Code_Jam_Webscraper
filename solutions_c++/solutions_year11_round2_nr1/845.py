#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <string>
using namespace std;
int n,ntest;
string s[111];

double a[111], b[111], c[111];


double cal(int i){
    int u = 0 , v = 0;
    for(int j = 0;j<n;j++)
      if (s[i][j] != '.') {
            v++;
            if (s[i][j] == '1') u++;   
        }
    if (v == 0) return 0;
    return u*1.0/v;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> ntest;
    for(int r = 0;r<ntest;r++){
    cout << "Case #"<< r+1 <<":" ;
    cin >> n;
    
    memset(a,0,sizeof(a));
    memset(b,0,sizeof(b));
    memset(c,0,sizeof(c));
    
    for(int i = 0;i<n;i++) cin >> s[i];
    
    for(int i = 0;i<n;i++) {
       if (i==1) 
        cout << endl; 
      a[i] = cal(i);
      double w = 0;
      int cnt = 0;
      for(int j = 0;j<n;j++) if (j!=i) {            
            if (s[i][j] != '.'){
                char now = s[j][i];
                cnt++;
                s[j].replace(i,1,1,'.');                
                w += cal(j);
                s[j].replace(i,1,1,now);
            }                  
      }
      if (cnt ==0 ) b[i] = 0;else
      b[i] = w/cnt;
      
    }    
    for(int i = 0;i<n;i++){
        int cnt = 0;
        for(int j = 0;j<n;j++)
         if (s[i][j] != '.'){
                  cnt ++;
                  c[i] += b[j];
            }
        if (!cnt) c[i] = 0; else        c[i] /= cnt;
        double res = 0.25 * a[i] + 0.5 * b[i] + 0.25 * c[i];
//        printf("%.10lf %.10lf %.10lf \n",a[i],b[i],c[i]);      
        printf("%.10lf\n",res);     
    }
    }
       
    return 0;
}
