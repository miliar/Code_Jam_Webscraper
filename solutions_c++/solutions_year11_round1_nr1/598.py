#include<cstdio>
#include<cstring>
using namespace std;
const int N=101;
int f[N];
int x1,x2,y1,y2,t,i,j,l;
unsigned long long n,ret;
bool bj[N];
char ch;
unsigned long long read(){
	while(ch=getchar(),ch<'0' || ch>'9');
	ret=ch-'0';
	while(ch=getchar(),ch>='0' && ch<='9')ret=ret*10+ch-'0';
	return ret;
}
void init(){
	memset(bj,0,sizeof(bj));
	memset(f,0,sizeof(f));
	for(i=2;i<N;i++)
		if(!bj[i]){
			f[++f[0]]=i;
			for(j=i;j<N;j+=i)
			  bj[j]=1;
		}
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&t);
	init();
	for(l=1;l<=t;l++){
		printf("Case #%d: ",l);
		n=read();scanf("%d%d",&x1,&y1);
		if(y1==0 || y1==100){
		if(x1!=y1){
			printf("Broken\n");
			continue;
		}
		else{
			printf("Possible\n");
			continue;
		}
		}
		x2=y2=100;
		for(i=1;i<=f[0];i++){
			while(x1%f[i]==0 && x2%f[i]==0 && x1!=0){
				x1/=f[i];x2/=f[i];
			}
			while(y1%f[i]==0 && y2%f[i]==0 && y1!=0){
				y1/=f[i];y2/=f[i];
			}
		}
		if(x2<=n)
		  printf("Possible\n");
		  else printf("Broken\n");
	}
}
