#include <stdio.h>

char s[60][60];
int x,y;
bool check(char ch,int n,int k1)
{
	int i,j,k;
	for(i=0; i<n; i++)
		for(j=0; j<n; j++)
			if(s[i][j] == ch){
				k = 0;
				//if(j > 0) if(s[i][j-1] == ch) goto x;
				while(s[i][j+k]==ch && j+k<n) k++;
				if(k == k1){
					x = i, y = j;
					return 1;
				}
x:k = 0;
				//if(i > 0) if(s[i-1][j] == ch) goto y;
				while(s[i+k][j]==ch && i+k<n) k++;
				if(k == k1){
					x = i, y = j;
					return 1;
				};
y:k = 0;
				//if(i > 0 && j > 0) if(s[i-1][j-1] == ch) goto z;
				while(s[i+k][j+k]==ch && j+k<n && i+k<n) k++;
				if(k == k1){
					x = i, y = j;
					return 1;
				}
z:k = 0;
			//	if(i < n-1 && j > 0) if(s[i+1][j-1] == ch) continue;
				while(s[i-k][j+k]==ch && j+k<n && i-k>=0) k++;
				if(k == k1){
					x = i, y = j;
					return 1;
				}
			}
			return 0;

}
int main(){
	int t,n,k,i,j,m;
	int Rc,Bc;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%d%d",&n,&k);
		for(j=0;j<n;j++){
			scanf("%s",s[j]);
// 			for(m=0;m<n;m++){
// 				
// 			}
		}
		for(j=n-1;j>=0;j--){
			for(m=n-1;m>=0;m--){
				for(int x=m-1;x>=0;x--)
				if(s[j][m]=='.') {
					char tmp=s[j][x];
					s[j][x]=s[j][m];
					s[j][m]=tmp;
				}
			}
		}
	    Rc=check('R',n,k);
		Bc=check('B',n,k);
		printf("Case #%d: ",i+1);
		if(Bc&&Rc) printf("Both\n");
		else if(Bc) printf("Blue\n");
		else if(Rc) printf("Red\n");
		else printf("Neither\n");
	
	}
}