#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;


int que[10],mode[10]={10,100,1000,10000,100000,1000000,10000000};
int has[10];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ca = 1;ca<=t;ca++){
        int a,b,sum = 0;
        scanf("%d%d",&a,&b);
        for(int i=a,j,te,tem,m;i<=b;i++){
            te = i,j=m=0;
            while(te>=mode[j])j++;
            for(int k=0;k<j;k++){
                tem = te%mode[k]*mode[j-k-1]+te/mode[k];
                if(tem<=b&&a<=tem&&tem!=i){
                    bool x = 1;
                    for(int l=0;l<m;l++){
                        if(que[l]==tem){
                            x = 0;
                            break;
                        }
                    }
                    if(x){
                        sum++;
                        que[m++] = tem;
                    }
                    //cout << tem << ' ' << i << endl;
                }
            }
        }
        printf("Case #%d: %d\n",ca,sum/2);
    }
    return 0;
}
