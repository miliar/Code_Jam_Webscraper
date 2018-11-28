#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<queue>
#include<set>
#include<map>
using namespace std;
const int INF=0x7fffffff;
const double eps=(1.0e-9);
const double PI=atan2(0.0,-1.0);

int main()
{
    freopen("B-large.in","r",stdin);
   freopen("out.txt","w",stdout);
    int cas,i,j,kk=1;
    cin>>cas;
    while(cas--)
    {
        char num[100];
        cin>>num;
        int l=strlen(num);
        int flag=0;
        string pp="";
        int from=100,to=-1,value=10000;
        for(i=1;i<l;i++)
        {
            for(j=i-1;j>=0;j--)
            {
                //if(i==3&&j==1)
                    //cout<<"++++++++++++"<<endl;
                if(num[i]>num[j])
                {
                    
                    flag=1;
                    if(j>to)
                    {
                        from=i;
                        to=j;
                        value=num[i]-'0';
                        //printf("%d   form  %d to  %d value\n",from,to,value);
                    }
                    else if(j==to)
                    {
                        //printf("i-----%d\n",i);
                        int curnow=num[i]-'0';
                        if(curnow<value)
                        {
                           // printf("value---%d\n",value);
                            value=curnow;
                            from=i;
                        }
                        else if(curnow==value)
                        {
                            if(i>from)
                            {
                                from=i;
                            }
                        }
                    }
                }
            }
        }
        if(flag==1)
        {
            i=from;
            j=to;
           // printf("from---%d  to---%d\n",from,to);
                    char tmp=num[i];
                    num[i]=num[j];
                    num[j]=tmp;
                    for(int k=0;k<=j;k++)
                    pp+=num[k];
                   // cout<<pp<<endl;
                    char p[100];
                    int q=0;
                    for(int k=j+1;k<l;k++,q++)
                    p[q]=num[k];
                    sort(&p[0],&p[q]);
                    //cout<<q<<endl;
                    for(int k=0;k<q;k++)
                    pp+=p[k];

            cout<<"Case #"<<kk<<": "<<pp<<endl;
        }
        else
        {
           int poi=-1;
            sort(&num[0],&num[l]);
            for(i=0;i<l;i++)
            if(num[i]!='0')
            {
                poi=i;
                break;
            }
            string ans="";
            ans+=num[poi];
            ans+='0';
            for(i=0;i<l;i++)
            if(i!=poi)
            ans+=num[i];
            cout<<"Case #"<<kk<<": "<<ans<<endl;
        }
        kk++;
    }
    return 0;
}
