#include <stdio.h>
#include <string.h>
#include <fstream>
#include <stdlib.h>

using namespace std;

int hashcode(int n) {
	int p;
	p=(n>>4)^(n<<10);
	p%=99983;
	if(p<0)
		p+=99983;
	return p;
}

int comp1(const void *__a,const void *__b) {
	return *(int *)__b - *(int *)__a;
}

int main() {
	int __T;
	fstream r0("C-small-attempt0.in",fstream::in);
	fstream w0("test.out",fstream::out);
	r0>>__T;
	for(int T=1;T<=__T;T++) {
		int N,L,H;
		r0>>N>>L>>H;
		int hash[100000];
		memset(hash,0xff,sizeof(hash));
		for(int i=0;i<N;i++) {
			int temp;
			r0>>temp;
			int hc=hashcode(temp);
			while(hash[hc]!=temp) {
				if(hash[hc]==-1) {
					hash[hc]=temp;
					break;
				}
			}
		}
		int a[10000],aN;
		int p1=0;
		for(int p0=0;p0<100000;p0++) {
			if(hash[p0]==-1)
				continue;
			a[p1++]=hash[p0];
		}
		aN=p1;

		qsort(a,aN,sizeof(int),comp1);
		bool map[10001];
		memset(map,false,sizeof(map));
		for(int i=1;i<10001;i++) {
			bool flag=true;
			for(int j=0;j<aN;j++)
				if(a[j]%i!=0 && i%a[j]!=0) {
					flag=false;
					break;
				}
			if(flag)
				map[i]=true;
		}

		int result=-1;
		for(int i=L;i<=H;i++) {
			if(map[i]) {
				result=i;
				break;
			}
		}

		w0<<"Case #"<<T<<": ";
		if(result==-1)
			w0<<"NO\n";
		else
			w0<<result<<endl;


	}
	return 0;
}
