#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
using namespace std;
int main(){
int test, cas;
cin >> test;
for (cas=1; cas<=test; ++cas){
    int a, b;
    cin >> a >> b;
    int cnt = 0;
    for (int i=a; i<=b; i++){
        char cstr[10];
        memset(cstr,0,sizeof(cstr));
        sprintf(cstr, "%d", i);
        int len = strlen(cstr);
        vector<int> kk;
        kk.clear();
        for (int j=1; j<len; ++j){
            char c=cstr[0];
            for (int k=1; k<len; ++k) cstr[k-1]=cstr[k];
            cstr[len-1]=c;
            int k = atoi(cstr);
            bool flag=false;
            for (int kkk=0;kkk<kk.size();++kkk) if (k==kk[kkk]) { flag=true; break; }
            if (flag) continue;
            kk.push_back(k);
            if (k>=a&&k<=b&&i<k) cnt++;
        }
//        if (i==1212) for (int j=0; j<kk.size();++j) cout <<"j:"<<kk[j]<<endl;
    }
    cout << "Case #" << cas << ": " << cnt << endl;
}
}
