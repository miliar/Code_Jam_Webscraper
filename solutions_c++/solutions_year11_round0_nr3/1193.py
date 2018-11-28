#include<iostream>
using namespace std;
int main()
{
    int T, N;
    int i,j;
    int temp;
    int num[1000];
    int min;
    freopen("C-large.in", "r", stdin);
    freopen("out", "w", stdout);
    cin>>T;
    for(i = 1; i <= T; i++){
          cout<<"Case #"<<i<<": ";
          cin>>N;
          for(j = 0; j < N; j++){
                cin>>num[j];
          }
          temp = num[0];
          for(j = 1; j < N; j++)
                temp = temp ^ num[j];
          if(temp != 0){
                  cout<<"NO"<<endl;
                  continue;
          }
          temp = 0;
          min = 999999;
          for(j = 0; j < N; j++){
                if(min > num[j])
                       min = num[j];
                temp = temp + num[j];
          }
          cout<<temp-min<<endl;
    }
    return 0;
}
