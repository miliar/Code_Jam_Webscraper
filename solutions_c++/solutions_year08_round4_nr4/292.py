#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#define task "file"

using namespace std;
int test;
int k;
char s[2000];
char now[2000];
int p[10];

int main(void){
	freopen(task".in","r",stdin);
	freopen(task".out","w",stdout);
	scanf("%i\n",&test);
	for (int z=1;z<=test;z++){
		printf("Case #%i: ",z);
		scanf("%i\n",&k);
		scanf("%s\n",s);
		int len=strlen(s);
		for (int i=0;i<k;i++) p[i]=i+1;
		//printf("%i\n",len);
		int ans=len;
		do{
			int cur=0;
			//for (int i=0;i<k;i++) printf("%i ",p[i]);
			//printf("\n");
			for (int i=0;i<len/k;i++){
				for (int j=0;j<k;j++){
					now[cur+j]=s[cur+p[j]-1];
				}
				cur+=k;
			}
			//for (int i=0;i<len;i++) printf("%c",now[i]);
			int top=1;
			for (int	i=1;i<len;i++)
				if (now[i]!=now[i-1]) top++;
			//printf("\n%i\n",top);
			if (top<ans) ans=top;
		}while (next_permutation(p,p+k));
		cout<<ans<<endl;
	}

	return 0;
}
