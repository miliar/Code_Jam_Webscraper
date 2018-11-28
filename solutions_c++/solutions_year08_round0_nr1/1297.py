#include <iostream>
using namespace std;

int N,S,Q;
int times,cnt;
int i,j,k,t;

string Search[101],key[1001];
int appear[101];
char s[100];

int main(){
    cin>>N;
    for(times=1;times<=N;times++){
        cin>>S;
        cin.getline(s,sizeof s,'\n');
        for(i=0;i<S;i++){
            cin.getline(s,sizeof s,'\n');
            Search[i] = s;
        }
        cin>>Q;
        cin.getline(s,sizeof s,'\n');
        for(i=0;i<Q;i++){
            cin.getline(s,sizeof s,'\n');
            key[i] = s;
        }
        cnt = -1;
        for(i=0;i<Q;){
            for(j=0;j<S;j++){
                for(k=i;k<Q;k++) if(key[k] == Search[j]) break;
                appear[j] = k;
            }
            for(t=j=0;j<S;j++) if(appear[j] > appear[t]) t=j;
            ++cnt;
            i = appear[t];
        }
        cout<<"Case #"<<times<<": "<<(cnt<0?0:cnt)<<endl;

    }
//    system("pause");
    return 0;
}
