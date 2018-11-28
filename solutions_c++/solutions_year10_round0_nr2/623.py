#include <cstdio>
#include <cstdlib>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <cctype>
using namespace std;
#define maxn 1010
#define base 10000
#define baselen 4
struct tlong{
	int len;
	int dig[52];
};
tlong mas[maxn];
int nsc, sc;
int n;
void readlong(tlong &num){
	char s[60];
	scanf(" %s ", s);
	int len=strlen(s);
	num.len=0;
	for(int i=len-1; i>=0; i-=baselen){
		int dig=0;
		for(int j=max(0, i-baselen+1); j<=i; j++)
			dig=dig*10+s[j]-'0';
		num.dig[num.len++]=dig;
	}
	
}
void init(){
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		readlong(mas[i]);
	}
	
}
bool iszero(tlong &a){
	return a.len==1 && a.dig[0]==0;
}
void norm(tlong &a){
	while (a.len>1 && a.dig[a.len-1]==0)
		a.len--;
}
void subl(tlong &a, tlong &b){
	int i, work, ost=0;
	for(int i=0; i<a.len; i++){
		work=a.dig[i]-ost;
		if (i<b.len)
			work-=b.dig[i];
		if (work<0){
			a.dig[i]=work+base;
			ost=1;
		}
		else{
			a.dig[i]=work;
			ost=0;
		}
	}
	
	norm(a);
}
void subl(tlong &a, tlong &b, tlong &res){
	int i, work, ost=0;
	res.len=0;
	for(int i=0; i<a.len; i++){
		work=a.dig[i]-ost;
		if (i<b.len)
			work-=b.dig[i];
		if (work<0){
			res.dig[res.len++]=work+base;
			ost=1;
		}
		else{
			res.dig[res.len++]=work;
			ost=0;
		}
	}
	norm(res);
}
void copyl(tlong &dst, tlong &src){
	dst.len=src.len;
	for(int i=0; i<src.len; i++)
		dst.dig[i]=src.dig[i];
}
void mult(tlong &a, int b,tlong &res){
	res.len=0;
	int work, i, ost=0;
	for(int i=0; i<a.len; i++){
		work=a.dig[i]*b+ost;
		res.dig[res.len++]=work%base;
		ost=work/base;
	}
	while (ost>0){
		res.dig[res.len++]=ost%base;
		ost/=base;
	}
}
bool morel(tlong &a, tlong &b);
void divl(tlong& a, tlong &b, tlong& res, tlong& ost){
	tlong work, work2;
	copyl(ost, a);
	res.len=0;
	for(int i=ost.len-1; i>=0; i--){
		work.len=0;
		for(int j=i; j<ost.len; j++){
			work.dig[work.len++]=ost.dig[j];
		}
		int l=1;
		int r=base-1;
		int mid;
		int best=-1;
		while (l<=r){
			mid=(l+r)/2;
			mult(b, mid, work2);
			if (!morel(work2, work)){
				best=mid;
				l=mid+1;
			}
			else 
				r=mid-1;
				
		}
		if (best==-1)
			continue;
		res.dig[res.len++]=best;
		mult(b, best, work2);
		subl(work, work2);
		for(int j=i; j<work.len; j++)
			ost.dig[j]=work.dig[j-i];
		ost.len=i+work.len;
		norm(ost);
	}
	if (res.len==0)
		res.dig[res.len++]=0;
	for(int i=0; i<res.len/2; i++)
		swap(res.dig[i], res.dig[res.len-i-1]);
	norm(res);
}
tlong getnod(tlong& a, tlong &b){
	if (iszero(b)) return a;
	tlong div,ost;
	divl(a,b,div,ost);
	return getnod(b, ost);
}
bool morel(tlong &a, tlong &b){
	if (a.len>b.len) return true;
	else if (a.len<b.len) return false;
	for(int i=a.len-1; i>=0; i--)
		if (a.dig[i]!=b.dig[i])
			return a.dig[i]>b.dig[i];
	return false;
}
bool cmp(tlong &a, tlong &b){
	return morel(b,a);
}
void printl(tlong &res){
	printf("%d", res.dig[res.len-1]);
	for(int i=res.len-2; i>=0; i--)
		printf("%0*d", baselen, res.dig[i]);
}
void solve(){
	sort(mas, mas+n, cmp);
	tlong nod;
	subl(mas[1],mas[0],nod);
	for(int i=2; i<n; i++){
		tlong dif;
		subl(mas[i], mas[i-1], dif);
		nod=getnod(nod, dif);
	}
	tlong div, ost;
	divl(mas[0], nod, div, ost);
	if (!iszero(ost)){
		subl(nod, ost);
		printf("Case #%d: ",sc);
		printl(nod);
		printf("\n");
	}
	else{
		printf("Case #%d: 0\n", sc);
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &nsc);
	for(sc=1; sc<=nsc; sc++){
		init();
		solve();
	}
	return 0;
}