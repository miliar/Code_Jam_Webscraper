using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

# define PI 3.14159265

int main() {
    int i,j,t,len,cs=0,ind;
    char in[111], out[111];
    char str[30]="yhesocvxduiglbkrztnwjpfmaq";
    scanf("%d",&t);
    cin.getline(in,111);
    while(t--) {
         cs++;
         cin.getline(in,111);
         len=strlen(in);
         for(i=0;i<len;i++) {
               if(in[i]!=' ') {
                      ind=in[i]-'a';
                      out[i]=str[ind];
               }
               else out[i]=' ';
         }
         out[i]='\0';
         printf("Case #%d: %s\n",cs,out);
    }
    return 0;
}

                                       
         
               
    
