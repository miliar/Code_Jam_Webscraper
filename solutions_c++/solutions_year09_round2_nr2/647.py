#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;


char s[100];
int n;



int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,t,T,ca;
	char c;
	ca=0;
	scanf("%d",&T);
	while(T--){
		scanf("%s",s);
		n=strlen(s);
		for(i=n-2;i>-1;i--){
			t=0; k=0;
			for(j=i+1;j<n;j++){
				if(s[j]>s[i]){
					if(t==0||s[k]>s[j]){
						t=1;
						k=j;
					}
				}
			}
			if(t==1){
				c=s[i];
				s[i]=s[k];
				s[k]=c;
				sort(s+i+1,s+n);
				break;
			}
		}
		if(i<=-1){
			t=0; 
			for(j=0;j<n;j++){
				if(s[j]>'0'){
					if(t==0||s[k]>s[j]){
						t=1;
						k=j;
					}
				}
			}
			for(j=n-1;j>-1;j--) s[j+1]=s[j];
			s[n+1]=0;
			k++;
			s[0]=s[k];
			s[k]='0';
			sort(s+1,s+n+1);
			
		}

		printf("Case #%d: %s\n",++ca,s);
	}
	return 0;
}