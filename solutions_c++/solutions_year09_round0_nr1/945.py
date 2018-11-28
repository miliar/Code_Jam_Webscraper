#include<iostream>
#include<vector>
#include<set>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("x.out","w",stdout);
    int l,d,n;
    scanf("%d %d %d\n",&l,&d,&n);
    string s;
    vector<string> D;
    for(int i=0;i<d;++i)
        getline(cin,s),D.push_back(s);
    for(int i=0;i<n;++i){
        getline(cin,s);
        int state=0,m=0,res=0;
        vector<set<char> > p;
        for(int j=0;j<s.size();++j)
            switch(s[j]){
                case '(':
                    state=1;
                    break;
                case ')':
                    state=0;
                    break;
                default:
                    if(state!=2){
                        if(state==1)state=2;
                        p.push_back(set<char>());
                        m++;
                    }
                    if(!p[m-1].count(s[j]))
                        p[m-1].insert(s[j]);
                    break;
            }
        if(m==l)
            for(int j=0,k;j<d;++j){
                for(k=0;k<l;++k)
                    if(!p[k].count(D[j][k]))
                        break;
                if(k==l)res++;
            }
        printf("Case #%d: %d\n",i+1,res);
    }
    return 0;
}
