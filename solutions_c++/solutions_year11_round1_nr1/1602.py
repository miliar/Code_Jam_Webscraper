

#include <iostream>
#include <cmath>
using namespace std;


int main()
{
	freopen("t.in","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	freopen("t.out","w",stdout);

	int cas;
	scanf("%d", &cas);
	for(int cas_n = 1;cas_n<=cas;cas_n++)
	{
		int n,dg,pg;
		scanf("%d %d %d\n", &n,&dg,&pg);
		
		bool suc = false;

		if(pg == 100 && dg != 100)
			suc = false;
		else if (pg == 0 && dg != 0 ){
			suc = false;
		}else if (dg == 0){
			suc = true;
		}else{
		
			for (int d=1;d<=n ;d++){
				for(int wd = 0;wd<=d; wd++){
					if((wd*100) == (dg*d)  ){
						suc = true;
						break;
					}
				}
			}
		}
		if(suc)
			printf("Case #%d: Possible\n", cas_n);
		else
			printf("Case #%d: Broken\n", cas_n);
	}
	return 0;
}