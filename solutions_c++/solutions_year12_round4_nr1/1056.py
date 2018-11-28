/* 
 * File:   main.cpp
 * Author: Tarun
 *
 * Created on May 26, 2012, 7:11 PM
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
    int t;
    FILE *fi = new FILE;
    FILE *fo = new FILE;
    fi = fopen("input.txt","r");
    //fi = stdin;
    fo = fopen("output.txt","w");
    fscanf(fi,"%d", &t);
    for(int i=1;i<=t;i++) {
        int n;
        fscanf(fi,"%d",&n);
        ii *wn = new ii[n+1];
        for(int i=0;i<n;i++)
        {
            int d,l;
            fscanf(fi,"%d%d",&d,&l);
            wn[i].first = d;
            wn[i].second = l;
        }
        fscanf(fi,"%d",&(wn[n].first));
        wn[n].second = 1000000007;
        sort(wn,wn+n);
        int **reach = new int*[n];
        for(int i=0;i<n;i++) reach[i]= new int[2];
        reach[0][0] = wn[0].first;
        wn[0].second = min(wn[0].first,wn[0].second);
        int j=0;
        for(int i=1;i<=n;i++)
        {
            bool b = 0;
            for(;j<i;j++)
            {

                if(wn[j].first+wn[j].second>=wn[i].first) {wn[i].second = min(wn[i].second,wn[i].first-wn[j].first);b=1; break;}
            }
            if(!b) wn[i].second =-1;
        }
        if(wn[n].second!=-1) fprintf(fo,"Case #%d: YES\n",i);

        else fprintf(fo,"Case #%d: NO\n",i);
    } 

    fclose(fi);
    fclose(fo);
    return 0;
}
