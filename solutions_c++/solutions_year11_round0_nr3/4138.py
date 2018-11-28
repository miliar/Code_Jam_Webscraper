# include <iostream>
using namespace std;
int main()
{
  int x,b,c,d,i,j,k,n,t;
  int min;
  cin>>t;
  j=0;
  while(t--)
  {
    //x=0;
    j++;
    cin>>b;
    cin>>min;
    x=min;
    d=min;
    for(i=1;i<b;i++)
    {
      cin>>c;
      d+=c;
      if(c<min)
      min=c;
      x=x^c;
    }
    //cout<<"min=="<<min
    if(x==0)
    cout<<"Case #"<<j<<": "<<d-min<<"\n";
    else
    cout<<"Case #"<<j<<": NO\n";
  }
  
  return 0;
}
