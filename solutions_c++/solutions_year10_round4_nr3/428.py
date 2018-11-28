#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

bool a[128][128];
int main(){
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		int n;
		scanf("%d",&n);
		memset(a,false,sizeof(a));
		for(int i=0;i<n;i++){
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int i=x1;i<=x2;i++)
				for(int j=y1;j<=y2;j++)
					a[i][j]=true;
		}
		int num=0;
		while(true){
			num++;
			bool found=false;
			for(int i=127;i>=0;i--)
				for(int j=127;j>=0;j--){
					bool A=a[i][j];
					bool B=i>=0&&a[i-1][j];
					bool C=j>=0&&a[i][j-1];
					a[i][j]=A&&B||A&&C||B&&C;
					if(a[i][j])
						found=true;

				}
			if(!found)
				break;
		}
		printf("Case #%d: %d\n",++cas,num);
	}
}
