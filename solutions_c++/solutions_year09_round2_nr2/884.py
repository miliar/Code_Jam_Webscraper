#include <string>    
#include <vector>   
#include <algorithm>
# define loop(i, a, b) for(int i=a ; i<b ; ++i) 
using namespace std;    

int res=0;
int l,d,n;
char q[100][100];
int e[1000];
char a[5000][100];
int pd[5000];
int last;

int main(){
  freopen("B.in", "rt", stdin);
  freopen("B.out", "wt", stdout);
  int n;
  scanf("%d/n",&n);

  loop(i,0,n){
    char a[30];
    scanf("%s",&a);
    int q=0,t=0,l=0;
    while(a[l++]);--l;
    loop(j,0,l-1) {
      if (a[j]>=a[j+1]) { ++q; } 
    }
    if (q==(l-1)) {
      sort(&a[0],&a[l]); 
      loop(j,0,l) { a[l-j]=a[l-j-1]; }
      a[0]='0';
      int k=0;
      while (a[k]=='0') ++  k;
      a[0]=a[k];
      a[k]='0';
      ++l;
    }
    else
    {
      int k=l-1;
      while ( a[k] <= a[k-1] ) {--k;}
      int t=a[k-1], f=k;
      loop(j,k,l) {if ( a[j]>t && a[j]<a[f]) { f=j; } }
      a[k-1]=a[f];
      a[f]=t;
      sort(&a[k],&a[l]);  
    }

    printf("Case #%d: ",i+1);
    loop(j,0,l) printf("%d",a[j]-'0');
    printf("\n");
  }
  
  return 0;
}