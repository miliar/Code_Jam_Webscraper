#include<iostream>
#include<fstream>
using namespace std;
int check(char t)
{
    if(t=='O')return 0;
    else return 1;
}
int main()
{
    fstream  fout;
    fout.open("1.txt",ios::out);
    int a[2][510],len[2];
    char robot;
    int cas,n,noa,nob;
    cin>>cas;
    int l;int i;int p,res;
    for(l=1;l<=cas;l++)
    {
                cin>>n;
                for(i=0;i<n;i++){a[0][i]=0;a[1][i]=0;}
                len[0]=0;len[1]=0;
                int data[200][2];
                int pos[2]={1,1};
                noa=0;nob=0;
                for(i=0;i<n;i++)
                {
                      cin>>robot>>data[i][1];
                      data[i][0]=check(robot);
                      a[check(robot)][len[check(robot)]++]=data[i][1];
                }
                res=0;
                for(i=0;i<n;i++)
                {
                      if(data[i][0]==0)
                      {
                           res+=int(abs(data[i][1]-pos[0]))+1;
                           
                           noa++;
                           if(pos[1]>a[1][nob])
                           {
                               pos[1]-=int(abs(data[i][1]-pos[0]))+1;
                               if(pos[1]<a[1][nob])
                                    pos[1]=a[1][nob];
                           }
                           if(pos[1]<a[1][nob])
                           {
                               pos[1]+=int(abs(data[i][1]-pos[0]))+1;
                               if(pos[1]>a[1][nob])
                                    pos[1]=a[1][nob];
                           }
                           pos[0]=data[i][1];
                      }
                      if(data[i][0]==1)
                      {
                                       
                           res+=int(abs(data[i][1]-pos[1]))+1;
                           
                           nob++;
                           if(pos[0]>a[0][noa])
                           {
                              pos[0]-=int(abs(data[i][1]-pos[1]))+1;
                               if(pos[0]<a[0][noa])
                                    pos[0]=a[0][noa];
                           }
                           if(pos[0]<a[0][noa])
                           {
                               pos[0]+=int(abs(data[i][1]-pos[1]))+1;
                               if(pos[0]>a[0][noa])
                                    pos[0]=a[0][noa];
                           }
                           pos[1]=data[i][1];
                      }
                //      cout<<res<<' '<<pos[0]<<' '<<pos[1]<<endl;
                }
               fout<<"Case #"<<l<<": "<<res<<endl;
             //  cout<<"Case #"<<l<<": "<<res<<endl;
    }
    fout.close();
   // cin>>i;
    return 0;
    
}
 
