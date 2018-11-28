#include<iostream>
#include<fstream>
using namespace std;
int main()
{
     int t,t1,i,j,n,c;
     char a[54][54];
    ifstream fi("input.txt");
    ofstream fo("output.txt");
    fi>>t;
    for(t1=1;t1<=t;t1++)
    {
        cout<<"Case";
        fi>>n>>c;
        fo<<"Case #"<<t1<<":\n";
        for(i=0;i<n;i++)
        {
            for(j=0;j<c;j++)
            {
                fi>>a[i][j];
                a[i+1][j]='.';
                a[i][j+1]='.';
                a[i+1][j+1]='.';
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<c;j++)
            {
                if(a[i][j]=='#')
                {
                    if(a[i+1][j+1]=='#' && a[i][j+1]=='#'  && a[i+1][j]=='#')
                    {
                        a[i+1][j+1]='/' ;
                        a[i][j+1]='\\' ;
                        a[i+1][j]='\\' ;
                        a[i][j]='/' ;
                        j+=1;
                    }
                    else 
                    {
                        fo<<"Impossible\n";
                        goto t;
                    }        
                 }       
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<c;j++)
            {
                fo<<a[i][j];
            }
            fo<<'\n';
        }
        t:;
            
    }
}                        
