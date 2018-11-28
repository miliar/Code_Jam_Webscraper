#include <cstdio>
#include <set>
#include <sstream>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <map>
#include <vector>
#include <queue>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef vector<ii> vii;
typedef vector<vii> vvii;

#define FOR(i, x) for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (__typeof__((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int)(x).size())
#define EPS 1E-10
#define INF 0x3F3F3F3f
#define DV(x) cout<<__LINE__<<"  "#x" is "<<x<<endl
#define DM(mat,rows,cols) FOR(i,rows){FOR(j,cols)cout<<mat[i][j]<<" ";cout<<endl;}

int cmp(double x, double y = 0, double tol = EPS) {
   return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

bool cmp_eq(double x, double y) { return cmp(x, y) == 0; }
bool cmp_lt(double x, double y) { return cmp(x, y) < 0; }


#define MAX 1000
double weight[MAX+1];
string feature[MAX+1];
bool leaf[MAX+1];
string inp;
int pos;

double getDouble()
{
   int loc = pos;
   //while((inp[loc]!=')') (inp[loc]==' ')) loc++;
   while(isdigit(inp[loc]) || (inp[loc]=='.') || (inp[loc]==' ')) loc++;
   //cout << "gD: " << loc << endl;
   double d;
   istringstream iss(inp.substr(pos,loc-pos));
   //cout <<inp.substr(pos,loc-pos)<<endl;
   iss >> d;
   //cout << d << endl;
   pos = loc;
   return d;
}

string getString()
{
   int loc = pos;
   //while((inp[loc]!=')') || (inp[loc]==' ')) loc++;
   while(isalpha(inp[loc])) loc++;
   string s;
   s = inp.substr(pos,loc-pos);
   pos = loc;
   while(inp[pos]==' ') pos++;
   return s;
}

void tree(int node)
{
   if(inp[pos]=='(') pos++;
   while(inp[pos]==' ') pos++;
   
   weight[node] = getDouble();

   if(inp[pos]==')') 
   {
      //cout << "leaf: " << weight[node] << endl;
      leaf[node] = true;      
      pos++;
      return;
   }
   
   feature[node] = getString();
   
   while(inp[pos]!='(' && inp[pos]!=')') pos++;
   if(inp[pos]=='(') tree(2*node);
   else if(inp[pos]==')')
   {
      //cout << "leaf: " << weight[node] << endl;
      leaf[node] = true;
      pos++;
      return;
   }
   
   while((inp[pos]==' ') || ((inp[pos]!=')') && (inp[pos]!='('))) pos++;
   if(inp[pos]=='(') tree(2*node+1);
   else if(inp[pos]==')')
   {
      //cout << "leaf: " << weight[node] << endl;
      leaf[node] = true;
      pos++;
      return;
   }
   while((inp[pos]==' ') || ((inp[pos]!=')') && (inp[pos]!='('))) pos++;
   pos++;
}

int main()
{
   freopen("in/A-small.in","r",stdin);
   freopen("out/A-small.out","w",stdout);   
   
   int N, L, A;
   string str, sstr;
   
   getline(cin,str);
   sscanf(str.c_str(),"%d",&N);
   
   FOR(n,N)
   {
      FOR(i,MAX) { feature[i] = "-1"; leaf[i] = false; }
      
      getline(cin,str);
      sscanf(str.c_str(),"%d",&L);
      
      inp = "";
      FOR(i,L)
      {
         getline(cin,str);
         inp += str;
      }
      //cout << inp << endl;

      getline(cin,str);
      sscanf(str.c_str(),"%d",&A);
      
      pos = 0;
      tree(1);

      cout << "Case #" << (n+1) << ":" << endl;
      
      FOR(i,A)
      {
         set<string> feats;
         int J;
         getline(cin,str);
         istringstream iss(str);
         iss >> sstr;
         //cout << sstr << endl;
         iss >> J;
         FOR(j,J)
         {
            iss >> sstr;
            feats.insert(sstr);
            //cout << sstr << " ";
         }
         //cout << endl;
         int node = 1;
         double mine = weight[node] * 1.0;
         while(!leaf[node])
         {
            //cout << feature[node] << endl;
            set<string>::iterator yes = feats.find(feature[node]);
            if(yes != feats.end())
            {
               node = 2*node;
            }
            else node = 2*node+1;
            mine = mine * weight[node] * 1.0;
         }
         mine *= 10000000.0;
         mine = ((int)mine)/10000000.0;
         //cout << mine << " ";
         printf("%.7lf\n",mine);
      }  
   }
   
   return 0;
}
