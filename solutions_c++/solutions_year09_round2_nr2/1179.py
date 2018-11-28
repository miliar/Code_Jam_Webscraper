#include <iostream>
#include <vector>
using namespace std;

int compare(const void *a,const void *b){
        return *(char*)a-*(char*)b;
}
int main(){
    int N,x;

    cin>>N;
    char num[30];
    int i,k;
    for(int j=0;j<N;++j){
        cin>>num;
        cout<<"Case #"<<j+1<<": ";
        for(i=strlen(num)-1;i>0;--i){
            if(num[i-1]<num[i])break;
        }
        if(i==0){
            int temp=strlen(num)-1;
            while(num[temp]=='0')--temp;
            cout<<num[temp]<<0;
            for(i=strlen(num)-1;i>=0;--i){
                if(i!=temp)
                cout<<num[i];
            }
            cout<<endl;
            continue;
        }
        for(k=0;k<i-1;++k){
            cout<<num[k];
        }
        for(k=strlen(num)-1;k>=0;--k){
            if(num[k]>num[i-1])break;
        }
        cout<<num[k];
        num[k]=num[i-1];
        qsort(&num[i],strlen(num)-i,1,compare);
        for(k=i;k<strlen(num);++k){
            cout<<num[k];
        }
        cout<<endl;
    }
    return 0;
}
