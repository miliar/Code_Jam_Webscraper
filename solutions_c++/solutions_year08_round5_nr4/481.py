#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;


const int radix=10000;
#define DIGIT 4
const int MAXNUM=100;

//做zju2017的时候,由于用1年前写的模板,再加上自己做题新写了一些操作, 两份东西结合得不好,搞了好久
//一定要再写一个模板,注明细节
class Num{
public:
	int n[MAXNUM];
	int l;//0的长度应设为l=1,重写高精模板
	bool sign;
	Num(){
		l=0;
		sign=0;
		memset(n,0,sizeof(n));
	}
	Num(int a){
		sign=0;
		l=0;
		if(a<0){
			sign=1;
			a=-a;
		}
		memset(n,0,sizeof(n));
		
		while(a){
			n[l++]=a%radix;
			a/=radix;
		}
	}
	Num(char *c){
		sign=0;
		l=0;
		if(c[0]=='-'){
			sign=1;
			c++;
		}

		memset(n,0,sizeof(n));

		char* end=c;
		while(*end!=0)end++;
		end--;
		int now;
		while(end>=c){
			now=0;
			for(int i=DIGIT-1;i>=0;i--){
				if(end-i<c)continue;
				now*=10;
				now+=(*(end-i))-'0';
				//end--;
			}
			end-=DIGIT;
			n[l++]=now;
		}
		while(n[l-1]==0 && l>0)l--;
	}
	void INF(){
		sign=0;
		l=MAXNUM;
		for(int i=0;i<MAXNUM;i++)
			n[i]=radix-1;
	}
	void Set(int a){
		sign=0;
		l=0;
		if(a<0){
			sign=1;
			a=-a;
		}
		memset(n,0,sizeof(n));
		while(a){
			n[l++]=a%radix;
			a/=radix;
		}
	}
	void print(){
		if(l==0){
			printf("0\n");
			return;
		}
		if(sign==1)printf("-");
		printf("%d",n[l-1]);
		for(int i=l-2;i>=0;i--){
			int rate=radix/10;
			while(n[i]<rate){
				printf("0");
				rate/=10;
			}
			if(n[i]!=0)printf("%d",n[i]);
		}
		printf("\n");
	}
};


Num operator+(Num&,Num&);
Num operator-(Num&,Num&);
Num operator*(const Num&,const Num&);
Num operator/(Num,int);
int operator%(const Num&,int);
Num& operator+=(Num&,const Num&);
Num& operator*=(Num&,const Num&);
Num& operator/=(Num&,const int);
Num& operator++(Num&,int);
Num& operator--(Num&,int);



