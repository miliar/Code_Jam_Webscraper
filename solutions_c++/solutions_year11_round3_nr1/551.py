#include <string> 
#include <vector> 
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
char arr[105][105];

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d:\n",tt);
        int r,c;
        scanf("%d %d",&r,&c);
        for(int i=0;i<r;i++)
            scanf("%s",arr[i]);    
        
        bool pos=true;
        for(int i=0;i<r&&pos;i++)
        for(int j=0;j<c&&pos;j++)
            if(arr[i][j]=='#'){
                if(i<r&&j<c&&i+1<r&&j+1<c&&arr[i][j]=='#'&&arr[i][j+1]=='#'&&arr[i+1][j]=='#'&&arr[i+1][j+1]=='#'){
                    arr[i][j]='/';
                    arr[i][j+1]='\\';
                    arr[i+1][j]='\\';
                    arr[i+1][j+1]='/';
                }else{
                    pos=false;
                }
            }
        if(pos){
            for(int i=0;i<r;i++)
                printf("%s\n",arr[i]);
        }else
            printf("Impossible\n");
    }

    return 0;
}

