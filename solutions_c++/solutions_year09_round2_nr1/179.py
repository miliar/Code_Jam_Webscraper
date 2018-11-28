#include<iostream>
#include<sstream>
#include<set>
#include<vector>
#include<string>
#include<map>

#define PB push_back
#define MP make_pair


using namespace std;

string i2s(long long x) { ostringstream o; o<<x; return o.str(); }
long long s2i(string s) { istringstream i(s); long long x; i>>x; return x; } 


struct Tree
{
    double w;
    string f;
    Tree *L, *R;      

    Tree() { f=""; }
    
};

string temp,s;

set<string> S;

double p;


void initialize()
{
    s = "";
    
    int i,j,k, num;
    getline(cin,temp);
    num = s2i(temp);    
    
    for (i=0; i<num; i++)
    {
        getline(cin,temp);
        s += temp;
    }
}

string norm(string s)
{
    while (s!="" && s[0]==' ') s.erase(0,1);
    while (s!="" && s[s.size()-1]==' '  ) s.erase(s.size()-1,1);
    if (s!="" && s[0]=='(') s.erase(0,1);
    if (s!="" && s[s.size()-1]==')' ) s.erase(s.size()-1,1);
    while (s!="" && s[0]==' ') s.erase(0,1);
    while (s!="" && s[s.size()-1]==' '  ) s.erase(s.size()-1,1);
    return s;
}


void go(string s, Tree *r)
{
    int i,j,k;
    s = norm(s);
    
    
//    cout<<s<<endl;

    // weight
    string temp="";
    for (i=0; i<s.size() && s[i]!=' '; i++)
      temp += s[i];
    
    istringstream ii(temp);
    ii>>r->w;
    
    
    // feature
    temp="";
    for (; i<s.size() && s[i]!='('; i++)
      temp += s[i];
    
    if (temp!="") // ok
    {
         r->f = norm(temp);
         temp = "";
         
         r->L = new Tree();
         r->R = new Tree();
         
         int cnt=0;
         for (;i<s.size(); i++)
         {
             temp += s[i];
             if (s[i]=='(') cnt++;
             if (s[i]==')') cnt--;
             
             if (cnt==0) //ok
             {
                 go(temp, r->L);
                 temp = s.substr(i+1);
                 go(temp, r->R);

                 return;
             }
         }
         
    }
    
    
}



void calc(Tree *r)
{
     p*=r->w;
     
     if (r->f=="") return;
     
     //cout<<r->f<<endl;
     
     if (S.count(r->f))
       calc(r->L);
     else
       calc(r->R);     
}


void solve()
{
    int i,j,num, cnt;
    Tree *r = new Tree(); 
    go(s,r);
    
    getline(cin,temp);
    num = s2i(temp);
    
    for (i=0; i<num; i++)
    {
        S.clear();
        getline(cin,temp);
        istringstream ii(temp);
        
        ii>>temp; // name
        ii>>cnt; 
        for (j=0; j<cnt; j++)
        {
            ii>>temp;
            S.insert(temp);
            //cout<<temp<<endl;
        }
        
        
        p=1;
        calc(r);
        
        printf("%.7lf\n",p);
    }
    
    
        
}


#include<conio.h>
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("t.out","w",stdout);
    
    int num,z;
    getline(cin,temp);
    num = s2i(temp);
    
    for (z=1; z<=num; z++)
    {
       cout<<"Case #"<<z<<":"<<endl;
       initialize();
       solve();
    }
    
    
    fclose(stdin);
//    fclose(stdout);    
    getch();
    
    return 0;
}
