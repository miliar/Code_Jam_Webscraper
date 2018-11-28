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
char dic[5002][17];
char str[1024];
struct Pa{
    char s[26];
}pa[16];
int main(){
    int l,d,n;
    while(scanf("%d %d %d",&l,&d,&n)!=EOF){
        for(int i=0;i<d;i++) scanf("%s",dic[i]);
        int no=1;
        while(n--){

            scanf("%s",str);
            memset(pa,0,sizeof(pa));
            int len=strlen(str);
            int p=0;
            for(int i=0;i<len;i++){
                if(str[i]=='('){
                    for(i=i+1;i<len&&str[i]!=')';i++)pa[p].s[str[i]-'a']=1;
                    p++;
                }
                else pa[p++].s[str[i]-'a']=1;
            }
            int ans=0;
            for(int i=0;i<d;i++){
                int len=strlen(dic[i]);
                int j=0;
                for(j=0;j<len;j++){
                    if(!pa[j].s[dic[i][j]-'a'])break;
                }
                if(j>=len)ans++;
            }
            printf("Case #%d: %d\n",no++,ans);
        }
    }
	return 0;
}

