#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;
int opt[502][20];
const char* w="welcome to code jam";
char in[502];
int main(){
    int t;
    scanf("%d",&t);
    getchar();

    int no=1;
    while(t--){
        gets(in);
        memset(opt,0,sizeof(opt));
        int s=-1;
        int l=strlen(in);
        for(int i=0;i<l;i++){
            if(in[i]=='w'){
                opt[i][0]=1;
                s=i;
                break;
            }
        }
        if(s==-1){
            printf("Case #%d: 0000\n",no++);
            continue;
        }
        int ws=1;
        //printf("%d %d\n",l,strlen(w));
        for(int i=0;i<l;i++){
            for(int j=0;j<19;j++){
                if(in[i]!=w[j])continue;

                if(j>0){
                    for(int k=i-1;k>=s;k--)
                    opt[i][j]=(opt[i][j]+opt[k][j-1])%10000;
                    //if(j==18)for(int k=i-1;k>=s;k--)opt[i][j]=(opt[i][j]+opt[k][j])%10000;
                }
                else opt[i][j]=1;
                //printf("(%d,%d,%d)\n",i,j,opt[i][j]);
            }
        }
        int ans=0;
        for(int i=0;i<l;i++)ans=(ans+opt[i][18])%10000;
        printf("Case #%d: %04d\n",no++,ans);
    }
	return 0;
}

