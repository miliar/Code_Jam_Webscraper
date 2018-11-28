/*
 * File:   main.cpp
 * Author: Tarun
 *
 * Created on April 14, 2012, 1:04 PM
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
    int n;
    FILE *fi;
    FILE *fo;
    fi = fopen("input.txt","r");
    fo = fopen("output.txt","w+");
    //fi = stdin;
    //fo = stdout;
    fscanf(fi,"%d", &n);
    for(int i=1;i<=n;i++) {
        int a,b;
        fscanf(fi,"%d%d",&a,&b);
        int count=0;
        bool *chk=new bool[b+1];
        for(int i=a;i<=b;i++) chk[i]=0;
            //cout<<"chk";
            int k=10;
        for(int j=a;j<=b;j++)
        {
            if(chk[j]) continue;
            int x = j;
            int cnt=0;
            while(k<=x) k*=10;
            do {
                //cout<<x<<" "<<k<<endl;
                if(x<=b) chk[x]=1;
                if(x>=a&&x<=b)cnt++;
                int y=x%10;
                x+=y*k;
                x/=10;
            }while(x!=j);
            //cout<<endl;
            count+=(cnt*(cnt-1))/2;
        }
        fprintf(fo,"Case #%d: %d\n",i,count);
    }
    fclose(fi);
    fclose(fo);
    system("pause");
    return 0;
}
