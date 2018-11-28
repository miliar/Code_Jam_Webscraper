#include<iostream>
using namespace std;
int main()
{
    int T, N;
    int num[1000];
    bool visit[1000];
    int i,j;
    int result, temp, gnum;
    freopen("D-large.in", "r", stdin);
    freopen("out", "w", stdout);
    cin>>T;
    result;
    for(i = 1; i <= T; i++){
          cin>>N;
          result = 0;
          for(j = 0; j < N; j++){
                cin>>num[j];
                visit[j] = false;
          }
          for(j = 0; j < N; j++){
                if(visit[num[j]-1] == true){
                            continue;
                            }
                gnum = 1;
                temp = num[num[j]-1];
                visit[j] = true;
                while(temp != num[j]){
                           gnum++;
                           visit[temp-1] = true;
                           temp = num[temp-1];
                }
                if(gnum != 1)
                                result += gnum;
          }
          cout<<"Case #"<<i<<": "<<result<<".000000"<<endl;
    }
    return 0;
}
