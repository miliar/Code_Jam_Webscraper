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
freopen("C.out","w",stdout);
int T=0;
scanf("%d",&T);
while (T--){
	  memset(isi,0,sizeof(isi));
	  memset(lho,0,sizeof(lho));
	  res=0;	  
	  memset(aneh,0,sizeof(aneh));
	  memset(jwb,0,sizeof(jwb));
	  int m;	  
	  scanf("%d%d",&m,&n);
	  for (int i=1;i<=m;i++) {scanf("%s",s);
	  long long tmp=0;
	  long long mult=1;
	  reverse(s,s+(n/4));
	  for (int j=1;j*4<=n;j++){
	  	  	   tmp+=conv(s[j-1])*mult;
			   mult*=16;
			   }
   			   for (int k=0;k<n;k++){
			   	   if ((1ll<<(long long)k) & tmp ) isi[i][n-k]=1;
					  }
	  
	  }
 /* for (int i=1;i<=m;i++){
  for (int j=1;j<=n;j++)
  cout<<isi[i][j];
  cout<<endl;*/
  int mx=min(m,n);
  //cout<<valid(1,13,6)<<endl;
  for (int k=mx;k>=1;k--)
  for (int i=1;i<=m-k+1;i++)
  for (int j=1;j<=n-k+1;j++){
  	  if (valid(i,j,k)){
	  	 				
	  	 				if (aneh[k]==0) res++;
	  	 				aneh[k]=1;
	  	 				jwb[k]++;
	  	 				for (int l=i;l<=i+k-1;l++)
	  	 				for (int M=j;M<=j+k-1;M++)
	  	 				isi[l][M]=2;
						   
						   }
		}
		apa++;
  printf("Case #%d: %d\n",apa,res);
  for (int i=n+m;i>=1;i--)if (aneh[i])
  printf("%d %d\n",i,jwb[i]);
  }
//	system("pause");

  }

