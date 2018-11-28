#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <numeric>
#include <utility>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

const int oo = 0x7fffffff;
const double PI = atan2(0.0, -1.0);
const double eps=(1.0e-9);

int gcd(int a, int b)
{
   if(b==0) return a;
   else return gcd(b,a%b);
}

int cal(char* s,int* order,int n)
{
    int i,j,len=strlen(s);
    char news[1024];
    
   // for(i=0;i<n;++i)
     //   printf("%d ",order[i]);printf("\n");
    
    for(i=0;i<len;i+=n)
        for(j=0;j<n;++j)
            news[i+j]=s[i+order[j]];
    news[len]='\0';
    
   // printf("%s  %s\n",s,news);
    
    int cnt=1;
    for(i=1;i<len;++i)
        if(news[i]!=news[i-1])
            ++cnt;
    return cnt;
}

int main()
{
    freopen("D-small.in","r",stdin);
    freopen("D-small.out","w",stdout);
    
    int n,cas,re,i,ans,order[8];
    char s[1024];
    
    for(scanf("%d",&re),cas=1;re--;++cas){
        scanf("%d%s",&n,s);
        for(i=0;i<n;++i)
            order[i]=i;
        ans=oo;
        do{
            ans=min(ans,cal(s,order,n));
        }while(next_permutation(order,order+n));
        printf("Case #%d: %d\n",cas,ans);
    }
    
}















