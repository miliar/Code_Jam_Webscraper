#include<cstdio>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
using namespace std;
const int mn=505,mm=20,p=10000;

char s1[]="welcome to code jam",s2[mn];

int n1,n2,f[mm][mn];

int main(){
	freopen("C-Large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int Tn;
	scanf("%d",&Tn);
	gets(s2);
	for(int Cn=1;Cn<=Tn;Cn++){
		gets(s2);
		n1=strlen(s1);
		n2=strlen(s2);
		memset(f,0,sizeof(f));
		for(int i=0;i<n1;i++){
			for(int j=0;j<n2;j++){
				if(s1[i]==s2[j]){
					if(i==0)f[i][j]=1;
					else{
						for(int k=0;k<j;k++)
							f[i][j]+=f[i-1][k]%p;
						f[i][j]%=p;
					}
				}
			}
		}
		int s=0;
		for(int i=n1-1;i<n2;i++)s+=f[n1-1][i],s%=p;
		printf("Case #%d: ",Cn);
		printf("%.4d\n",s);
	}
	return 0;
}
