#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int T,i,l;
    char N[30];
    cin>>T;
    for(i=1;i<=T;i++) {
                       cin>>N;l=strlen(N);
                       if(next_permutation(N,N+l)) cout<<"Case #"<<i<<": "<<N<<endl;
                       else {
                             N[l]='0';
                             l++;N[l]='\0';
                             sort(N,N+l);
                             while(N[0]=='0') next_permutation(N,N+l);
                             cout<<"Case #"<<i<<": "<<N<<endl;
                            }
                      }
    return 0;
}
