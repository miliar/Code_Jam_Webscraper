#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <sstream>
#include <map>

#define all(v) (v).begin(), (v).end()

using namespace std;

struct nodo
{
    double w;
    string feature;
    nodo()
    {
    }
    nodo(double a, string b)
    {
        w = a;
        feature = b;
    }
};

string s;
map <long long, nodo> G;

set <string> S;

double parse(string num)
{
    stringstream is(num);
    double x;
    is>>x;
    return x;
}


int doit(long long ind, int p)
{

    
    int q = p;
    
    //s[q]='('
    while(s[q]!='(') q++;
    q++;
    while(s[q]==' ') q++;
    
    string num = "";
    while(s[q]!=' ' && s[q]!=')')
    {
        num += s[q];
        q++;
    }
    
    double w = parse(num);
    
    while(s[q]==' ') q++;
    
    if(s[q]!=')')
    {
        string feature = "";
        while(s[q]==' ') q++;
        
        while(s[q] != ' ')
        {
            feature += s[q];
            q++;
        }
        
        
        G[ind] = nodo(w, feature);
        
        int k1 = doit(ind*2 + 1, q);
        int k2 = doit(ind*2 + 2, q+k1);
        q += k1;
        q += k2;
        while(s[q]!=')') q++;
        
        return q-p+1;
    }
    else
    {
        G[ind] = nodo(w, "END");
        return q-p+1;
    }
    
}

double f()
{
    long long p = 0;
    double x = 1;
    while(1)
    {
        x *= G[p].w;
        if(G[p].feature == "END") return x;
        else if(S.find(G[p].feature)!=S.end()) p = p*2 + 1;
        else p = p*2 + 2;
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int N;
    cin>>N;
    
    for(int nCaso = 1; nCaso <= N; nCaso++)
    {
        int L;
        cin>>L;
        
        string tmp;
        getline(cin, tmp);
        
        s = "";
        for(int i=0; i<L; i++){
            getline(cin, tmp);
            s += " " + tmp;
        }
        doit(0, 0);
        
        int A;
        cin>>A;
        
        cout<<"Case #"<<nCaso<<":"<<endl;
        
        for(int i=0; i<A; i++)
        {
            string animal;
            cin>>animal;
            
            int F;
            cin>>F;
            
            S.clear();
            
            for(int j=0; j<F; j++)
            {
                string tmp;
                cin>>tmp;
                
                S.insert(tmp);
            }
            printf("%.7lf\n", f());
        }
    }
    return 0;
}
