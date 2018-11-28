#include <iostream>
using namespace std;

int n,len,wlen,f[501][501],ans;
string target,word;

int doit(int a,int b){
    if (b==len) return 1;
    if (f[a][b]!=-1) return f[a][b];
    int res=0;
    for (int i=a;i<wlen;i++){
        if (word[i]==target[b]){
            res+=doit(i+1,b+1);
        }
    }
    res%=10000;
    return f[a][b]=res;
}

int main(){
    freopen("hasil.txt","w",stdout);
    scanf("%d",&n);
    target="welcome to code jam";
    len=target.length();
    getchar();
    for (int i=0;i<n;i++){
        getline(cin,word);
        wlen=word.length();
        memset(f,-1,sizeof(f));
        ans=doit(0,0);
        printf("Case #%d: ",i+1);
        if (ans<10) printf("000");
        else if (ans<100) printf("00");
        else if (ans<1000) printf("0");
        printf("%d\n",ans);
    }
    //system("pause");
    return 0;
}
