/*
Program:
Author: ldl
Method:
DataStructure:
Date: 2010- -
Status:
Remark:
*/
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int n,m,ans;
char s[1000];
map<string,int> data;

void work(bool flag){
    scanf("%s", s);
    int len = strlen(s);
    if (len == 1) return;
    int k = 1;
    while(k < len){
        if (s[k] == '/' || k == len - 1){
            int p = k;
            if (k == len - 1) p++;
            if (flag) data[string(s,p)] = 1;
              else if (!data[string(s,p)]) {
                 ans++;
                 data[string(s,p)] = 1;
              }
        }
        k++;
   }
}

int main(){
//    freopen("test.txt","r",stdin);
    int T;
    scanf("%d", &T);
    for (int p = 1; p <= T ; p++)
    {
       scanf("%d%d", &n , &m);
       printf("Case #%d: ", p);
       data.clear();
       ans = 0;
       for (int i = 0; i < n ; i++)
           work(true);
       for (int i = 0; i < m ; i++)
           work(false);
       printf("%d\n", ans);
      
    }
    return 0;
}
  
