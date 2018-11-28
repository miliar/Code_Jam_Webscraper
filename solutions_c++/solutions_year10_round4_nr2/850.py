#include <iostream>
#include <string.h>
using namespace std;

int a[5010],k ,t ,p ,b[2010],d[21];

bool check(){
	for(int i=0;i<d[p];i++)
		if(b[i]>0)
			return true;
	return false;
}

int main(){
	for(int i = 0; i < 20; i ++)	d[i] = 1<<i;
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	cin >> t;
	for(int idx = 1; idx <= t; idx ++) {
		memset(a,0,sizeof(a));
		cin >> p;
		for(int i=0;i<d[p];i++){
			cin >> b[i];
			b[i]=p-b[i];
		}
		for(int i=0;i<d[p]-1;i++)
			cin >> k;
		int n = 0, m = 0;
		for(int pos = 1; check(); m ++){
			if(m==0){
				for(int i=0;i<d[p];i++)
				b[i]--;
				n++;
			} else {
				for(int i=0; i<d[m]; i++){
					pos = 0;
					for(int j=d[p-m]*i;j<d[p-m]*(i+1);j++)
						if(b[j]>0)
							pos=1;
					if(pos) {
						for(int j=d[p-m]*i;j<d[p-m]*(i+1);j++)
							b[j]--;
						n++;
					}
				}
			}
		}
		printf("Case #%d: %d\n", idx, n);
	}
	return 0;
}
