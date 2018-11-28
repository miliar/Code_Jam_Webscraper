#include <stdio.h>
#include <algorithm>
using namespace std;

int main(){
	int ntc;
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		int n,data[1001],res=-1,txor=0,tsum=0;
		scanf("%d",&n);
		for (int i=0;i<n;i++){
			scanf("%d",&data[i]);
			txor^=data[i];
			tsum+=data[i];
		}
		for (int i=0;i<n;i++)
			if ((txor^data[i])==data[i])
				if (tsum-data[i]>res) res=tsum-data[i];
		if (res==-1) printf("Case #%d: NO\n",tc);
		else printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}