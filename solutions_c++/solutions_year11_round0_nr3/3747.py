#include<cstdio>
#include<algorithm>
using namespace std;
int candy[1001];
int caso;
void doit(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)scanf("%d",candy+i);
    sort(candy,candy+n);
    int ans=0;
    for(int i=0;i<n;i++){
        ans=ans^candy[i];
        }
    int total=0;
    for(int i=1;i<n;i++)total+=candy[i];
    ans==0?printf("Case #%d: %d\n",++caso,total):printf("Case #%d: NO\n",++caso);
    }
int main(){
    int C;caso=0;
    scanf("%d",&C);
    for(int i=0;i<C;i++)doit();
    }
