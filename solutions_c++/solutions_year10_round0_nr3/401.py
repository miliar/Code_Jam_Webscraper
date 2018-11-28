#include <stdio.h>
#include <iostream>

using namespace std;
#define LL long long

LL data[1500],num[1500],next[1500],k,r,n;

void find(LL a) {
	LL i,cur = 0;
	//printf ("\nfind %lld\n",a);
	for (i=0;i<n;i++) {
		LL x = data[(a+i)%n];
		//printf ("%lld ",cur+x);
		if (cur+x<=k)
			cur += x;
		else {
			num[a] = cur;
			next[a] = (a+i)%n;
			return;
		}
	}
	num[a] = cur;
	next[a] = a;
}

LL findcycle() {
	LL i,cur,pos,x,cyclen,rot,rem,res,tres,st,tmp;
	LL chk[1500];
	for (i=0;i<n;i++) chk[i] = -1;
	cur = 0;pos = 0;
	while (true) {
		x = next[cur];
		//cout << cur << "-";
		if (chk[cur]!=-1) {
			cyclen = pos-chk[cur];
			st = chk[cur]; //st+(N-1)*cyclen
			break;
		}
		chk[cur] = pos;
		pos++;
		cur = x;
	}
	//printf ("%lld %lld\n",r,st);
	res = 0;
	if (r<=st) {
		cur= 0;
		while (r--) {
			res += num[cur];
			cur = next[cur];
		}
		return res;
	}
	rot = (r-1-st)/cyclen ; rem = (r-1-st)%cyclen;
	//printf ("%lld %lld %lld %lld\n",st,cyclen, rot,rem);
	tmp = st; cur = 0;
	while (tmp--) {
		res += num[cur];
		cur = next[cur];
	}
	//printf ("%lld\n",res);
	tmp = st; tres= 0; cur = 0;
	while (tmp--) cur = next[cur];
	tmp = cyclen;
	while (tmp--) {
		tres += num[cur];
		//printf ("%lld\n",num[cur]);
		cur = next[cur];
	}
	res += rot*tres;
	//printf ("%lld %lld\n",res,tres);
	tmp = st; cur = 0;
	while (tmp--) cur = next[cur];
	tmp = rem+1;
	while (tmp--) {
		res += num[cur];
		cur = next[cur];
	}
	return res;
}

int main () {
	LL t,ii,i;
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	scanf ("%lld",&t);
	for (ii=1;ii<=t;ii++) {
		scanf ("%lld%lld%lld",&r,&k,&n);
		for (i=0;i<n;i++) scanf ("%lld",&data[i]);
		for (i=0;i<n;i++) find(i);
		/*for (i=0;i<n;i++) cout << num[i] << " ";
		cout << endl;
		for (i=0;i<n;i++) cout << next[i] << " ";
		cout << endl;*/
		printf ("Case #%lld: %lld\n",ii,findcycle());
	}
	return 0;
}
