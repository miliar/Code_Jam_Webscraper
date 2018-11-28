#include<iostream>

using namespace std;

int main()
{
  int T=0, N=0, SURP=0, p=0, *ti, MAX=0, a=0;
  cin>>T;
  for(int k=1;k<=T;k++)
  {
    MAX=0,a=0;
    cin>>N>>SURP>>p;
    ti = new int[N];
    for(int i=0;i<N;i++)
    {
        cin>>ti[i];
        a = ti[i];
        if( a>=p && a>=3*p-2 )
        {
            MAX++;
        }
        else if( a>=p && (a>=3*p-4 && SURP!=0) )
        {
            MAX++;
            SURP--;
        }
    }
    cout<<"Case #"<<k<<": "<<MAX<<"\n";
  }
  return 0;
}
