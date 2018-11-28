#include <iostream>
using namespace std;

int main(){
    int N;
    cin>>N;
    char str[]="welcome to code jam";
    int count[30];
    cin.ignore(1,'\n');
    for(int i=0;i<N;++i){
        char text[501];
        cin.getline(text,500);
        memset(count,0,sizeof(count));
        for(int j=0;j<strlen(text);++j){
            for(int k=0;k<strlen(str);++k){
                if(text[j]==str[k]){
                    if(k==0)++count[k];
                    else count[k]+=count[k-1];
                    if(count[k]>10000)
                    count[k]%=10000;
                }
            }
        }
        int r=count[18]%10000;
        cout<<"Case #"<<i+1<<": "<<r/1000<<r/100%10<<r/10%10<<r%10<<endl;
    }
    return 0;
}
