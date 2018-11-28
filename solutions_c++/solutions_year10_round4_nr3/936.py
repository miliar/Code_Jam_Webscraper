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

int arr[1005][1005];

int main(){
    int test;
    scanf("%d",&test);
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        int r;
        scanf("%d",&r);
        memset(arr,0,sizeof(arr));
        for(int i=0;i<r;i++){
            int x1,y1,x2,y2;
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
            
            for(int i=y1;i<=y2;i++)
            for(int j=x1;j<=x2;j++)
                arr[i][j]=1;
            
        }
        /*for(int i=0;i<10;i++){
        for(int j=0;j<10;j++)
            cout<<arr[i][j]<<" ";
        cout<<endl;
        }*/
        
        int res=0;
        bool found=true;
        while(found){
            found=false;
            int ch=false;
            for(int i=205;i>=1;i--)
                for(int j=205;j>=1;j--)
                    if(!arr[i][j]){
                        if(arr[i-1][j]&&arr[i][j-1]){
                            arr[i][j]=1;
                            found=true;
                            ch=true;
                        }
                    }
                    else{
                        ch=true;
                        if(!arr[i-1][j]&&!arr[i][j-1])
                            arr[i][j]=0;
                        else
                            found=true;
                    }
            if(ch) res++;
        } 
        printf("%d",res);    
        printf("\n");
    }    
}
