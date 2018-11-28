#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
int data[100];
int mp[100];
int P[10]={
    10,10,10,10,10,2
};
int usedpd[3000];

bool pd(int n,int a[]) {
    int top=0;
    usedpd[top]=a[0];
    for (int i=1;i<n-1;i++) {
        while (top>=0&&i+1==usedpd[top]) top--;
        if (top==-1) usedpd[++top]=a[i];
        else {
            if (usedpd[top]<a[i]) return false;
            if (usedpd[top]>a[i]) usedpd[++top]=a[i];
        }
    }
    return true;
}

int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int kase;
    scanf("%d",&kase);
    for(int kases=1;kases<=kase;kases++){
        int n;
        scanf("%d",&n);
        for(int i=0;i<n-1;i++)scanf("%d",&data[i]);
        printf("Case #%d:",kases);
        //printf("=====%s\n",pd(n,data)?"YES":"NO");
        if(!pd(n,data)){
            printf(" Impossible\n");
            continue;
        }
        int tm=100000000;
        while(--tm){
            for(int i=0;i<n;i++)mp[i]=rand()%30;
            int f=1;
            for(int i=0;i<n-1;i++){
                double best=-1.0;
                int t=-1;
                for(int j=i+1;j<n;j++){
                    double tmp = atan2(j-i,mp[i]-mp[j]);
                    if(tmp>best){
                        best=tmp;
                        t=j+1;
                    }
                }
                if(t!=data[i]){
                    f=0;
                    break;
                }
            }
            if(f){
                for(int i=0;i<n;i++)printf(" %d",mp[i]);
                printf("\n");
                break;
            }
        }
    }


	return 0;
}
