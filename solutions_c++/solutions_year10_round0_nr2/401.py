// iii.cpp : Defines the entry point for the console application.
//0-1背包

//#include "stdafx.h"
#include<cstdio>
#include<memory>
#include <math.h>
#include <stdlib.h>
using namespace std;

const int base = 10; // (base^2) fit into int
const int width = 1; // width = log base
const int N = 100; // n * width: 可表示的最大位数
struct bint{
int ln, v[N];
bint (int r = 0) { // r应该是字符串！
for (ln = 0; r > 0; r /= base) v[ln++] = r % base;
}
bint (char a[]) { // r应该是字符串！
for (ln = 0; a[ln] != '\0'; ln++);
int c = 0;ln;
while(a[c] == '0') {ln--;c++;}
int pos = ln-1;
for(;pos>=0;pos--)v[pos] = a[c++]-'0';
}
bint& operator = (const bint& r) {
memcpy(this, &r, (r.ln + 1) * sizeof(int));// !
return *this;
}
} ;
bool operator < (const bint& a, const bint& b){
int i;
if (a.ln != b.ln) return a.ln < b.ln;
for (i = a.ln - 1; i >= 0 && a.v[i] == b.v[i]; i--);
return i < 0 ? 0 : a.v[i] < b.v[i];
}
bool operator <= (const bint& a, const bint& b){
return !(b < a);
}
bint operator + (const bint& a, const bint& b){
bint res; int i, cy = 0;
for (i = 0; i < a.ln || i < b.ln || cy > 0; i++) {
if (i < a.ln) cy += a.v[i];
if (i < b.ln) cy += b.v[i];
res.v[i] = cy % base; cy /= base;
}
res.ln = i;
return res;
}
bint operator - (const bint& a, const bint& b){
bint res; int i, cy = 0;
for (res.ln = a.ln, i = 0; i < res.ln; i++) {
res.v[i] = a.v[i] - cy;
if (i < b.ln) res.v[i] -= b.v[i];
if (res.v[i] < 0) cy = 1, res.v[i] += base;
else cy = 0;
}
while (res.ln > 0 && res.v[res.ln - 1] == 0) res.ln--;
return res;
}
bint operator * (const bint& a, const bint& b){
bint res; res.ln = 0;
if (0 == b.ln) { res.v[0] = 0; return res; }
int i, j, cy;
for (i = 0; i < a.ln; i++) {
for (j=cy=0; j < b.ln || cy > 0; j++, cy/= base) {
if (j < b.ln) cy += a.v[i] * b.v[j];
if (i + j < res.ln) cy += res.v[i + j];
if (i + j >= res.ln) res.v[res.ln++] = cy % base;
else res.v[i + j] = cy % base;
}
}
return res;
}
bint operator / (const bint& a, const bint& b)
{ // ! b != 0
bint tmp, mod, res;
int i, lf, rg, mid;
mod.v[0] = mod.ln = 0;
for (i = a.ln - 1; i >= 0; i--) {
mod = mod * base + a.v[i];
for (lf = 0, rg = base -1; lf < rg; ) {
mid = (lf + rg + 1) / 2;
if (b * mid <= mod) lf = mid;
else rg = mid - 1;
}
res.v[i] = lf;
mod = mod - b * lf;
}
res.ln = a.ln;
while (res.ln > 0 && res.v[res.ln - 1] == 0) res.ln--;
return res; // return mod 就是%运算
}

bint operator % (const bint& a, const bint& b)
{ // ! b != 0
bint tmp, mod, res;
int i, lf, rg, mid;
mod.v[0] = mod.ln = 0;
for (i = a.ln - 1; i >= 0; i--) {
mod = mod * base + a.v[i];
for (lf = 0, rg = base -1; lf < rg; ) {
mid = (lf + rg + 1) / 2;
if (b * mid <= mod) lf = mid;
else rg = mid - 1;
}
res.v[i] = lf;
mod = mod - b * lf;
}
res.ln = a.ln;
while (res.ln > 0 && res.v[res.ln - 1] == 0) res.ln--;
return mod; // return mod 就是%运算
}

int digits(bint& a) // 返回位数
{
if (a.ln == 0) return 0;
int l = ( a.ln - 1 ) * 4;
for (int t = a.v[a.ln - 1]; t; ++l, t/=10) ;
return l;
}
bool read(bint& b, char buf[]) // 读取失败返回0
{
if (1 != scanf("%s", buf)) return 0;
int w, u, ln = strlen(buf);
memset(&b, 0, sizeof(bint));
if ('0' == buf[0] && 0 == buf[1]) return 1;
for (w = 1, u = 0; ln; ) {
u += (buf[--ln] - '0') * w;
if (w * 10 == base) {
b.v[b.ln++] = u; u = 0; w = 1;
}
else w *= 10;
}
if (w != 1) b.v[b.ln++] = u;
return 1;
}
void write(const bint& v){
int i;
printf("%d", v.ln == 0 ? 0 : v.v[v.ln - 1]);
for (i = v.ln - 2; i >= 0; i--)
printf("%d", v.v[i]); // ! 4 == width
printf("\n");
}
/*==================================================*/



char nums[1000][100];
bint bi[1000];
bint cha[1000];

bint gcd(bint x,bint y) //计算最大公约数 
{
	bint z=x%y; 
	while(!(z.ln==0)) 
	{x=y;y=z;z=x%y;}//辗转相除 
	return y;//返回y，即为两者最大公约数 
}

int cmp(const void *a,const void *b)
{
	if(strlen((char *)a) < strlen((char *)b)) return -1;
	else if(strlen((char *)a) > strlen((char *)b)) return 1;
	return strcmp((char *)a,(char*)b);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("1.out","w",stdout);
	int t,n;
	scanf("%d",&t);
	for(int x=1;x<=t;++x)
	{
		scanf("%d",&n);
		for(int i=0;i<n;++i)
		{
			scanf("%s",nums[i]);
		}
		qsort(nums,n,sizeof(nums[0]),cmp);
		for(int i=0;i<n;++i)
		{
			bint tp(nums[i]);
			bi[i] = tp;
		}
		for(int i=0;i<n-1;++i)
			cha[i] = bi[i+1]-bi[i];
		bint tp = cha[0];
		for(int i=1;i<n-1;++i)
		{
			if(cha[i].ln==0) continue;
			tp = gcd(cha[i],tp);
		}
		bint bei = nums[0] / tp;
		bint xx = bei*tp;
		if(xx < bi[0]){xx=xx+tp;}
		bint out = xx-nums[0];
		printf("Case #%d: ",x);
		write(out);
	}
	return 0;
}
