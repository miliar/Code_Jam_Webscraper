#include<iostream>
#include<string>
#include<vector>
#include<sstream>

using namespace std;

typedef struct node
{
       double val;
       string s;
     
       node *child1;
       node *child2;
} node;
string trim(string X)
{
       while(X.size()>0 && X[0]==' ')
         X=X.substr(1);
       while(X.size()>0 && X[X.size()-1]==' ')
          X.erase(X.end()-1);
       return X;
}
node * maketree(string X)
{
     node *R=new node;
     R->s="";
     R->child1=NULL;
     R->child2=NULL;
     
     
     X=trim(X);
     if(X.size()<=2) return R;
     if(X[0]=='(')
     {
                  int ind=1;
                  while(X[ind]==' ') ind++;
                  string s="";
                  while(ind<X.size() && X[ind]!=' ' && X[ind]!=')')
                  {
                    s.push_back(X[ind]);
                    ind++;
                  }
                  s=trim(s);
                  while(s[0]<'0' || s[0]>'9')
                     s=s.substr(1);
                  while(s[s.size()-1]<'0' || s[s.size()-1]>'9')
                     s.erase(s.end()-1);
                  stringstream ss;
                  ss<<s;
                  double sd;
                  ss>>sd;
                  R->val=sd;
                  while(ind<X.size() && X[ind]==' ') ind++;
                  if(ind==X.size() || X[ind]==')') return R;
                  
                  string s1;
                  while(X[ind]!=' ')
                  {
                                  
                                  s1.push_back(X[ind]);
                                  ind++;
                  }
                  R->s=s1;
                  R->child1=maketree(X.substr(ind+1));
                  while(X[ind]!='(')
                    ind++;
                  int count=1;
                  ind++;
                  while(count!=0)
                  {
                                 ind++;
                                 if(X[ind]==')')
                                   count--;
                                 if(X[ind]=='(')
                                   count++;
                  }
                  ind++;
                  R->child2=maketree(X.substr(ind));
     }
     return R;
}
                                   
bool has(vector<string> X,string to)
{
     for(int i=0;i<X.size();i++)
       if(X[i]==to) return true;
      return false;
}                  
     
int main()
{
    int T;
    freopen("21.in","r",stdin);
    freopen("21.out","w",stdout);
    cin>>T;
    int K=T;
    getchar();
    while(T--)
    {
              int L;
              cin>>L;
              getchar();
              string s="";
              for(int i=0;i<L;i++)
              {
                           string t;
                           getline(cin,t);
                           t=trim(t);
                           s=s+" "+t;
              }
              node *P=maketree(s);
              int N;
              cin>>N;
              getchar();
              cout<<"Case #"<<K-T<<":\n";
              for(int i=0;i<N;i++)
              {
                      string s1;
                      cin>>s1;
                      int Y;
                      cin>>Y;
                      getchar();
                      vector<string> F(Y);
                      for(int ii=0;ii<Y;ii++) cin>>F[ii];
                      node *T=P;
                      double ans=1;
                      while(T)
                      {
                              ans=ans*(T->val);
                              if(has(F,T->s))
                                   T=T->child1;
                              else T=T->child2;
                      }
                      printf("%.7f\n",ans);;
              }
    }
}
                      
                      
                      
              
              
    
    
       
