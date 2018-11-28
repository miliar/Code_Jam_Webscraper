/* 
 * File:   main.cpp
 * Author: Tarun
 *
 * Created on April 14, 2012, 11:13 AM
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
    char *s = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char *y = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    map<char , char> ch;
    int len = strlen(s);
    FILE *fi;
    fi = fopen("input.txt","r");
    FILE *fo;
    fo = fopen("output.txt","w+");
    for(char c='a';c<='z';c++)
    {
        ch[c]=c;
    }
    for(int i=0;i<len;i++) {
        ch[s[i]]=y[i];
    }
    ch['z']='q';
    ch['q']='z';
    ch[' ']=' ';
    for(map<char,char>::iterator ii=ch.begin();ii!=ch.end();ii++)
    {
        cout<<ii->first<<" "<<ii->second<<endl;
    }
    int n;
    fscanf(fi,"%d",&n);
    for(int i=1;i<=n;i++)
    {
        char *str = new char[1000];
        fscanf(fi,"\n%[^\n]",str);
        int len = strlen(str);
        cout<<len;
        for(int i=0;i<len;i++)
        str[i]=ch[str[i]];
        fprintf(fo,"Case #%d: %s\n",i,str);
        printf("Case #%d: %s\n",i,str);
    }
    fclose(fi);
    fclose(fo);
    system("pause");
    return 0;
}
