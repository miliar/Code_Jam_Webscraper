#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<sstream>
#include<map>
#define MAXN (1<<20)
using namespace std;
struct node
{
    double w8;
    string feat;
    int lf,rt;
} A[MAXN];
node make_node(double a1,string a2,int a3,int a4)
{
    node w;
    w.w8=a1;
    w.feat=a2;
    w.lf=a3;
    w.rt=a4;
    return w;
}
pair<double,string> parse(string a)
{
    while(1)
    {
        if(a[0]>='0'&&a[0]<='9')break;
        a.erase(a.begin());
    }
    istringstream iss(a, istringstream::in);
    double g;
    string h;
    iss>>g>>h;
    if(h.length()==0||h[0]<'a'||h[0]>'z')h.clear();
    return make_pair(g,h);
}
void input(int ind)
{
    string L;
    pair<double,string> wTf;
    while(1)
    {
        getline(cin,L);
        for(int i=0;i<L.size();++i)if(L[i]=='(')goto bb;
    }
    bb:
    wTf=parse(L);
    if(L[L.size()-1]==')')A[ind]=make_node(wTf.first,wTf.second,-1,-1);// a leaf
    else
    {
        A[ind]=make_node(wTf.first,wTf.second,2*ind+1,2*ind+2);
        input(2*ind+1);
        input(2*ind+2);
    }
}
map<string,bool> ET;
double go(int ind)
{
    if(A[ind].lf==-1)return A[ind].w8;
    if(ET[A[ind].feat])return A[ind].w8*go(2*ind+1);
    else return A[ind].w8*go(2*ind+2);
}
int pr2(string a)
{
    istringstream iss(a, istringstream::in);
    int r;
    iss>>r;
    return r;
}
int main()
{
    int i,j,k,T,lv,nv;
    string u;
    cin>>T;
    for(k=0;k<T;++k)
    {
        scanf("%d\n",&lv);
        input(0);
        while(1)
        {
            cin>>u;
            if(!u.empty()&&u[0]>='0'&&u[0]<='9')break;
        }
        lv=pr2(u);
        printf("Case #%d:\n",k+1);
        for(i=0;i<lv;++i)
        {
            string rq,tmp;
            cin>>rq;
            cin>>nv;
            ET.clear();
            for(j=0;j<nv;++j)
            {
                cin>>tmp;
                ET[tmp]=true;
            }
            printf("%.7lf\n",go(0));
        }
        /*for(i=0;i<13;++i)
        {
            cout<<A[i].w8<<' '<<A[i].feat<<' '<<A[i].lf<<' '<<A[i].rt<<'\n';
        }*/
    }
    return 0;
}
