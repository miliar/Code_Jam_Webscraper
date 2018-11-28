#include<iostream>
#include<string>
using namespace std;
char com(char A, char B, string combine[], int C){
     int i;
     for(i = 1; i <= C; i++){
           if((A == combine[i][0] && B == combine[i][1]) || (A == combine[i][1] && B == combine[i][0])){
                 return combine[i][2];
           }
     }
     return '0';
}
bool clear(char A, char B, string opposite[], int D){
     int i;
     for(i = 1; i <= D; i++){
           if((A == opposite[i][0] && B == opposite[i][1]) || (A == opposite[i][1] && B == opposite[i][0]))
                 return true;
     }
     return false;
}
int main()
{
    int T, C, D, N;
    int i, j, z, q;
    string combine[37], opposite[29], base, result;
    char temp;
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);
    cin>>T;
    for(i = 1; i <= T; i++){
            cin>>C;
            for(j = 1; j <= C; j++){
                  cin>>combine[j];
            }
            cin>>D;
            for(j = 1; j <= D; j++){
                  cin>>opposite[j];
            }
            cin>>N>>base;
            z = 0;
            for(j = 0; j < N; j++){
                  result[z] = base[j];
                  z++;
                  if(z != 0){
                       temp = com(result[z-1], result[z-2], combine, C);
                       if(temp != '0'){
                               result[z-2] = temp;
                               z--;
                               continue;
                       }
                       for(q = 0; q < z; q++){
                             if(clear(result[q], result[z-1], opposite, D)){
                                                 z = 0;
                                                 continue;
                             }
                       }
                  }
            }
            cout<<"Case #"<<i<<": [";
            for(j = 0; j < z-1; j++)
                  cout<<result[j]<<", ";
            if(z != 0)
                  cout<<result[z-1]<<"]"<<endl;
            else
                  cout<<"]"<<endl;
    }
    return 0;
}
