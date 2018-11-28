#include <iostream>
#include <queue>
#define fi first
#define se second
#include <utility>
#include <algorithm>
using namespace std;
int isi[1111][1111];
int res;
int apa;
int n;
bool aneh[1000000];
pair <int,int> lho[11111];

char s[111111];
bool valid(int a,int b,int z){
	 if (z==1 && isi[a][b]==2) return 0;
	 if (z==1) return 1;
	 for (int i=a;i<a+z-1;i++)
	 for (int j=b;j<b+z-1;j++){
	 	 if (isi[i][j]==2 || isi[i][j]==isi[i+1][j] || isi[i][j]==isi[i][j+1]) return 0;
		  }
  for (int i=a;i<a+z-1;i++){
  	  if (isi[i][b+z-1]==2 || isi[i][b+z-1]==isi[i+1][b+z-1]) return 0;
		}

  for (int j=b;j<b+z-1;j++){
  	  if (isi[a+z-1][j]==2 || isi[a+z-1][j]==isi[a+z-1][j+1]) return 0;
		}
		if (isi[a+z-1][b+z-1]==2) return 0;
		  return 1;
	 }
	 
int conv(char x){
	if (x>='0' && x<='9') return x-'0';
	return x-'A'+10;
	}
	int jwb[1000000],jwb2[1000000];
int main(){
freopen("ins.in","r",stdin);
freopen("B.out","w",stdout);
int T=0;
scanf("%d",&T);
while (T--){
	  memset(isi,0,sizeof(isi));
	  memset(lho,0,sizeof(lho));
	  res=0;	  
	  memset(aneh,0,sizeof(aneh));
	  memset(jwb,0,sizeof(jwb));
	  long long a,b,c;  
	  scanf("%lld%lld%lld",&a,&b,&c);
	 int res=0;
	// cout<<c<<endl;
	 int zz=1;
	 while (a*c<b){
	 			res++;
	 			c*=c;
				 
				 
				 
				 }
		apa++;
  printf("Case #%d: %d\n",apa,res);
  }
//	system("pause");

  }

