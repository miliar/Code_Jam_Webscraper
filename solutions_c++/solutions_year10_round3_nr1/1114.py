#include <vector>
#include <cstdio>

using namespace std;


int main(){
    int T;
    scanf("%d", &T);
    for(int cas=1; cas <= T; ++cas){
	vector <int> wa, wb;
	int N;
	scanf("%d",&N);
	int ret=0;
	for(int i=0;i<N;++i){
	    int a,b;
	    scanf("%d%d", &a, &b);
	    for(int j=0;j<wa.size(); ++j){
		
		if(wa[j]<a && wb[j] > b) ++ret;
		if(wa[j]>a && wb[j] < b) ++ret;
	    }
	    wa.push_back(a);
	    wb.push_back(b);
	}
	printf("Case #%d: %d\n", cas, ret);
    }
}
