#include<iostream>
using namespace std;

int main()
{
    int i,j,o[101],s=1,b[101],z,ora,bl,t,n;
    char c;
    cin>>t;
    while(1)
    {
         
            if(t==0)
            break;
            
            cin>>n;
            int p=0;
            int q=0;
            for(i=0;i<n;i++)
            {
                            cin>>c;
                            cin>>o[p];
                            if(c=='O')
                            b[p]=0;
                            else
                            b[p]=1;
                            p++;
          //  cout<<o[i]<<"  "<<b[i];
            }
          //  cout<<"fly";
            int time=0;
            ora=1;
            bl=1;
            i=0;
            j=0;
            while(1)
            {
                    if(i==n)
                    {
                            break;
                    }
                    if(b[i]==0)
                    {
                               if(ora==o[i])
                               i++;
                              // cout<<"o\n";}
                               else if(ora<o[i])
                               ora++;
                               else if(ora>o[i])
                               ora--;
                               for(z=i;z<n;z++)
                               {
                                               if(b[z]==1)
                                               break;
                               }
                               if(bl<o[z])
                               bl++;
                               else if(bl>o[z])
                               bl--;
                               
                    }
                    else
                    {
                         if(bl==o[i])
                               i++;
                             //  cout<<"b\n";}
                               else if(bl<o[i])
                               bl++;
                               else if(bl>o[i])
                               bl--;
                               for(z=i;z<n;z++)
                               {
                                               if(b[z]==0)
                                               break;
                               }
                               if(ora<o[z])
                               ora++;
                               else if(ora>o[z])
                               ora--;
                    }
                    time++;
                     
            }
            cout<<"Case #"<<s<<": "<<time<<endl;   
            t--;
            s++;    
    } 
    return 0;
    }
