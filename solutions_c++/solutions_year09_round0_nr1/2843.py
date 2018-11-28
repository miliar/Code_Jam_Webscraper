#include<iostream>
#include<string.h>
using namespace std;

int main()
{
    int L,D,N;
    cin>>L>>D>>N;
    char dict[D][L];
    for(int i=0;i<D;i++)
              cin>>dict[i];
    for(int i=0;i<N;i++)
    {
            bool match[5000][15]={0};
            cin.ignore();
            for(int j=0;j<L;j++)
            {
                    char ch=getchar();
                    if(ch=='(')
                    {
                                 while((ch=getchar())!=')')
                                 {
                                                           for(int k=0;k<D;k++)
                                                                   if(!match[k][j]) match[k][j]=(ch==dict[k][j]);                   
                                 }          
                    }
                    else
                    {
                        for(int k=0;k<D;k++)
                                   match[k][j]=(ch==dict[k][j]);
                    }
                    
            }
            int count=0;
            for(int p=0;p<D;p++)
            {                    
                    int flag=1;
                    for(int q=0;q<L;q++)
                            flag&=match[p][q];
                    count+=flag;
            }    
            /*for(int p=0;p<L;p++)
            {
                    for(int q=0;q<D;q++)
                            cout<<match[q][p]<<" ";
                    cout<<endl;
            } */ 
            cout<<"Case #"<<(i+1)<<": "<<count<<endl;        
    }        
    return 0;    
}
