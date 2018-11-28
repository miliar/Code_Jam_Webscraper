#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;

int calc[2000];

inline bool check(int x,int base)
{
	int t1=x,t2=x,x1,x2;
	do{
		for (x1=t1,t1=0;x1;x1/=base) t1+=(x1%base)*(x1%base);
		for (x2=t2,t2=0;x2;x2/=base) t2+=(x2%base)*(x2%base);
		for (x2=t2,t2=0;x2;x2/=base) t2+=(x2%base)*(x2%base);
	}while (t1!=1 && t1!=t2);
	return t1==1;
}

int T,c;

int main()
{
	for (int i=0;i<1<<10;++i) calc[i]=2;
	/*scanf("%d",&T);
	for (int test=1;test<=T;++test){
		vector <int> a;
		for (;;){
			scanf("%d",&c);a.push_back(c);
			if (getchar()!=' ') break;
		}
		int mask=0;
		for (int i=0;i<a.size();++i) mask|=1<<a[i]-1;
		for (int j=calc[mask-(mask&-mask)];;++j){
			bool flag=true;
			for (int k=0;k<a.size() && flag;++k) if ((mask>>a[k]-1)&1)
				if (!check(j,a[k])) flag=false;
			if (flag) {calc[mask]=j;break;}
		}
		printf("%d\n",calc[mask]);
	}*/
	for (int mask=0;mask<1<<10;++mask){
		for (int j=calc[mask-(mask&-mask)];;++j){
			bool flag=true;
			for (int k=2;k<=10 && flag;++k) if ((mask>>k-1)&1)
				if (!check(j,k)) flag=false;
			if (flag) {calc[mask]=j;break;}
		}
		printf("%d,\n",calc[mask]);
	}
	return 0;
}
