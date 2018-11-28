#include <iostream>
using namespace std;
void work(int t) {
    cout<<"Case #"<<t<<":"<<endl;
    int n,m;
    cin>>n>>m;
    char *temp  =   new char[2];
    char **s =   new char*[n];
    cin.getline(temp,2);
    for(int i=0;i<n;i++) {
        s[i]=new char[m];
        cin.getline(s[i],m+2);
    }
    int flag=1;
    for(int i=0;i<n-1;i++) {
        for(int j=0;j<m-1;j++)
        {
            if(s[i][j]=='#')
            {
                if(s[i][j+1]!='#' || s[i+1][j]!='#' || s[i+1][j]!='#')
                {
                    flag=0;
                    i=n;
                    j=m;
                }
                else{
                    s[i][j]     =s[i+1][j+1]    ='/';
                    s[i][j+1]   =s[i+1][j]      ='\\';
                }
            }
        }
    }
    if(flag==1)
    {
        for(int i=0;i<n;i++)
            if(s[i][m-1]=='#')
                {flag=0; break;}
        if(flag==1){
        for(int i=0;i<m;i++)
            if(s[n-1][i]=='#')
            {   flag=0;break;}
        }      
    }
    if(flag==1)
    {
        for(int i=0;i<n;i++)
            cout<<s[i]<<endl;
    }
    else
        cout<<"Impossible"<<endl;
}
int main() {
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
        work(i+1);
    return 0;
}
