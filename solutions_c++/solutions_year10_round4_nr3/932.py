#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <stdio.h>
#include <queue>



using namespace std;
int T,test,t,s,i,l,j,R,X1[1005],X2[1005],Y1[1005],Y2[1005],a[105][105],b[105][105];
int main()
{
	

	freopen("C-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	for(test=1;test<=T;test++)
	{
		cin>>R;
		for(i=0;i<103;i++)
			for(j=0;j<103;j++)
				b[i][j]=a[i][j]=0;
		s=0;
		for(i=0;i<R;i++)
		{
			cin>>X1[i]>>Y1[i]>>X2[i]>>Y2[i];
			for(l=Y1[i];l<=Y2[i];l++)
				for(j=X1[i];j<=X2[i];j++)
					a[l][j]=1,s++;
		}
		t=0;
		while(s)
		{
			for(i=1;i<103;i++)
				for(j=1;j<103;j++)
					if(a[i][j]==0&&(a[i-1][j]+a[i][j-1]==2))
						b[i][j]=1;
			for(i=1;i<103;i++)
				for(j=1;j<103;j++)
					if(a[i][j]&&(a[i-1][j]+a[i][j-1]==0))
						b[i][j]=-1;
			s=0;
			for(i=0;i<103;i++)
				for(j=0;j<103;j++)
					a[i][j]+=b[i][j],s+=a[i][j];
			t++;
			for(i=0;i<103;i++)
				for(j=0;j<103;j++)
					b[i][j]=0;
		}
		cout<<"Case #"<<test<<": "<<t<<"\n";
	}
	return 0;
}