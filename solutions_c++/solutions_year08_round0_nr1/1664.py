#include <iostream>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

void solve(int tc)
{
  map<string,int> names;
  int A[2][110];

  int E,Q;
  scanf("%d ",&E);

  for(int i=0;i<E;i++)
  {
    string s;
    getline(cin,s);
    names[s]=i;
  }
  for(int i=0;i<E;i++)A[1][i]=0;

  scanf("%d ",&Q);
  int t=0;
  for(int i=0;i<Q;i++,t=1-t)
  {
    string s; getline(cin,s);
    int e=names[s];

    int m=A[1-t][0]; for(int j=0;j<E;j++)if(A[1-t][j]<m)m=A[1-t][j];

    for(int j=0;j<E;j++)
    {
      int a=A[1-t][j];
      int b=m+1;
      A[t][j]=(a<b)?a:b;
    }

    A[t][e]=Q+117;
  }

  int M=Q+117;
  for(int i=0;i<E;i++)if(A[1-t][i]<M)M=A[1-t][i];

  cout<<"Case #"<<tc<<": "<<M<<"\n";
}

int main()
{
  int N; cin>>N;
  for(int i=0;i<N;i++)solve(i+1);
}
