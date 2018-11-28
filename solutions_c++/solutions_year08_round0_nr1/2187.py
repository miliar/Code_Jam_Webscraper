#include<iostream>
#include<sstream>
#include<string>


using namespace std;

int f[100];

int change(int m)
{
    int i;
    for(i=0;i<m;i++)
        if(f[i]==0)
            return 0;
    return 1;
}

int main()
{
    freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
    int n;
    int no=1;
    cin>>n;
    int x=n;
    while(n--)
    {
              int i;
              for(i=0;i<100;i++)
                  f[i]=0;
              int m;
              cin>>m;
              string vs[100];
              string s;
              getline(cin,s);
              for(i=0;i<m;i++)
              {
                  getline(cin,s);
                  vs[i]=s;
                  }
              int q;
              cin>>q;
              int ret=0;
              string ss;
              getline(cin,ss);
              while(q--)
              {
                        getline(cin,ss);
                        int p;
                        for(p=0;p<m;p++)
                            if(vs[p]==ss)
                            {
                                f[p]=1;
                                break;
                                }
                        if(change(m))
                        {
                            ret++;
                            for(int j=0;j<100;j++)
                                f[j]=0;
                            f[p]=1;
                                }
                                }
                                cout<<"Case #"<<no++<<": "<<ret<<endl;
}
}
                                
                        
                        
                        
                  

