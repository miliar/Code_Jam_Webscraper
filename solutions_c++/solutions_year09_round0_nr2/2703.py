#include<iostream>
using namespace std;

int tab[20000], uni[20000];
int find(int a){
	return uni[a]==a?a:(uni[a]=find(uni[a]));
}
void lacz(int a,int b){
	uni[find(a)]=find(b);
}
int H, W;

inline void check(int x, int y){
	int n=y*W+x;
	int low=1<<24;
	if(x>0){
		low=min(tab[n-1],low);
	}
	if(x<W-1){
		low=min(tab[n+1],low);
	}
	if(y>0){
		low=min(tab[n-W],low);
	}
	if(y<H-1){
		low=min(tab[n+W],low);
	}
	if(tab[n]<=low) return;
	if(y>0 && tab[n-W]==low){
		lacz(n-W,n);
	}
	else if(x>0&& tab[n-1]==low){
		lacz(n-1,n);
	}
	else if(x<W-1&& tab[n+1]==low){
		lacz(n+1,n);
	}
	
	else if(y<H-1&& tab[n+W]==low){
		lacz(n+W,n);
	}
}

int lit[400];
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int Test;
	scanf("%d",&Test);
	for(int TEST=1; TEST<=Test; TEST++){
		printf("Case #%d:\n",TEST);
		scanf("%d%d",&H,&W);
		for(int i=0; i<H*W; i++){scanf("%d",&tab[i]); uni[i]=i;}
		for(int i=0; i<H; i++)
			for(int j=0; j<W; j++) check(j, i);
		for(int i=0; i<H*W; i++) uni[i]=find(i);
		memset(&lit, 0, sizeof(lit));
		char c='a';
		for(int i=0; i<H; i++){
			for(int j=0; j<W; j++){
				int n=W*i+j;
				if(lit[find(n)]==0){
					lit[find(n)]=c++;
				}
				printf("%c ",lit[find(n)]);
			}
			printf("\n");
		}
	}
//while(1);

}