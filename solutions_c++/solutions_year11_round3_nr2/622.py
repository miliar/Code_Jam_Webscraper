#include<stdio.h>
#include<algorithm>
#define max 1000
FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");
struct _A{
	int a,cnt,e;
};
bool compare(_A a,_A b){
	return a.e>b.e;
}
_A a[max+5];
int l,n,c;
__int64 t,tsum,res;
void input(){
	tsum=0;
	fscanf(in,"%d%I64d%d%d",&l,&t,&n,&c);
	t/=2;
	for(int i=0;i<c;i++){
		fscanf(in,"%d",&a[i].a);
		a[i].e=a[i].a;
		tsum+=a[i].a;
	}
}
int min(int a,int b){
	if(a<b) return a;
	return b;
}
void process(){
	__int64 cs,ss;
	res=tsum*(n/c)*2;
	cs=t/tsum;
	__int64 imsi=t%tsum;
	for(int i=0;i<c;i++){
		if(i<n%c) res+=a[i].a*2;
		if(imsi>=0) a[i].cnt=n/c-(cs+1);
		else a[i].cnt=n/c-cs;
		if(i<n%c) a[i].cnt++;
		if(imsi>=0){
			imsi-=a[i].a;
			if(imsi<0){
				a[c].e=-imsi;
				a[c].cnt=1;
				ss=i;
			}
		}
	}
	std::sort(a,a+c+1,compare);
	for(int i=0;i<c;i++){
		if(a[i].cnt>=0){
			res-=min(l,a[i].cnt)*a[i].e;
			l-=min(l,a[i].cnt);
		}
	}
}
void output(int tc){
	fprintf(out,"Case #%d: %I64d\n",tc,res);
}
int main(){
	int t;
	fscanf(in,"%d",&t);
	for(int i=0;i<t;i++){
		input();
		process();
		output(i+1);
	}
	fclose(in);
	fclose(out);
	return 0;
}
