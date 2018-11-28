#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <set>
#include <algorithm>

using namespace std;
#define TASK "file"
int test;

#define N 50

int a[N][N];
int last[N];
int n;

int main(void){
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
	
	scanf("%i\n",&test);
	for (int tst=0;tst<test;tst++){
		printf("Case #%i: ",tst+1);
		scanf("%i\n",&n);
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				char c;
				scanf("%c",&c);
				a[i][j]=c-'0';
			}
			scanf("\n");
		}
		/*for (int i=0;i<n;i++){
			for (int j=0;j<n;j++) cout<<a[i][j]<<" ";
			cout<<endl;
		}*/
		int ans=0;
		for (int i=0;i<n;i++){
			last[i]=-1;
			for (int j=0;j<n;j++)
				if (a[i][j]==1) last[i]=j;
			//cout<<last[i]<<endl;
		}
		int flag=1;
		for (int i=0;i<n;i++){
			if (last[i]>i){
				int k=i;
				for (int j=i+1;j<n;j++)
					if (last[j]<=i){
						k=j;
						break;
					}
				if (k!=i){
					int j=k;
					while (j>i){
						ans++;
						swap(last[j],last[j-1]);
						j--;
					}
				}
			}
		}
		if (flag)
			cout<<ans<<endl;
		else cout<<"fuck!"<<endl;
	}

	
	return 0;
}