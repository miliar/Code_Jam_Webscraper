#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define D 100
inline int MAX(int a,int b){return a>b?a:b;}
struct big{
	int num[D];
	int s;
	big(){
		memset(num,0,sizeof(num));
		s=1;
	}
	big(int a){
		memset(num,0,sizeof(num));
		s=0;
		while(a){
			num[s++]=a%10;
			a/=10;
		}
		if(s==0)s++;
	}
	big(const char* c){
		memset(num,0,sizeof(num));
		s=strlen(c);
		for(int i=0;i<s;i++)num[i]=c[s-1-i]-'0';
	}
	void print(){
		/*printf("s=%d: ",s);*/for(int i=s-1;i>=0;i--)printf("%d",num[i]);
	}
	big operator+(const big &b)const{
		big x;
		int i,c=0;
		x.s=MAX(s,b.s);
		for(i=0;i<x.s;i++){
			x.num[i]=(num[i]+b.num[i]+c)%10;
			c=(num[i]+b.num[i]+c)/10;
		}
		if(c){
			x.num[x.s]=c;
			x.s++;
		}
		return x;
	}
	bool operator<(const big &b)const{
		if(s!=b.s)return s<b.s;
		for(int i=s-1;i>=0;i--)if(num[i]!=b.num[i])return num[i]<b.num[i];
		return 0;
	}
	big& operator=(const big& b){
		s=b.s;
		for(int i=0;i<D;i++)num[i]=b.num[i];
		return *this;
	}
	big operator-(const big &b)const{
		big x;
		x=(*this);
		int i,c=0;
		if(x<b){
			fprintf(stderr,"minus to negative!!!!\n");
			exit(1);
		}
		for(i=0;i<s;i++){
			x.num[i]-=b.num[i];
			if(x.num[i]<0){
				x.num[i]+=10;
				x.num[i+1]--;
			}
		}
		while(x.s>1&&x.num[x.s-1]==0)x.s--;
		return x;
	}
	big operator*(const int b)const{
		big x;
		int i;
		for(i=0;i<s;i++)x.num[i]=num[i]*b;
		for(i=0;i<s||x.num[i];i++){
			x.num[i+1]+=x.num[i]/10;
			x.num[i]%=10;
		}
		x.s=i;
		return x;
	}
	big operator*(const big &b)const{
		int i,j;
		big x;
		for(i=0;i<s;i++)for(j=0;j<b.s;j++)x.num[i+j]+=num[i]*b.num[j];
		for(i=0;i<s+b.s-1||x.num[i];i++){
			x.num[i+1]+=x.num[i]/10;
			x.num[i]%=10;
		}
		x.s=i;
		return x;
	}
	big operator>>(int a)const{
		big x;
		if(s<=a)return x;
		for(int i=0;i<s-a;i++)x.num[i]=num[i+a];
		x.s=s-a;
		return x;
	}
	big operator<<(int a)const{
		big x;
		for(int i=0;i<s&&i+a<D;i++)x.num[i+a]=num[i];
		x.s=s+a;
		if(x.s>D)x.s=D;
		return x;
	}
	big operator/(const big &b)const{
		big x,y,z,w;
		if((*this)<b)return x;
		w=*this;y=b;
		int i,j;
		y=(y<<(s-b.s));
		for(i=s-b.s;i>=0;i--){
			for(j=9;j>=0;j--){
				z=y*j;
				if(!(w<z)){
					x.num[i]=j;
					w=w-z;
					break;
				}
			}
			y=(y>>1);
		}
		x.s=s-b.s+1;
		if(x.s>1&&x.num[x.s-1]==0)x.s--;
		return x;
	}
	big operator%(const big &b)const{
		big x,y,z,w;
		if((*this)<b)return (*this);
		w=*this;y=b;
		int i,j;
		y=(y<<(s-b.s));
		for(i=s-b.s;i>=0;i--){
			for(j=9;j>=0;j--){
				z=y*j;
				if(!(w<z)){
					x.num[i]=j;
					w=w-z;
					break;
				}
			}
			y=(y>>1);
		}
		return w;
	}
	bool isnz()const{
		return !(s==1&&num[0]==0);
	}
}in[1010],tt,T,ans;
big gcd(big a,big b){
	if(b.isnz())while((a=(a%b)).isnz()&&(b=(b%a)).isnz());
	return a+b;
}
char tmp[100];
int main(){
	int t,cas=1;
	scanf("%d",&t);
	while(t--){
		int n,i;
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",tmp);
			in[i]=tmp;
		}
		for(i=1;i<n;i++)if(in[i]<in[0]){
			tt=in[0];in[0]=in[i];in[i]=tt;
		}
		/*for(i=0;i<n;i++){
			printf("in[%d]=",i);in[i].print();puts("");
		}*/
		T=0;
		for(i=1;i<n;i++){
			T=gcd(T,in[i]-in[0]);
		//	printf("i=%d ",i);(in[i]-in[0]).print();printf(" ");T.print();puts("");
		}
		//T.print();puts("");
		ans=(T-in[0]%T)%T;
		printf("Case #%d: ",cas++);ans.print();puts("");
	}
}
