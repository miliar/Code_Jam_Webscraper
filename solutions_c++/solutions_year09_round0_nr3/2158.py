#include <iostream>
using namespace std;


char s[502];
int f[502][20];
char alpha[20] = "welcome to code jam";

inline void fix( int &x ) {
	if(x>=10000)x%=10000;
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int an=strlen(alpha);
	
	int n;
	int cas=1;
	
	scanf("%d\n",&n);
	while(n--){
		gets(s);
		
		int len=strlen(s);
		int sum=0;
		int i=0;
		while(i<len && s[i]!='w')i++;
		
		printf("Case #%d: ",cas++);
		if(i==len){
			printf("%04d\n",sum);
			continue;
		}
		
		memset(f,0,sizeof f);
		for(int i=0;i<len;i++)
			if(s[i]=='w')
				f[i][0]=1;
		
		for(;i+1<len;i++){
			for(int j=0;j<an-1;j++){
				if(s[i]==alpha[j]){
					for(int k=i+1;k<len;k++){
						if(s[k]==alpha[j+1]){
							//printf("%d,%d <- %d,%d\n",k,j+1,i,j);
							f[k][j+1]+=f[i][j];
							fix(f[k][j+1]);
						}
					}
				}
			}
		}
		for(int i=0;i<len;i++){
			sum+=f[i][an-1];
			//printf("%d %d\n",i,an-1);
			fix(sum);
		}
		printf("%04d\n",sum);
	}
	
	return 0;
}
