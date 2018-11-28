// Author: Adam Polak
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cmath>
#include <ctime>
#include <cstdlib>
using namespace std;
const int NIL = (-1);

#define REP(i,n) for(int i=0;i<(n);i++)
#define SIZE(c) ((int)((c).size()))

#define mp make_pair
#define st first
#define nd second
#define pb push_back

const int T = 80*100+10;

int m,l[T],r[T];
double val[T];
string fet[T];

char buf[T];
int buf_l,it;

void read_node(int i) {
    l[i]=r[i]=NIL;

    if (buf[it]!='(') { //assert
        printf("\nERROR reading node %d; it=%d\n",i,it);
        _exit(1);
    }
    int nxt=it+1;
    string tmp="";
    while((buf[nxt]>='0'&&buf[nxt]<='9')||buf[nxt]=='.') tmp+=buf[nxt++];
    sscanf(tmp.c_str(),"%lf",&val[i]);

    it = nxt;
    if (buf[it]==')') {it++;return;}
    
    tmp="";
    nxt=it; while(buf[nxt]>='a'&&buf[nxt]<='z') tmp+=buf[nxt++];
    fet[i]=tmp;
    it=nxt;
    l[i]=m++; r[i]=m++;
    read_node(l[i]); read_node(r[i]);
    it++;
}

void show_node(int i) {
//    printf("%d: %lf\t'%s'\t%d %d\n",i,val[i],fet[i].c_str(),l[i],r[i]);
//  if (l[i]!=NIL) {show_node(l[i]),show_node(r[i]);}
}
   
set<string> s;

double go(int i) {
    if (l[i]==NIL) return val[i];
    if (s.find(fet[i])==s.end()) 
        return val[i]*go(r[i]);
    else 
        return val[i]*go(l[i]);
}


void scase(int case_num) {
    printf("Case #%d:\n",case_num);

    int l; scanf("%d\n",&l);
  //  printf("l=%d\n",l);
    buf_l=0;
    REP(i,l) {
        char c;
        while(1) {
            scanf("%c",&c);
            if (c==' ') continue;
            if (c=='\n') break;
            buf[buf_l++]=c;
        }
    }
    it = 0;
    m = 1;
    //buf[buf_l]=0;printf("%s\n",buf);
    read_node(0);
    //show_node(0);
    int a; scanf("%d",&a);
    while(a--) {
        scanf("%s",buf);
        int q; scanf("%d",&q);
        s.clear();
        while(q--) {
            scanf("%s",buf); 
            s.insert(string(buf));
        }
        printf("%0.7lf\n",go(0));
    }

}

int main() {
    int cases; 
    scanf("%d",&cases);
    //cin >> cases;
    REP(case_num,cases) scase(case_num+1);
    return 0;
}

    
