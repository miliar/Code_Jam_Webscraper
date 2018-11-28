#include<stdio.h>
#include<algorithm>
#include<memory.h>

int n,T,bad;
struct Tlong {
	int x[222];
	Tlong(){
		memset(x,0,sizeof(x));
		x[0]=1;
	}
	void read(){
		char s[55];
		scanf("%s",s);
		memset(x,0,sizeof(x));
		x[0]=strlen(s);
		for(int i=1;i<=x[0];i++) x[i]=s[x[0]-i]-48;
	}
	void print(){
		for(int i=x[0];i>0;i--) putchar(x[i]+48);
	}
	bool operator<(const Tlong & B)const{
		if(x[0]!=B.x[0]) return x[0]<B.x[0];
		for(int i=x[0];i>0;i--) if(x[i]!=B.x[i]) return x[i]<B.x[i];
		return 0;
	}
	bool operator<=(const Tlong & B)const{
		if(x[0]!=B.x[0]) return x[0]<B.x[0];
		for(int i=x[0];i>0;i--) if(x[i]!=B.x[i]) return x[i]<B.x[i];
		return 1;
	}
	Tlong operator-(const Tlong & B)const{
		Tlong C;
		C.x[0]=x[0];
		for(int i=1;i<=x[0];i++){
			C.x[i]+=x[i]-B.x[i];
			if(C.x[i]<0){
				C.x[i]+=10;
				C.x[i+1]--;
			}
		}
		while(C.x[0]>1 && C.x[C.x[0]]==0) C.x[0]--;
		return C;
	}
	Tlong operator+(const Tlong & B)const{
		Tlong C;
		C.x[0]=x[0];
		if(B.x[0]>C.x[0]) C.x[0]=B.x[0];
		for(int i=1;i<=C.x[0];i++){
			C.x[i]+=x[i]+B.x[i];
			if(C.x[i]>9){
				C.x[i]-=10;
				C.x[i+1]++;
			}
		}
		if(C.x[C.x[0]+1]) C.x[0]++;
		return C;
	}
	Tlong operator+(const int X)const{
		Tlong C;
		C.x[0]=x[0];
		C.x[1]=X;
		for(int i=1;i<=x[0];i++){
			C.x[i]+=x[i];
			if(C.x[i]<0){
				C.x[i]+=10;
				C.x[i+1]--;
			}
		}
		while(C.x[0]>1 && C.x[C.x[0]]==0) C.x[0]--;
		return C;
	}
	void div2(){
		int c=0;
		for(int i=x[0];i>0;i--){
			c=c*10+x[i];
			x[i]=c>>1;
			c&=1;
		}
		while(x[0]>1 && x[x[0]]==0) x[0]--;
	}
	Tlong operator*(const Tlong & B){
		Tlong C;
		for(int i=1;i<=x[0];i++)
			for(int j=1;j<=B.x[0];j++)
				C.x[i+j-1]+=x[i]*B.x[j];
		C.x[0]=x[0]+B.x[0]-1;
		for(int i=1;i<=C.x[0];i++){
			C.x[i+1]+=C.x[i]/10;
			C.x[i]%=10;
		}
		if(C.x[C.x[0]+1]) C.x[0]++;
		return C;
	}
	Tlong operator/(const Tlong & B)const{
		Tlong left,right=*this,center;
		while(left<right){
			center=left+right+1;
			center.div2();
			if(center*B<=(*this)) left=center;else right=center+(-1);
		}
		return left;
	}
	Tlong operator%(const Tlong & B)const{
		Tlong C=(*this)/B;
		return (*this)-(C*B);
	}
	bool operator!()const{
		return x[0]>1 || x[1]!=0;
	}
} a[2222],tt,t;


Tlong gcd(Tlong a,Tlong b){
	Tlong c;
	while(!b){
		c=a%b;
		a=b;
		b=c;
	}
	return a;
}

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%d",&n);
		for(int i=0;i<n;i++) a[i].read();
		std::sort(a,a+n);
		tt=a[1]-a[0];
		for(int i=2;i<n;i++) tt=gcd(tt,a[i]-a[i-1]);
		bad=0;
		for(int i=0;i<n;i++){
			Tlong h=a[i]%tt;
			if(h.x[0]>1 || h.x[1]!=0){
				bad=1;
				break;
			}
		}
		Tlong y;
		if(bad){
			y=tt-(a[0]%tt);
			for(int i=1;i<n;i++){
				t=tt-(a[i]%tt);
				y=(y/gcd(y,t))*t;
			}
		}                    
		printf("Case #%d: ",_);
		y.print();
		puts("");
	}
	return 0;
}
