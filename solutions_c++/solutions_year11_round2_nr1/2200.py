#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;

struct Table {
	int op[100];
	int wsum;
	int lsum;
};

int main() {
	fstream r0("A-large.in",fstream::in);
	fstream w0("test.out",fstream::out);
	int __T;
	r0>>__T;
	for(int T=1;T<=__T;T++) {
		int n;
		r0>>n;

		Table a[100];
		for(int i=0;i<n;i++) {
			a[i].wsum=0;
			a[i].lsum=0;
			while(r0.get()!='\n')
				;
			for(int j=0;j<n;j++) {
				char temp=r0.get();
				if(temp=='.')
					a[i].op[j]=-1;
				if(temp=='1') {
					a[i].op[j]=1;
					a[i].wsum++;
				}
				if(temp=='0') {
					a[i].op[j]=0;
					a[i].lsum++;
				}
			}
		}

		double wp[100],owp[100],oowp[100];
		for(int i=0;i<n;i++)
			wp[i]=(double)a[i].wsum/(a[i].wsum+a[i].lsum);
		for(int i=0;i<n;i++) {
			double opwp[100];
			for(int k=0;k<n;k++)
				opwp[k]=-1;
			for(int j=0;j<n;j++) {
				if(a[i].op[j]==-1)
					continue;
				int opwpWsum=a[j].wsum;
				int opwpLsum=a[j].lsum;
				if(a[i].op[j]==1)
					opwpLsum--;
				else
					opwpWsum--;
				opwp[j]=(double)opwpWsum/(opwpWsum+opwpLsum);
			}
			double tempD=0;
			for(int j=0;j<n;j++) {
				if(opwp[j]==-1)
					continue;
				tempD+=opwp[j];
			}
			owp[i]=tempD/(a[i].wsum+a[i].lsum);
		}

		for(int i=0;i<n;i++) {
			double tempD=0;
			for(int j=0;j<n;j++) {
				if(a[i].op[j]==-1)
					continue;
				tempD+=owp[j];
			}
			oowp[i]=tempD/(a[i].wsum+a[i].lsum);
		}

		w0<<"Case #"<<T<<":\n";
		for(int i=0;i<n;i++)
			w0<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
	}
	return 0;
}
