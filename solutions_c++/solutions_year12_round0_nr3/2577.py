#include<iostream>
#include<complex>
#include<vector>
#include<string>
#include<map>

#include<cstdio>
#include<cctype>
#include<cstring>
#include<cstdlib>
#include<cmath>

using namespace std;
#define SZ(X) ((int)X.size())
#define CLR(X) memset(X,0,sizeof(X))
#define REP(I,N) for(int I=0;I<(N);I++)
#define PB push_back
typedef vector<int> VI;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define MIN(A,B) (((A)<(B))?(A):(B))
template<class T> inline string stringify(T x,int p=9){ostringstream o;o.precision(p);o<<x;o.flush();return o.str();}

inline VI parsei(string s,char ch=' '){string a="";VI wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(atoi(a.c_str()));a="";} if(!a.empty()) wyn.PB(atoi(a.c_str()));return wyn;}

class liczba{
  char c[20];
  int p;
  int of;
  public:
  liczba(int n){
    CLR(c);
    itoa(n,c,10);
    p=strlen(c);
    of=0;
    strncpy(c+p,c,p);
  }
  int d(){return p;}
  void rot(){of++;}
  int val(){char pom=c[of+p]; c[of+p]='\0'; int ret=atoi(c+of); c[of+p]=pom; return ret;}
};

int main(){
  int T;
  cin>>T;
  int t=1;
  string kurwa;
  getline(cin,kurwa);
  int *d=(int*)calloc(2000005, sizeof(int));
  while(t<=T){
    string g;
    getline(cin,g);
    //int d[2000005];
    //CLR(d);
    memset(d,0,2000005*sizeof(int));
    VI inp=parsei(g);
    int A=inp[0], B=inp[1];
    int out=0;
 //   printf("%d %d:\n",A,B);
    FOR(i, A, B) if(!d[i]){
      int k=1;
      liczba q(i);
      d[i]=1;
      REP(j,q.d()){
        int v=q.val();
//        printf("\t%d",v);
        if(v>i&&v<=B&&!d[v]){
                  //printf("\tok");
          d[v]=1;
          k++;
        }
                //printf("\n");
        q.rot();
      }
      out+=k*(k-1)/2;
    }
    cout<<"Case #"<<stringify(t)<<": "<<stringify(out)<<endl;
    t++;
  }
  return 0;
}
