#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	int ks,p,q,i,j,k,t;
	int f[120][120];
	int l[129];
	cin >> ks;
for (t=1;t<=ks;t++)
{
	cin >> p >> q;
	for (i=1;i<=q;i++)
		cin >> l[i];
	l[0]=0;
	l[q+1]=p+1;
	memset(f,1,sizeof(f));
	for (i=0;i<=q;i++)
		f[i][i+1]=0;
	for (i=2;i<=q+1;i++)
		for (j=0;i+j<=q+1;j++)
			for (k=j+1;k<i+j;k++)
				f[j][i+j]=min(f[j][i+j],l[i+j]-l[j]-2+f[j][k]+f[k][i+j]);
	cout << "Case #" << t << ": " << f[0][q+1] << endl;
}
}
