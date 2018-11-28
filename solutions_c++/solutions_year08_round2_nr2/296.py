#include <iostream>
using namespace std;

struct set{
    bool p[169];
}s[1000];
int ps[169];

bool prime(int x){
    for(int i=2;i*i<=x;i++) if(x%i==0) return false;
    return true;
}

int T,times;
int cnt=0,i,j;
int N,A,B,P;
int small;
bool check;

bool merge(set a,set b){
    for(int i=small;i<169;i++) if(a.p[i]==1&&b.p[i]==1) return true;
    return false;
}
void domerge(int x,int y){
    for(int i=0;i<169;i++) if(s[y].p[i]==1) s[x].p[i]=1;
    s[y] = s[--N];
}

int main(){
    for(i=2;i<=1009;i++)
        if(prime(i)){
            ps[cnt++] = i;
        }
    cin>>T;
    for(times=1;times<=T;times++){
        cin>>A>>B>>P;
        memset(s,0,sizeof s);
        for(small = 0;ps[small]<P;small++);
        N = B-A+1;
        for(i=0;i+A<=B;i++){
            for(j=small;j<169;j++) if((i+A)%ps[j]==0) s[i].p[j] = true;
        }
        check = false;
        while(1){
            for(i=0;i<N;i++) for(j=i+1;j<N;j++){
                if(merge(s[i],s[j])){ domerge(i,j); check=true; }
            }

            if(!check) break;
            check=false;
        }
        cout<<"Case #"<<times<<": "<<N<<endl;
    }
    return 0;
}
