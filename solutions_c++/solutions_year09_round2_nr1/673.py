#include<iostream>
#include<vector>
#include<set>
#include<ctype.h>

using namespace std;

int n,tn;
char tree[10000],pc[1000];
vector<pair<string,double> > tr;
set<int> Q;

double f(int i,set<string> a){
    if(!Q.count(i))return 1;
    double res=tr[i].second;
    if(a.count(tr[i].first))res*=f(2*i,a);
    else res*=f(2*i+1,a);
    return res;
}

int miss_white(int k){
    for(;isspace(tree[k]);k++);
    return k;
}

int parse(int k,int p){
    k=miss_white(k);
    if(tree[k]!='(')return -1;
    k=miss_white(k+1);
    if(!isdigit(tree[k]))return -1;
    double w=0;
    for(;k<n&&isdigit(tree[k]);++k)
        w=w*10+tree[k]-'0';
    if(tree[k]=='.'){
        double q=0,b=10;
        for(k++;k<n&&isdigit(tree[k]);++k,b*=10)
            q+=(tree[k]-'0')/b;
        w+=q;
    }
    k=miss_white(k);
    int l=0;
    for(;k<n&&!isspace(tree[k])&&tree[k]!=')';++k)
        pc[l++]=tree[k];
    pc[l]=0;
    string feach=(string)pc;
    if(tr.size()<p+1)tr.resize(p+1);
    tr[p]=make_pair(feach,w);
    Q.insert(p);
    k=miss_white(k);
    if(tree[k]==')')return miss_white(k+1);
    k=parse(parse(k,2*p),2*p+1);
    if(tree[k]!=')')return -1;
    return miss_white(k+1);
}

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc;
    scanf("%d\n",&tc);
    for(int t=1;t<=tc;++t){
        int l;
        scanf("%d\n",&l);
        string s;
        n=0;
        for(int i=0;i<l;++i){
            getline(cin,s);
            for(int j=0;j<s.size();++j)
                tree[n++]=s[j];
        }
        tree[n]=0;
        tr.resize(0);
        Q.clear();
        if(parse(0,1)!=n)
            cout<<"FUCK"<<endl;
        tn=tr.size();
        int k;
        scanf("%d\n",&k);
        string name;
        int c;
        printf("Case #%d:\n",t);
        for(int i=0;i<k;++i){
            cin>>name>>c;
            string ss;
            set<string> animal;
            for(int j=0;j<c;++j){
                cin>>ss;
                animal.insert(ss);
            }
            printf("%.7lf\n",f(1,animal));
        }
    }
    return 0;
}
