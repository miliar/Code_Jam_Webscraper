#include <cstdio>
#include <algorithm>
using namespace std;

bool release[110];
int arr[100];

int main(){
	freopen("input.txt","r",stdin);
	freopen("C:\\Users\\ziroy\\Desktop\\output.txt","w",stdout);
	int p,q;
	int m;
	int count;
	scanf("%d",&count);
	for (int _case=1;_case<=count;_case++){
		m = 0x7fffffff;
		scanf("%d%d",&p,&q);
		for (int i=0;i<q;i++)
			scanf("%d",arr+i);
		sort(arr,arr+q);
		
		do{
			int now = 0;
			memset(release,0,sizeof(release));
			for (int i=0;i<q;i++){
				release[arr[i]] = true;
				for (int k=arr[i]-1;k>=1 && !release[k];k--,now++);
				for (int k=arr[i]+1;k<=p && !release[k];k++,now++);
			}
			if (now < m) m = now;
		}while (next_permutation(arr,arr+q));
		printf("Case #%d: %d\n",_case,m);
	}
			

	return 0;
}