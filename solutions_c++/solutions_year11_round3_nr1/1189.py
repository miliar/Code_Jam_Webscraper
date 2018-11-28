#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<malloc.h>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<list>
#include<string>
#include<map>
#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SS ({int x;scanf("%d",&x);x;})
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;cin>>t;
    for(int tcase=1;tcase<=t;tcase++){
        int r,c;cin>>r>>c;
        string arr[60];
        for(int i=0;i<r;i++){
            cin>>arr[i];
        }
        int flag=0;
        for(int i=0;i<r && !flag;i++){
            for(int j=0;j<c && !flag;j++){
                if(arr[i][j]=='#'){
                    if(j+1<c && arr[i][j+1]=='#' && i+1<r && arr[i+1][j]=='#' && arr[i+1][j+1]=='#'){
                        arr[i][j]='/';arr[i][j+1]='\\';arr[i+1][j]='\\';arr[i+1][j+1]='/';
                    }
                    else{
                        flag++;
                    }
                }
            }
        }
        cout<<"Case #"<<tcase<<":\n";
        if(flag){
            cout<<"Impossible\n";
        }
        else{
            for(int i=0;i<r;i++){
                cout<<arr[i]<<endl;
            }
        }
    }
}
