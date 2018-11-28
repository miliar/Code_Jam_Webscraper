#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;


int a[4];
int main(){
	int i,j,k,m,n,r,c,s,p,x,ans;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>r;
	for(c=1;c<=r;++c){
		a[0]=a[1]=a[2]=a[3]=0;
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;++i){
			scanf("%d",&x);
//			cout<<x<<endl;
			if(x==0){
				a[2]++;  //only not sup
				if(0>=p)	a[3]++;  //not sup & >=p
				continue;
			}
			if(x==1){
				a[2]++;
				if(1>=p)	a[3]++;
				continue;
			}
			
			if(x%3==0){
				if(x/3>=p)	a[0]++;
				else if(x/3+1>=p)	a[1]++;
			}
			else if(x%3==1){
				if(x/3+1>=p)	a[0]++;
			}
			else{
				if(x/3+1>=p)	a[0]++;
				else if(x/3+2>=p)	a[1]++;
			}
		}
		
		ans=a[1];
		if(s<ans)	ans=s;
		ans+=a[0]+a[3];
		
		if(n-a[2]<s)	ans=0;
		printf("Case #%d: %d\n",c,ans);
	}
}


/*
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
}*/



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