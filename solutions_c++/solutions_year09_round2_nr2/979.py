#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> num;
vector<int> next;

int main () {
    int t,n,i,j,k,l,min,pos,mark,gg;
    string s;
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    scanf ("%d\n",&t);
    for (i=1;i<=t;i++) {
        num.clear();
        next.clear();
        mark = 0;
        printf ("Case #%d: ",i);  
        getline(cin,s);
        l = s.length();
        for (j=0;j<l;j++)
            num.push_back(s[j]-48);
        pos = 0;
        for (j=l-2;j>=0;j--) {
            if (num[j]>=num[j+1]) continue;
            //printf ("%d\n",j);
            pos = j+1;
            for (k=l-1;k>=pos;k--) {
                if (num[k]>num[j]) {
                   swap(num[k],num[j]);
                   mark = 1;           
                   break;        
                }    
            }
            break;
        }
        if (mark==1)
           for (j=pos;j<l;j++) next.push_back(num[j]);
        else {
             for (j=l-1;j>=0;j--)
                 if (num[j]>0) {
                    swap (num[0],num[j]);
                    num[0] *= 10;
                    pos= 1;
                    break;              
                 }    
             for (j=1;j<l;j++) next.push_back(num[j]);
        }     
        sort (next.begin(),next.end());
        for (j=0;j<pos;j++) printf ("%d",num[j]);
        for (j=0;j<next.size();j++) printf ("%d",next[j]);
        printf ("\n");
    }
    return 0;   
}
