#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;


int main(){
	int i,j,k,m,n,r,c,A,B,x,y,t,p,ans;
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>r;
	for(c=1;c<=r;++c){
		scanf("%d%d",&A,&B);
		ans=0;
		for(x=A;x<B;++x){
			t=x;
			p=1;
			t/=10;
			while(t){
				t/=10;
				p*=10;
			}
			y=x;
			while(true){
				y=(y%10)*p+y/10;
				if(y==x)	break;
				if(y>x&&y<=B){
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",c,ans);
	}
}



/*

char a[30]="yhesocvxduiglbkrztnwjpfmaq";
int main(){
	int i,j,k,m,n,r,c;
	char ch;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&r);
	getchar();
	for(c=1;c<=r;++c){
		printf("Case #%d: ",c);
		while(scanf("%c",&ch)==1){
			if(ch==' ')	printf(" ");
			else if(ch=='\n'){
				printf("\n");
				break;
			}
			else	printf("%c",a[ch-'a']);
		}
	}
	
}*/