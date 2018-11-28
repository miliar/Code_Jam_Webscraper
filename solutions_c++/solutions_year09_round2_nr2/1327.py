#include <cstdio>
#include <cstring>
#include <cctype>
#include <map>
#include <sstream>
#include <iostream>
#include <string>

using namespace std;

int arr[25];

int main(){
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++){
        printf("Case #%d: ",t);
        
        int n;
        scanf("%d",&n);
        int len=0;
        
        int n2=n;
        while(n2){
            arr[len++]=n2%10;
            n2/=10;
        }
        
        sort(arr,arr+len);
        
        int res=-1;
        int mmin=0x3f3f3f3f;
        int rmin=0x3f3f3f3f;
        
        do{
            if(arr[0]){
                int temp=0;
                for(int i=0;i<len;i++)
                    temp=temp*10+arr[i];
                if(temp>n&&temp-n<mmin){
                    mmin=temp-n;
                    res=temp;
                }
                if(temp<rmin)
                    rmin=temp;
            }
            
        }while(next_permutation(arr,arr+len));
        if(res==-1){
            ostringstream out;
            out<<rmin;
            printf("%s0%s\n",out.str().substr(0,1).c_str(),out.str().substr(1).c_str());
        }else{
            printf("%d\n",res);
        }
    }
    return 0;
}
