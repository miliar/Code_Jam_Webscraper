

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

typedef struct
{
	char s[100];
	//int i;
}mybignum;

void mybignum_print(mybignum a)
{
	int i;
	int view=0;
	//printf("%d",a.i);
	for (i=99;i>=0;i--){
		if (!(0<=a.s[i] && a.s[i]<=9)){
			printf("%d\n",(int)a.s[i]);
			assert(0);
		}
		if (a.s[i]!=0)view=1;
		if (view)
			printf("%d",(int)a.s[i]);
	}
	if (view==0)printf("0");
}

mybignum mybignum_scan(void)
{
	char s[100];
	mybignum ret;
	scanf("%s ",s);
	memset(&ret,0,sizeof(ret));
	int i,len;
	len=strlen(s);
	for (i=0;i<len;i++){
		ret.s[i]=s[len-1-i]-'0';
	}
	return ret;
}

int mybignum_ge(mybignum a,mybignum b)
{
	int i;
	for (i=99;i>=0;i--){
		if (a.s[i]>b.s[i])return 1;
		if (a.s[i]<b.s[i])return 0;
	}
	return 0;
}

//結果が負になる計算はやらないはず。
mybignum mybignum_sub(mybignum a,mybignum b)
{
	mybignum ret;
	int i;
	int c=0;
	memset(&ret,0,sizeof(ret));
	for (i=0;i<100;i++){
		if (a.s[i]<b.s[i]+c){
			//繰り下がり
			ret.s[i]=a.s[i]-b.s[i]-c+10;
			c=1;
		}
		else{
			ret.s[i]=a.s[i]-b.s[i]-c;
			c=0;
		}
		assert(0<= ret.s[i] && ret.s[i]<=9);
	}
	return ret;
}

mybignum mybignum_inc(mybignum a)
{
	mybignum ret,dummy;
	int i;
	int c=0;
	memset(&dummy,0,sizeof(dummy));
	dummy.s[0]=1;
	for (i=0;i<100;i++){
		if (a.s[i]+dummy.s[i]+c>9){
			//繰り上がり
			ret.s[i]=a.s[i]+dummy.s[i]+c-10;
			c=1;
		}
		else{
			ret.s[i]=a.s[i]+dummy.s[i]+c;
			c=0;
		}
	}
	return ret;
}

int mybignum_iszero(mybignum a)
{
	int i;
	for (i=0;i<100;i++){
		if (a.s[i]!=0)return 0;
	}
	return 1;
}

mybignum mybignum_div(mybignum a,mybignum b)
{
	mybignum ret;
	int i;
	char tmp[200];
	memset(tmp,0,sizeof(tmp));
	memcpy(&tmp[0],a.s,100);
	memset(&ret,0,sizeof(ret));
	for (i=100;i>=0;i--){
		//もし大きいなら引く、というのを繰り返す
		while (1){
			int j;
			int exit=0;
			for (j=99;j>=0;j--){
				if (tmp[i+j]>b.s[j]){exit=0;break;}
				if (tmp[i+j]<b.s[j]){exit=1;break;}
			}
			if (exit==1)break;
			//引く
			int c=0;
			for (j=0;j<100;j++){
				if (tmp[i+j]<b.s[j]+c){
					//繰り下がり
					tmp[i+j]=tmp[i+j]-b.s[j]-c+10;
					c=1;
				}
				else{
					tmp[i+j]=tmp[i+j]-b.s[j]-c;
					c=0;
				}
			}
			//インクリメント
			ret.s[i]++;
		}
	}
	return ret;
}

mybignum mybignum_mul(mybignum a,mybignum b)
{
	char tmp[200];
	mybignum ret;
	int i,j;
	memset(tmp,0,sizeof(tmp));
	for (i=0;i<100;i++){
		for (j=0;j<100;j++){
			//部分積を計算。足していく
			int val=a.s[i]*b.s[j];
			int k=0;
			int c=0;
			while (val || c)
			{
				if (tmp[i+j+k]+c+val%10>9){
					tmp[i+j+k]+=val%10+c-10;
					c=1;
				}
				else{
					tmp[i+j+k]+=val%10+c;
					c=0;
				}
				val/=10;
				k++;
			}
		}
	}
	memcpy(ret.s,tmp,100);
	return ret;
}

mybignum mybignum_mod(mybignum a,mybignum b)
{
	mybignum ret;
	int i;
	char tmp[200];
	memset(tmp,0,sizeof(tmp));
	memcpy(&tmp[0],a.s,100);
	memset(&ret,0,sizeof(ret));
	for (i=100;i>=0;i--){
		//もし大きいなら引く、というのを繰り返す
		while (1){
			int j;
			int exit=0;
			for (j=99;j>=0;j--){
				if (tmp[i+j]>b.s[j]){exit=0;break;}
				if (tmp[i+j]<b.s[j]){exit=1;break;}
			}
			if (exit==1)break;
			//引く
			int c=0;
			for (j=0;j<100;j++){
				if (tmp[i+j]<b.s[j]+c){
					//繰り下がり
					tmp[i+j]=tmp[i+j]-b.s[j]-c+10;
					c=1;
				}
				else{
					tmp[i+j]=tmp[i+j]-b.s[j]-c;
					c=0;
				}
			}
		}
	}
	memcpy(ret.s,tmp,100);
	return ret;
}

mybignum gcd(mybignum m,mybignum n)
{
	mybignum tmp;
	if (mybignum_ge(n,m)){tmp=m;m=n;n=tmp;}
	while (1){
		if (mybignum_iszero(n))return m;
		if (mybignum_iszero(mybignum_mod(m,n)))return n;
		tmp=n;n=mybignum_mod(m,n);m=tmp;
	}
}

int main(void) {
	int i,j;
	int minidx;
	mybignum min,y;
	int C,N;
	mybignum *t;
	scanf("%d\n",&C);
	for (i=0;i<C;i++){
		scanf("%d ",&N);
		t=new mybignum[N];
		minidx=-1;
		for (j=0;j<N;j++){
			//新しいやつを読む
			t[j]=mybignum_scan();
			//最小値を記録しておく
			if (minidx<0 || mybignum_ge(min,t[j])){
				minidx=j;min=t[j];
			}
		}
		//mybignum_print(t[0]);printf("\n");
		//mybignum_print(t[1]);printf("\n");
		//mybignum_print(mybignum_mul(t[0],t[1]));printf("\n");
		for (j=0;j<N;j++){
			//最小値を引く
			t[j]=mybignum_sub(t[j],min);
		}
		//すべてのtの最大公約数を求める
		int init=0;
		for (j=0;j<N;j++){
			if (j==minidx)continue;
			if (!init){
				y=t[j];
				init=1;
				continue;
			}
			y=gcd(t[j],y);
		}
		//mybignum_print(y);printf("\n");
		//mybignum_print(min);printf("\n");
		//オフセットをもとにもどす
		mybignum n;
		n=mybignum_div(min,y);
		//mybignum_print(n);printf("\n");
		//mybignum_print(mybignum_mod(min,y));printf("\n");
		if (!mybignum_iszero(mybignum_mod(min,y))){
			n=mybignum_inc(n);
			//mybignum_print(n);printf("\n");
		}
		y=mybignum_sub(mybignum_mul(n,y),min);
		printf("Case #%d: ",i+1);
		mybignum_print(y);
		printf("\n");
		delete[] t;
	}
	return 0;
}
