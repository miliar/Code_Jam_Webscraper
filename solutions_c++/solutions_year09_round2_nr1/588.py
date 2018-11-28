#include <iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<map>
#include<vector>
#include<cctype>
#include<set>
#include<sstream>
#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;
char td[10000];
struct tok{
    int typ;
    string s;
    double d;
    tok *L,*R;
};
tok* lpar() {
    tok* a=new tok();
    a->typ=0;
    a->L=0;
    a->R=0;
    return a;
}
tok* rpar() {
    tok* a=new tok();
    a->typ=1;
    a->L=0;
    a->R=0;

    return a;
}
tok* num(double d) {
    tok* a=new tok();
    a->typ=2;
    a->L=0;
    a->R=0;
    a->d=d;
    return a;
}
tok* stri(string d) {
    tok* a=new tok();
    a->typ=3;
    a->L=0;
    a->R=0;
    a->s=d;
    return a;
}
int ptr;
vector<tok*> v;
tok* parse(tok *x){
   //  printf("ptr=%d %d\n",ptr,v.size());
   //  printf("%d \n",v[ptr]->typ);

    x->d=v[ptr+1]->d;
    if (v[ptr+2]->typ==1) {
        ptr+=3;
        return v[ptr-2];
    } else {
        x->s=v[ptr+2]->s;
        ptr+=3;
        x->L=parse(v[ptr]);
        x->R=parse(v[ptr]);
        ptr++;
    }
    return x;
}
set<string> fs;
double go(tok *x) {

    double rval=x->d;
    if (x->R && x->L) {
        if(fs.find(x->s)==fs.end()) {
            rval*=go(x->R);
        } else {
            rval*=go(x->L);
        }
    }
    return rval;

}
int main()
{
    int N,L;
    char p[3100];
    gets(p);
    sscanf(p,"%d",&N);
    REP(cc,N) {
        v.clear();
        gets(p);
        ptr=0;
        sscanf(p,"%d",&L);
        REP(i,L) {
            gets(p);
            strcpy(td+ptr,p);
            ptr+=strlen(p);
        }
        ptr=0;
       // printf("td=%s\n",td);
        while(td[ptr]) {
            if (td[ptr]=='(') {v.push_back(lpar());  ptr++;continue;}
            if (td[ptr]==')') {v.push_back(rpar());  ptr++;continue;}
            if (td[ptr]==' ' || td[ptr]=='\n') {ptr++;continue;}
            sscanf(td+ptr,"%[^) ]",p);
            double x;
            if(sscanf(p,"%lf",&x)==1) {
                v.push_back(num(x));
            } else {
                v.push_back(stri(p));
            }
            ptr+=strlen(p);
        }
        ptr=0;
        //printf("OK\n");
        parse(v[0]);
        //printf("!!!OK\n");

        gets(p);
        int A;
        sscanf(p,"%d",&A);
        printf("Case #%d:\n",cc+1);
        REP(oo,A) {
            gets(p);
            fs=set<string>();
            istringstream ss(p);
            int cnt;
            string s;
            ss>>s;
            ss>>cnt;
            REP(i,cnt) {
                ss>>s;
                fs.insert(s);
            }
            double ans=0;
            ans=go(v[0]);
            printf("%.7lf\n",ans);
        }
        REP(i,v.size()) delete v[i];
        v.resize(0);



    }
    return 0;
}
