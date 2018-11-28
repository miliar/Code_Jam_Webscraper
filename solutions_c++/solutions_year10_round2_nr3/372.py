#include<cstdio>
#include<cstring>
#include<string>

#include<map>
#include<algorithm>

#define mm 100003

using namespace std;

int ncr[556][556];
int f[556][556];

int main(){
	memset(ncr,0,sizeof(ncr));
	for(int i=0;i<555;i++)ncr[i][0]=1;
	for(int i=1;i<555;i++)for(int j=1;j<555;j++)
		ncr[i][j] = (ncr[i-1][j-1]+ncr[i-1][j])%mm;
	memset(f,0,sizeof(f));
	f[0][1] = 1;
	for(int i=1; i<555; i++)for(int j=i+1; j<555; j++){
		f[i][j]=0;
		for(int k=0;k<i;k++){
			f[i][j]=(f[i][j]+f[k][i]*ncr[j-i-1][i-k-1])%mm;
		}
	}
	int tt,l;
	scanf("%d", &tt);
	for(int ii=0;ii<tt;ii++){
		scanf("%d", &l);
		int ans = 0;
		for(int i=0;i<l;i++)ans = (ans+f[i][l])%mm;
		printf("Case #%d: %d\n", ii+1, ans);
	}
	
	return 0;
}

