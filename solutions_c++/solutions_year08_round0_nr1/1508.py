#include <iostream>
#include <cstdlib>
#include<vector>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
    freopen("D:/petio's/new.txt","w",stdout);
    freopen("D:/petio's/input.txt","r",stdin);
    int n;
    cin>>n;
    for(int x=0;x<n;x++)
    {
            int s;
            cin>>s;

            char names[1000][1000];
            for(int y=0;y<s;y++)
            {
                    gets(names[y]);
            }
            int q;
            cin>>q;
            char name[1000];
            int temp[1000];
            for(int i=0;i<s;i++)
               temp[i]=0;
            int used=0;
            int ans=0;
            for(int i=0;i<q;i++)
            {
                    gets(name);
                    int k;
                    for(k=0;k<s;k++)
                    {
                       if(!strcmp(name,names[k]))
                               break;
                    }
                    //cout<<k<<" "<<temp[k]<<"\n";
                    if(!temp[k])
                        if(used<s-1)
                        {
                             temp[k]=1;
                             used++;
                             //cout<<used<<"hi:)!!!!!!!!!!!!!!!!!!!!!!\n";
                        }
                        else
                        {
                            ans++;
                            for(int j=0;j<s;j++)
                                temp[j]=0;
                            used=1;
                            temp[k]=1;
                        }
                    //for(int j=0;j<s;j++)
                      //cout<<temp[j]<<" ";
                    //cout<<"\n";
            }
            cout<<"Case #"<<x+1<<": "<<ans<<"\n";
    }








      //system("PAUSE");
      return 0;
}
