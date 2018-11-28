#include <string> 
#include <vector> 
#include <map> 
#include <utility> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <queue> 
#include <stack> 
#include <set> 
#include <sstream> 
#include <algorithm> 
#include <iostream> 
#include <iomanip> 
using namespace std;
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<int,int> pii; 

char buff[50005];
char bufc[50005];
int perm[20];
char temp[20];


int main(){
    int test;
    scanf("%d",&test);
    for(int t=0;t<test;t++){
        printf("Case #%d: ",t+1);
        int k;
        scanf("%d",&k);
        scanf("%s",buff);
        //printf("%d\n",k);
        for(int i=0;i<k;i++)
            perm[i]=i;
        int len=strlen(buff);
        int res=len;
        do{
            memcpy(bufc,buff,sizeof(buff));
            //printf("%s\n",bufc);
            for(int i=0;i<len;i+=k){
                for(int j=0;j<k;j++)
                    temp[j]=bufc[i+perm[j]];
                for(int j=0;j<k;j++)
                    bufc[i+j]=temp[j];                
            }            
            //printf("%s\n",bufc);
            int c=1;
            for(int i=1;i<len;i++)
                if(bufc[i]!=bufc[i-1])
                    c++;
            res<?=c;
        }while(next_permutation(perm,perm+k));
        printf("%d\n",res);
    }
}
