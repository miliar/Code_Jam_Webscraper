#include <iostream>
#include <cstdio>
#include <map>
#include <math.h>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
#define For(i,a,b) for (i=a;i!=b;i++)
#define Rep(i,n) For(i,0,n)
#define set(a,c) memset(a,c,sizeof(a))
#define pb push_back
#define GI ({int t;scanf("%d",&t);t;})
typedef pair<string,string> SS;
vector<int> arrA, arrB;
vector<SS> timA, timB;
int toint(string X) {
    int a = (X[0]-'0') * 10 + X[1]-'0';
    int b = (X[3]-'0') * 10 + X[4]-'0';
    return a*60+b;
}
int main() {
    int t = GI, test;
    string tim1, tim2;
    Rep (test,t) {
          int T = GI;
          int NA = GI, NB = GI, i;
          timA.clear();
          timB.clear();
          arrA.clear();
          arrB.clear();
          Rep(i,NA) {
               cin>>tim1;
               cin>>tim2;
               timA.pb(SS(tim1,tim2));
          }
          Rep(i,NB) {
               cin>>tim1;
               cin>>tim2;
               timB.pb(SS(tim1,tim2));
          }
          sort(timA.begin(),timA.end());
          sort(timB.begin(),timB.end());
          int cntA = 0, cntB = 0;
          int ansA = 0,ansB = 0;
          while (cntA < NA && cntB < NB) {
                if (timA[cntA] <= timB[cntB]) {
                   int n = arrA.size();
                   Rep(i,n) {
                       if (arrA[i] <= toint(timA[cntA].first) - T) {
                                   arrA.erase(arrA.begin()+i);
                                   break;
                       }
                   }
                   if (i == n) {
                         ansA++;
                   }
                   arrB.push_back(toint(timA[cntA].second));
                   cntA++;
                   continue;
                }
                int n = arrB.size();
                Rep(i,n) {
                    if (arrB[i] <= toint(timB[cntB].first) - T) {
                       arrB.erase(arrB.begin()+i);
                       break;
                    }
                }
                if (i == n) {
                   ansB++;
                }
                arrA.push_back(toint(timB[cntB].second));
                cntB++;
          }
          if (cntA < NA)
          {
                   while (cntA < NA) {
                          int n = arrA.size();
                          Rep(i,arrA.size()) {
                              if (arrA[i] <= toint(timA[cntA].first) - T) {
                                   arrA.erase(arrA.begin()+i);
                                   break;
                              }
                          }
                          if (i == n) {
                             ansA++;
                          }
                          cntA++;
                   }
          }
          else
          {
              while (cntB < NB) {
                          int n = arrB.size();
                          Rep(i,arrB.size()) {
                              if (arrB[i] <= toint(timB[cntB].first) - T) {
                                   arrB.erase(arrB.begin()+i);
                                   break;
                              }
                          }
                          if (i == n) {
                             ansB++;
                          }
                          cntB++;
              }
          }
          cout << "Case #" << test+1 <<": "
               << ansA << " " << ansB << endl;
    }
    // system("pause");
}
