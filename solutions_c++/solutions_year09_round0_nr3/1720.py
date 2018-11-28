#include<iostream>
#include<string>
#define SIZE 20
using namespace std;
int main()
{
    int table[25][510],i,j,k,N,l;
    string s;
    char str[]="maj edoc ot emoclew";
    cin>>N;getline(cin,s);
    for(k=0;k<N;k++) {
                      getline(cin,s);
                      l=s.length();l--;
                      for(i=0;i<SIZE;i++) for(j=0;j<=l;j++) table[i][j]=0;
                      if(s[l]=='m') table[0][l]=1;
                      for(j=l-1;j>=0;j--) if(s[j]=='m') table[0][j]=((table[0][j+1])%10000+1)%10000; else table[0][j]=table[0][j+1];
                      for(i=1;i<=18;i++) for(j=l-i;j>=0;j--) {
                                                              if(s[j]==str[i]) 
                                                                               table[i][j]=(table[i-1][j+1]%10000+table[i][j+1]%10000)%10000;
                                                              else
                                                                               table[i][j]=table[i][j+1];
                                         }
                      //for(i=0;i<=18;i++) {for(j=0;j<=l;j++) cout<<table[i][j]<<" ";cout<<endl;}
                      printf("Case #%d: %04d\n",k+1,table[18][0]);
                     }
    return 0;
}
