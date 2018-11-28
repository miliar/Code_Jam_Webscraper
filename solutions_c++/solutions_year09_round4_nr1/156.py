#include <cstdio>
#include <algorithm>
using namespace std;
int arr[100];
int main()
{
    freopen("c:\\A-large.in","r",stdin);
    freopen("c:\\a.out","w",stdout);
	int test;
	scanf("%d",&test);
	int tt=0;
	while(test--){
		++tt;
		int n;
		scanf("%d",&n);
		for(int i=1;i<=n;i++){
            arr[i]=0;
			getchar();
			for(int j=1;j<=n;j++){
				char tp;
				scanf("%c",&tp);
				if(tp=='1')
                     arr[i]=max(j,arr[i]);
			}
		}
		int ans=0;
		for(int i=1;i<=n;i++){
			for(int j=i;j<=n;j++){
				if(arr[j]<=i){
					for(int k=j;k>i;k--){
						swap(arr[k],arr[k-1]);
						++ans;
					}
				break;
				}
			}
	}
		printf("Case #%d: %d\n",tt,ans);
	}

}
