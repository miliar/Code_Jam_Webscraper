#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <stdio.h>
using namespace std;

#define small
//#define large

int main()
{
    #ifdef small
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small.out","w",stdout);
    #endif
    #ifdef large
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    #endif

    int i,j,t;
    scanf("%d",&t);
    map <char,int> count;

    for(i=65;i<=90;i++)
    { count[char(i)]=0;  }
    for(i=1;i<=t;i++)
    {
        int c,d,n;
        scanf("%d",&c);
        string combine[c][2];
        string temp,rtemp;
        string ans="";
        char l;
        for(j=0;j<c;j++)
        {
            cin>>temp;
            combine[j][1]=temp[2];
            combine[j][0]=temp[0];
            combine[j][0]+=temp[1];
        }
        scanf("%d",&d);
        map <char,char> oppose;
        for(j=0;j<d;j++)
        {
            cin>>temp;
            oppose[temp[0]]=temp[1];
            oppose[temp[1]]=temp[0];

        }
        scanf("%d",&n);
        bool com=false,des=false;
        for(j=0;j<n;j++)
        {
            com=false;
            des=false;
            temp="";
            rtemp="";
            cin>>l;
            if(ans.size()<1)
            { ans+=l;count[l]++; /*cout<<"ANS IS "<<ans<<endl;*/ continue; }
            else
            {
                temp+=l;
                temp+=ans[ans.size()-1];
                rtemp+=ans[ans.size()-1];
                rtemp+=l;
                for(int k=0;k<c;k++)
                {
                    //cout<<temp<<" "<<rtemp<<" "<<combine[k][0]<<" "<<combine[k][1][0]<<endl;
                    if(temp==combine[k][0])
                    {
                        count[ans[ans.size()-1]]--;
                        ans[ans.size()-1]=combine[k][1][0];
                        //count[l]--;
                        //cout<<"Replacing "<<ans[ans.size()-1]<<" and "<<l<<endl;
                        com=true;
                        break;
                    }
                    if(rtemp==combine[k][0])
                    {
                        count[ans[ans.size()-1]]--;
                        ans[ans.size()-1]=combine[k][1][0];
                        //count[l]--;
                        //cout<<"Replacing "<<ans[ans.size()-1]<<" and "<<l<<endl;
                        com=true;
                        break;
                    }
                }
                //cout<<"LOOKING FOR OPPOSE "<<oppose[l]<<endl;
                if(com==false && count[oppose[l]]>=1)
                {
                    ans=""; des=true;
                    //cout<<"OPPOSE EXISTS\n";
                    for(int k=65;k<=90;k++)
                    { count[char(k)]=0;  }
                }
                if(com==false && des==false)
                { ans+=l; count[l]++;}
            }
            //cout<<"ANS IS "<<ans<<endl;
        }
        cout<<"Case #"<<i<<": [";
        for(j=0;j<ans.size();j++)
        {
            cout<<ans[j];
            if(j<ans.size()-1)
            printf(", ");
        }
        cout<<"]"<<endl;
        for(int k=65;k<=90;k++)
        { count[char(k)]=0;  }
    }
    return 0;
}
