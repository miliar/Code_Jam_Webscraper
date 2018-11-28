#include <iostream>
#include <cstring>
using namespace std;
char s[2000],pe[100];
int minim=1000000;
    int k;
    int len;
void scambismo(char* ko){
    int i=0;
    char pessima[2000];
    while(i<len){
        pessima[i]=s[k*(i/k) + ko[i%k]-'1'];
        i++;
    }
//    cout<<pessima<<endl;
    int cnt=1;
    for(i=1;i<len;i++){
        if(pessima[i]!=pessima[i-1]) cnt++;
    }
    if(cnt<minim)minim=cnt;
}
void permuta(char* s, int a,int b){
//    cout<<a<<' '<<b<<endl;
    if(a==(b-1)) {//cout<< s <<endl;
        scambismo(s);
    }
    else{
        permuta(s,a+1,b);
        for(int k=a+1;k<b;k++){
            s[a]^=s[k];
            s[k]^=s[a];
            s[a]^=s[k];
            permuta(s,a+1,b);
            s[a]^=s[k];
            s[k]^=s[a];
            s[a]^=s[k];
        }
    }
}
int main(){
    int n;
    cin>> n;
    for(int z=0;z<n;z++){
        minim=1000000;
        cin>>k>>s;
        len = strlen(s);
//        cout<<len<<endl;
        for(int y=0;y<k;y++)
            pe[y]='0'+y+1;
        pe[k]=0;
//        cout<<pe;
        permuta(pe,0,k);
        cout<<"Case #"<<(z+1)<<": "<<minim<<endl;
    }
}
