#include<iostream>
#include<vector>

using namespace std;

int main(){
  int T,t=1;
  cin>>T;
  while(T--){
    int N,pd,pg;
    cin>>N>>pd>>pg;
    int pos=1;
    if (pg==100 && pd<100)
      pos=0;
    if (pg==0 && pd>0)
      pos=0;
    if (N>=1 && pd%100 == 0)
      goto end;
    if(N>=2 && pd%50 == 0)
      goto end;
    if(N>=4 && pd%25 == 0)
      goto end;
    if(N>=5 && pd%20 == 0)
      goto end;
    if (N>=10 && pd%10 == 0)
      goto end;
    if (N>=20 && pd%5 == 0)
      goto end;
    if (N>=25 && pd%4 == 0)
      goto end;
    if (N>=50 && pd%2 == 0)
      goto end;
    if (N>=100)
      goto end;
    pos=0;
    end:
    if (pos)  
      cout<<"Case #"<<t++<<": Possible"<<endl;
    else      
      cout<<"Case #"<<t++<<": Broken"<<endl;
  }
}
      

      