bool operator<(Num& a,Num& b){
	if(a.sign!=b.sign){
		if(a.sign==0)return 0;
		return 1;
	}
	if(a.sign){
		a.sign=0;
		b.sign=0;
		bool ans=(b<a);
		a.sign=1;
		b.sign=1;
		return ans;
	}
	if(a.l!=b.l)return a.l<b.l;
	for(int i=a.l-1;i>=0;i--){
		if(a.n[i]!=b.n[i])return a.n[i]<b.n[i];
	}
	return 0;
}
Num& operator/=(Num& a,const int b){
	a=a/b;
	return a;
}
Num operator-(Num& a,Num& b){
	Num c;
	if(a.sign){
		if(b.sign){
			a.sign=0;
			b.sign=0;
			c=b-a;
			a.sign=1;
			b.sign=1;
			return c;
		}
		else{
			a.sign=0;
			//b.sign=0;
			c=a+b;
			a.sign=1;
			//b.sign=1;
			c.sign=1;
			return c;
		}
	}
	if(b.sign){
		b.sign=0;
		c=a+b;
		b.sign=1;
		return c;
	}

	if(a<b){
		c=b-a;
		c.sign=1;
		return c;
	}

	c=a;
	for(int i=0;i<c.l;i++){
		c.n[i]-=b.n[i];
		if(c.n[i]<0){
			c.n[i]+=radix;
			c.n[i+1]--;
		}
	}
	while(c.n[c.l-1]==0 && c.l>0)c.l--;
	return c;
}
Num& operator+=(Num& a,Num& b){
	a=a+b;
	return a;
}
Num operator+(Num& a,Num& b){
	Num c;
	if(a.sign){
		if(b.sign){
			a.sign=0;
			b.sign=0;
			c=a+b;
			a.sign=1;
			b.sign=1;
			c.sign=1;
			return c;
		}
		else{
			a.sign=0;
			c=b-a;
			a.sign=1;
			return c;
		}
	}
	if(b.sign){
		b.sign=0;
		c=a-b;
		b.sign=1;
		return c;
	}

	int l=a.l;
	if(b.l>l)l=b.l;

	int up=0;
	for(int i=0;i<l;i++){
		c.n[i]=a.n[i]+b.n[i]+up;
		up=c.n[i]/radix;
		c.n[i]%=radix;
	}
	if(up)c.n[l++]=up;
	c.l=l;
	return c;
}
Num& operator*=(Num& a,const Num& b){
	a=a*b;
	return a;
}
Num operator*(const Num& a,const Num& b){
	Num c;
	if(a.l==0 || b.l==0)return c;
	int up=0;
	for(int i=0;i<a.l;i++){
		up=0;
		for(int j=0;j<b.l;j++){
			c.n[i+j]+=a.n[i]*b.n[j]+up;
			up=c.n[i+j]/radix;
			c.n[i+j]%=radix;
		}
		if(up)c.n[i+b.l]+=up;
	}
	c.l=a.l+b.l-1;
	if(c.n[c.l]!=0)c.l++;
	c.sign=(a.sign!=b.sign);
	return c;
}

Num operator/(Num a,const int b){
	if(b<0){
		Num temp=a/(-b);
		temp.sign=!temp.sign;
		return temp;
	}
	int up=0;
	for(int i=a.l-1;i>=0;i--){
		a.n[i]+=up*radix;
		up=a.n[i]%b;
		a.n[i]/=b;
	}
	while(a.n[a.l-1]==0 && a.l>0)a.l--;
	if(a.l==0)a.sign=0;

	return a;
}
int operator%(const Num& a,const int b){
	int now=0;
	for(int i=a.l-1;i>=0;i--){
		now*=radix;
		now+=a.n[i];
		now%=b;
	}
	if(a.sign)now=-now;
	return now;
}
Num& operator++(Num& a,int){
	if(a.sign==1){
		a.sign=0;
		a--;
		if(a.l)a.sign=1;
		return a;
	}

	a.n[0]++;
	int i=0;
	while(a.n[i]>=radix){
		a.n[i]-=radix;
		i++;
		a.n[i]++;
	}
	if(i==a.l)a.l++;
	return a;
}
Num& operator--(Num& a,int){
	if(a.sign){
		a.sign=0;
		a++;
		a.sign=1;
		return a;
	}
	if(a.l==0){
		a.Set(-1);
		return a;
	}
	a.n[0]--;
	int i=0;
	while(a.n[i]<0){
		a.n[i]+=radix;
		i++;
		a.n[i]--;
	}
	if(a.n[a.l-1]==0)a.l--;
	return a;
}

const int modi=10007;


int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);

	int n;
	scanf("%d",&n);
	for(int t=1;t<=n;t++){
		int h,w,r;
		scanf("%d %d %d",&h,&w,&r);

		bool trap[128][128]={0};
		for(int i=0;i<r;i++){
			int rr,cc;
			scanf("%d %d",&rr,&cc);
			trap[rr][cc]=1;
		}

		int dp[128][128]={0};
		dp[1][1]=1;
		for(int i=1;i<120;i++){
			for(int j=1;j<120;j++){
				if(trap[i][j])continue;
				dp[i+1][j+2]+=dp[i][j]; dp[i+1][j+2]%=modi;
				dp[i+2][j+1]+=dp[i][j]; dp[i+2][j+1]%=modi;
			}
		}

		printf("Case #%d: %d\n",t,dp[h][w]);
	}
}