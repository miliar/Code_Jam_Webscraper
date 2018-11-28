#include<iostream>
using namespace std;

const int maxn=40;

int len[maxn];
int n,fr;
bool used[maxn];
int p[maxn];

void init(){
    int i,j,bg;
    char ch;
    cin>>n;
    cin.get();
    for (i=0;i<n;++i){
        bg=0;
        for (j=0;j<n;++j){
            cin.get(ch);
            if (ch=='1') bg=j;
        }
        len[i]=bg;
        cin.get();
    }
}

void refresh(){
    int i,j,res=0;
    for (i=n-1;i>=0;--i){
        for (j=i+1;j<n;++j) if (p[i]>p[j]) ++res;
    }
    if (res<fr) fr=res;
}

void work(int step){
    if (step==n){
        refresh();
        return;
    }
    for (int i=0;i<n;++i) if (!used[i]&&len[i]<=step){
        used[i]=true;
        p[i]=step;
        work(step+1);
        used[i]=false;
    }
}

int main(){
    int N,I,i;
    cin>>N;
    for (I=1;I<=N;++I){
        cout<<"Case #"<<I<<": ";
        init();
        for (i=0;i<n;++i) used[i]=false;
        fr=2000;
        work(0);
        cout<<fr<<endl;
    }
    return 0;
}
