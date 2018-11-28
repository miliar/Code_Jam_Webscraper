/*  File: main.cpp  Author: Administrator Created on 2010年5月8日, 上午6:55 */

#include <stdlib.h>
#include<iostream>
#include<stdio.h>
using namespace std;

int main(int argc, char** argv) {
    int n,k,ca,T;
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>T;
    while(T--){
        cin>>n>>k;
        printf("Case #%d: ",++ca);
        int t=(1<<n);
        if((k%t==t-1)) printf("ON\n");
        else printf("OFF\n");
    }
    return (EXIT_SUCCESS);
}/*Sample

Input

Output

4
1 0
1 1
4 0
4 47
 Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON


*/

