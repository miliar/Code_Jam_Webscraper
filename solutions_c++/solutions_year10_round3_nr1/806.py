#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int main(void){
	int run;
	int t;
	int n;
	int i,j;
	int t1,t2;
	int result;
	scanf("%d",&t);
	for(run=0;run<t;run++){
	    vector<int> a;
	    vector<int> b;
	    result=0;
        scanf("%d",&n);
        // inputs
        for(i=0;i<n;i++){
            scanf("%d %d",&t1,&t2);
            a.push_back(t1);
            b.push_back(t2);
        }
        // testing
        for(i=0;i<n;i++){
            for(j=i+1;j<n;j++){
                if(a[i]>a[j]&&b[i]<b[j])result++;
                else if(a[i]<a[j]&&b[i]>b[j])result++;
            }
        }

		printf("Case #%d: %d\n",run+1,result);
	}
	return 0;
}
