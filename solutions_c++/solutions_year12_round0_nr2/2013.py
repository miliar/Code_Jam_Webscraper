#include <iostream>
#include <bitset>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <cctype>
#include <set>
#include <cmath>
#include <climits>
#include <sstream>
#include <fstream>
#include <list>
#include <functional>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define SZ size()
#define pp push_back

typedef long long LL;
typedef vector <int> vi;
typedef vector <double> vd;
typedef vector <vi> vvi;
typedef vector <string> vs;
typedef pair<int,int> pii;
typedef vector <LL> vll;

int arr[105];

int main() {
    freopen("dancing.in","r",stdin);
    freopen("dancing.out","w",stdout);
    int n,s,p,tc;
    int div;
    int res;
    bool found;
    scanf("%d",&tc);
    for(int i=0;i<tc;i++) {
            scanf("%d %d %d",&n,&s,&p);
            res = 0;
            for(int j=0;j<n;j++) {
                    scanf("%d",&arr[j]);
                    div=arr[j]/3;
                    found = false;
                    for(int k=0;k<6;k++) {
                            if(k == 0) {
                                 if(div*3 == arr[j]) { 
                                          if(div >= p) {
                                                 res++; 
                                                 found = true; 
                                                 break;
                                          }
                                 }     
                            }            
                            else if(k == 1) {
                                 if(div + (div+1) + (div+1) == arr[j]) { 
                                        if((div+1) >= p) {
                                                   res++; 
                                                   found = true; 
                                                   break;
                                        }
                                 }
                            }
                            else if(k==2) {
                                 if(div + (div) + (div+1) == arr[j]) { 
                                        if((div+1) >= p) {
                                                   res++; 
                                                   found = true; 
                                                   break;
                                        }
                                 }
                            }
                            else if(k==3) {
                                 if(div + (div-1) + (div-1) == arr[j] && (div-1) >= 0) { 
                                        if((div) >= p) {
                                                   res++; 
                                                   found = true; 
                                                   break;
                                        }
                                 }
                            }
                            else if(k==4) {
                                 if(div + (div) + (div-1) == arr[j] && (div-1) >= 0) { 
                                        if((div) >= p) {
                                                   res++; 
                                                   found = true; 
                                                   break;
                                        }
                                 }
                            }
                            else if(k==5) {
                                 if((div-1) + (div-1) + (div-1) == arr[j] && (div-1) >= 0) { 
                                        if((div-1) >= p) {
                                                   res++; 
                                                   found = true; 
                                                   break;
                                        }
                                 }
                            }
                    }
                    if(!found) {
                               for(int k=0;k<6;k++) {
                                       if(k == 0) {
                                            if(div + (div+1) + (div+2) == arr[j] && s) { 
                                                   if((div+2) >= p) {
                                                              res++; 
                                                              s--; 
                                                              found = true; 
                                                              break;
                                                   }
                                            }     
                                       }            
                                       else if(k == 1) {
                                            if(div + (div+2) + (div+2) == arr[j] && s) { 
                                                   if((div+2) >= p) {
                                                              res++; 
                                                              s--; 
                                                              found = true; 
                                                              break;
                                                   }
                                            }
                                       }
                                       else if(k == 2) {
                                            if(div + (div) + (div+2) == arr[j] && s) { 
                                                   if((div+2) >= p) {
                                                              res++; 
                                                              s--; 
                                                              found = true; 
                                                              break;
                                                   }
                                            }
                                       }
                                       else if(k == 3) {
                                            if(div + (div-2) + (div-2) == arr[j] && s && (div-2) >= 0) { 
                                                   if((div) >= p) {
                                                              res++; 
                                                              s--; 
                                                              found = true; 
                                                              break;
                                                   }
                                            }
                                       }
                                       else if(k == 4) {
                                            if(div + (div) + (div-2) == arr[j] && s && (div-2) >= 0) { 
                                                   if((div) >= p) {
                                                              res++; 
                                                              s--; 
                                                              found = true; 
                                                              break;
                                                   }
                                            }
                                       }
                                       
                                       else if(k==5) {
                                            if((div) + (div-1) + (div+1) == arr[j] && s && (div-1) >= 0) { 
                                                     if((div+1) >= p) {
                                                                res++; 
                                                                s--;
                                                                found = true; 
                                                                break;
                                                     }
                                            }
                                       }
                                       
                               }                    
                    }
            }
            printf("Case #%d: %d\n",i+1,res);
    }
}
