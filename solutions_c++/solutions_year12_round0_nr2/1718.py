/* 
 * File:   main.cpp
 * Author: Tarun
 *
 * Created on April 14, 2012, 12:13 PM
 */

#include <cstdlib>
#include<cstdio>
#include<iostream>
#include<math.h>
#include<vector>
#include<map>
#include<string.h>
#include<queue>
#include<algorithm>
#include<string.h>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef unsigned long long ulint;
typedef long long lint;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

int main() {
    int m;
    FILE *fi;
    FILE *fo;
    fi = fopen("input.txt","r");
    fo = fopen("output.txt","w+");
    fscanf(fi,"%d", &m);
    
    for(int i=1;i<=m;i++) {
        int n,s,p;
        fscanf(fi,"%d%d%d",&n,&s,&p);
        int *t = new int[n];
        int mx = (p-1)*3+1;
        int mn = mx-2;
        if(p==1) mn=1,mx=1;
        else if(p==0) mn=0,mx=0;
        int mncount=0;
        int mxcount=0;
        for(int i=0;i<n;i++)
        {
            int x;
            fscanf(fi,"%d",&x);
            if(x>=mx) mxcount++;
            else if (x>=mn) mncount++;
        }
        mncount=min(mncount,s);
        fprintf(fo,"Case #%d: %d\n",i,mxcount+mncount);
    }
        cout<<"chk";
    fclose(fo);
    fclose(fi);
    return 0;
}
