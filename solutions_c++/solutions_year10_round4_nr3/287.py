#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <bitset>

using namespace std;

int a[500][500];
int b[500][500];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int c;
	scanf("%d",&c);

	for (int cc=1; cc<=c; cc++){
		memset(a,0,sizeof(a));
		printf("Case #%d: ",cc);

		int n;
		scanf("%d",&n);

		for (int i=1; i<=n; i++){
			int x,b,c,d;
			scanf("%d%d%d%d",&x,&b,&c,&d);
			for (int j=b; j<=d; j++)
				for (int k=x; k<=c; k++)
					a[j][k]=1;
		}

		int k=1;
		int t=0;
		while (k>0){
			k=0;
			memset(b,0,sizeof(b));

			for (int i=0; i<500; i++)
				for (int j=0; j<500; j++)
					if (a[i][j]==1&&a[i-1][j]==0&&a[i][j-1]==0) k++, b[i][j]=0; else
						if (a[i-1][j]==1&&a[i][j-1]==1&&a[i][j]==0) k++, b[i][j]=1; else
							b[i][j]=a[i][j];

			for (int i=0; i<500; i++)
				for (int j=0; j<500; j++)
					a[i][j]=b[i][j];
			if (k>0) t++;
		}
		printf("%d\n",t);
	}

	return 0;
}