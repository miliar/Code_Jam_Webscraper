#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <algorithm>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)

using namespace std;

char ST[30];
char RES[30];

int main(){
  int CN;
  cin >> CN;
  For1(CI,CN){
    string str;
    cin >> str;
    memset(ST, 0, sizeof(ST));
    strcpy(ST, str.c_str());

    int p;
    for(p=str.size()-1;p>0;p--){
      if(ST[p-1]<ST[p]){
        char mm=ST[p];
        int rmmp=p;
        int mmp;
        //search minmore
        for(mmp=p;mmp<str.size();mmp++){
          if(ST[mmp]>ST[p-1] && ST[mmp]<mm){
            mm=ST[mmp];
            rmmp = mmp;
          }
        }
        ST[rmmp]=ST[p-1];
        ST[p-1]=mm;
        sort(ST+p,ST+str.size());
        break;
      }
    }
    if(p<=0){
      ST[str.size()]='0';
      sort(ST,ST+str.size()+1);
      int i;
      for(i=0;ST[i]=='0';i++);
      ST[0]=ST[i];
      ST[i]='0';
    }


    cout << "Case #" << CI << ": ";
    printf(ST);
    cout << endl;
  }
}
