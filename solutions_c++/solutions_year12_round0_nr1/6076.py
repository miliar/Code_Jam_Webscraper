using namespace std;
#include<string>
#include<vector>
#include<cstdio>
#include<iostream>
int main()
{   vector<char> A(26,' ');
    A[0]='y';  A[1]='h';  A[2]='e';
    A[3]='s';  A[4]='o';  A[5]='c';
    A[6]='v';  A[7]='x';  A[8]='d';
    A[9]='u';  A[10]='i';  A[11]='g';
    A[12]='l';  A[13]='b';  A[14]='k';
    A[15]='r';  A[16]='z';  A[17]='t';
    A[18]='n';  A[19]='w';  A[20]='j';
    A[21]='p';  A[22]='f';  A[23]='m';
    A[24]='a';  A[25]='q';
    int x,T,y; string S;
    cin>>T; getline(cin,S);
    for(x=0;x<T;x++) 
    { getline(cin,S);
      cout<<"Case #"<<x+1<<": ";
      for(y=0;y<S.length();y++)
      {  if(S[y]!=' ') cout<<A[S[y]-'a'];
         else cout<<S[y];
      }
      cout<<endl;
    }
    return 0;
}
    
           
