#include <iostream>
#include <string>
#define task "file"


using namespace std;
int test;
int n,m,a;


int main(void){
	freopen(task".in","r",stdin);
	freopen(task".out","w",stdout);
	scanf("%i\n",&test);
	for (int z=1;z<=test;z++){
		scanf("%i %i %i",&n,&m,&a);
		printf("Case #%i: ",z);
		int sol=0;
		
		for (int x1=0;x1<=n;x1++)
			for (int y1=0;y1<=m;y1++)
				for (int x2=0;x2<=n;x2++)
					for (int y2=0;y2<=m;y2++){
						int ans=x1*y1;
						ans+=(x2-x1)*(y1+y2);
						ans+=(-x2*y2);
						if (ans<0) ans=-ans;
						if (ans==a){
							printf("0 0 %i %i %i %i",x1,y1,x2,y2);
							sol=1;
							goto next;
						}
					}
		if (!sol) cout<<"IMPOSSIBLE";
		next: 
		cout<<endl;
	}

	return 0;
}
