#include<iostream>
#include<string>
using namespace std;

int searchlist(string lis[],string s, int length)
{
    int i=0;
    while(i<length)
    {
        if(s == lis[i])
        {return i;}
        i++;              
    }
    return -1;
}

void clear(bool a[],int length)
{
    for(int i=0;i<length;i++)
    {
            a[i]=false;
    }            
}

int main()
{
    int N;
    cin>>N;//cout<<"N is "<<N<<endl;
    for(int iN=0;iN<N;iN++)
    {
            int S,Q;
            cin>>S;//cout<<"S is "<<S<<endl;
            string s[S];
            bool b[S];
            getline(cin,s[0],'\n');
            for (int i=0;i<S;i++)
            {
                getline(cin,s[i],'\n');//cout<<" "<<i<<" "<<s[i]<<endl;
                b[i]= false;
            }        
            cin>>Q;//cout<<"Q is "<<Q<<endl;
            string h;
            int u,dn=0,switches=0;
            getline(cin,h,'\n');
            for(int i=0;i<Q;i++)
            {
                  getline(cin,h,'\n');
                  u = searchlist(s,h,S);
                  if(b[u]==false)
                  {
                        if(dn<S-1)
                        {dn++;b[u]=true;}
                        else
                        {clear(b,S);dn=1;switches++;b[u]=true;}         
                  }  
                  //cout<<switches<<endl;
            }
            cout<<"Case #"<<iN+1<<": "<<switches<<"\n";   
            cout.flush();                 
    }
    //system("pause");
}
