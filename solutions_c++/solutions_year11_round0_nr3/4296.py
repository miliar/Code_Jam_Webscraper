
#include <iostream>

using namespace std;


const int maxn = 1100;
const int maxc=11000000;
int n;

int a[maxn];
int d[maxc];
int e[maxc];

int main() {
  int nt;
  cin>>nt;
  for (int t=1;t<=nt;t++){
	cout<<"Case #"<<t<<": ";
	cin>>n;
	for (int i=0;i<n;i++)
	  cin>>a[i];
	
	int sum=0;
	int sum2=0;
	int lo=a[0];
	for (int i=0;i<n;i++) {
	  sum^=a[i];
	  sum2+=a[i];
	  lo=min(lo,a[i]);
	};
	if (sum!=0) {
	  cout<<"NO"<<endl;
	  continue;
	}

	cout<<sum2-lo<<endl;
	/*
	memset(d,0,sizeof d);
	memset(e,0,sizeof e);

	int *pd=d;
	int *pe=e;

	d[0]=1;
	int top=1;
	
	for (int i=0;i<n;i++) {
	  int z=a[i];
	  for (int x=top;x>=0;x--) pe[x]=pd[x];
	  for (int x=top;x>=0;x--)
		if (pd[x]) {
		  int y=x+z;
		  top=max(top,y);
		  pe[y]=1;
		}
	  swap(pe,pd);
	}
	cout<<top<<endl;*/
  };

  return 0;
}

