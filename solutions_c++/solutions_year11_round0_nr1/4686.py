#include<iostream>
using namespace std;

int main()
{
    int t,n,p,opoz,bpoz,lo,lb,zmianao,zmianab,wynik;
    char zn;
    
    cin>>t;
    for(int i=0;i<t;++i)
    {
            cin>>n;
            opoz=bpoz=1;
            wynik=0;
            zmianao=zmianab=0;
            for(int j=0;j<n;++j)
            {
                    cin>>zn>>p;
                  //  cout<<zn<<" "<<p<<endl;
                    if(zn=='O')
                    {
                               wynik+=max(abs(p-opoz)-zmianab+1,1);
                               zmianao+=max(abs(p-opoz)-zmianab+1,1);
                               opoz=p;
                               zmianab=0;
                             //  cout<<"zmiana O wynosi :"<<zmianao<<endl;
                    }
                    if(zn=='B')
                    {
                               wynik+=max(abs(p-bpoz)-zmianao+1,1);
                               zmianab+=max(abs(p-bpoz)-zmianao+1,1);
                               bpoz=p;
                               zmianao=0;
                            //   cout<<"zmiana B wynosi :"<<zmianab<<endl;
                    }
                   // cout<<"wynik:"<<wynik<<endl;
            }
            cout<<"Case #"<<i+1<<": "<<wynik<<endl;//<<endl<<endl;
            
    }
    
    
    return 0;
}
