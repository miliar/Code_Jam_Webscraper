#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <iomanip>
using namespace std;

#define mem(a,b) (memset(a,b,sizeof(a)));
#define two(x) ((1)<<(x))
#define REP(x) for(int i=0;i<x;i++)
#define IREP(i,x) for(int i=0;i<x;i++)
#define SIZE(x) ((int)(x).size())
#define MP(x,y) make_pair(x,y)
#define rint(x) scanf("%d",&x)
#define rdbl(x) scanf("%lf",&x)
#define OUT(x) (cout << #x << " = " << x << endl)
typedef pair<int,int> PI;
typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VII;
template<class T>T sqr(T a){return a*a;}
template<class T>T gcd(T a,T b){return b==0?a:gcd(b,a%b);}
template<class T>inline bool checkmax(T&a,const T&b){return a<b?a=b,1:0;}
template<class T>inline bool checkmin(T&a,const T&b){return a>b?a=b,1:0;}
template<class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
template<class T>T dis(T x1,T y1,T x2,T y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
int lowbit(int x){return x&(-x);}
template<class T>void printbit(T a){cout<<bitset<17>(a)<<endl;}
const int NMAX=30;
struct Trie{
	bool judge;
	struct Trie *next[NMAX];
};

Trie *root;

void append(char* str,int len){
	int i, j;
	Trie *p;
       p = root;
       for (i = 0; i <= len; i++){
              if (i == len){
                     p->judge = 1;
              }
              else{
                     int index=str[i]-'a';
                     if (p->next[index] == 0){
                            p->next[index] = new Trie;
                            p = p->next[index];
                            p->judge = 0;
                            for (j = 0;j<NMAX; j++){
                                   p->next[j] = NULL;
                            }
                     }
                     else{
                            p = p->next[index];
                     }
              }
	}
}
//
//int destroy(Trie *p){
//	int i;
//	for (i=0; i<NMAX; i++)
//	{
//		if (p->next[i] != NULL)
//		{
//			destroy(p->next[i]);
//		}
//	}
//	delete p;
//	return 1;
//}
//
//char path[100];
//void print(Trie* h,int dep){
//      if(dep==3){
//              for(int i=0;i<dep;i++){
//                     printf("%c",path[i]);
//              }
//              puts("");//debug
//              return;
//       }
//       for(int i=0;i<NMAX;i++){
//              if(h->next[i]){
//                     path[dep]='a'+i;
//                     print(h->next[i],dep+1);
//              }
//       }
//}

const int AMAX=20;
//vector<char>A[AMAX];
int A[AMAX][100];
int Alen[AMAX];
int acnt;
int ans;
int len;

void dfs(int dep,Trie* h){
       if(dep==len){
//              for(int i=0;i<dep;i++)cout<<path[i];cout<<endl;
              ans++;
              return;
       }
       for(int i=0;i<Alen[dep];i++){
              int index=A[dep][i]-'a';
//              path[dep]=A[dep][i];
              if(h->next[index]){
                     dfs(dep+1,h->next[index]);
              }
       }
}

int go;

char str[1001];
void initTree(){
       root=new Trie;
	root->judge = 0;
	for (int i=0;i<NMAX; i++){
		root->next[i] = NULL;
	}
}

void init(){
       initTree();
       int scnt;
       scanf("%d%d%d\n",&len,&scnt,&go);
       REP(scnt){
              gets(str);
//              if(strlen(str)!=len)cout<<"error";
              append(str,len);
       }
}

void readStr(){
       gets(str);
       acnt=0;
       char *s=str;
       while(*s){
              if(*s=='('){
                     s++;
                     while(*s && *s!=')'){
                            A[acnt][Alen[acnt]++]=(*s);
                            s++;
                     }
              }else{
                     A[acnt][Alen[acnt]++]=(*s);
              }
              acnt++;
              s++;
       }
}
//
//void output(){
//       for(int i=0;i<AMAX;i++){
//              for(int j=0;j<SIZE(A[i]);j++){
//                     cout<<A[i][j]<<" ";
//              }
//              cout<<endl;
//       }
//}

int main(){
//       freopen("in.txt","r",stdin);
//       freopen("out.txt","w",stdout);
       init();
//       print(root,0);
       for(int i=1;i<=go;i++){
//              for(int j=0;j<AMAX;j++){A[j].clear();}
              for(int j=0;j<AMAX;j++)Alen[j]=0;
              ans=0;
              readStr();
              dfs(0,root);
              printf("Case #%d: %d",i,ans);puts("");//debug
       }
	return 0;
}
