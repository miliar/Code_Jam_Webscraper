#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
int ans[50];
int main()
{
    for(int ttt =0 ;ttt<=50;ttt++)
    ans[ttt]=-1;
    ans[22]=40265;
    ans[23]=68060;
    ans[24]=13335;
    ans[25]=84884;
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int t,one=1;
    scanf("%d",&t);
    while(t-- >0)
    {
        int n,l,pos,pos1,flag=1,count=0;
        vector <int> a;
        vector <int> b;
        long long i=0ll,j=0ll,power=0ll,k=0ll,m=0ll,max=-1,flag1=1;
        scanf("%d",&n);
        if(ans[n]!=-1)
        {
             printf("Case #%d: %d\n",one,ans[n]);
                one++;
            continue;
        }
        for(i=2;i<n;i++)
        {
            a.push_back(i);
        }
  

        power = (long long)pow(2.0,n-2);
       
        for(i=1;i<power;i++)
        {
            vector <int> b;
            for(j=0;j<n-2;j++)
            {
                if((i&(1<<j))!=0)
                {
                    if(a[j]<max)
                    {
                        flag1=0;
                        break;
                    }
                    b.push_back(a[j]);
                    if(a[j]>max)
                    max=a[j];
                }
            }
           if(flag1==0)
            {
                flag1=1;
                continue;
            }
            max=0;
            b.push_back(n);
            //for(int mm=0;mm<b.size();mm++)
            //cout<<b[mm]<<" ";
            //cout<<endl;
            
            l = b.size();
            
            pos = l;
            while(1)
            {
                
                for(m=0;m<l;m++)
                {
                    if(b[m]==pos)
                    break;
                }
                if(m == l)
                {
                    break;
                    flag = 0;
                }
                if(m==0)
                {
                    flag = 1;
                    break;
                }
                pos = m+1;
            }
            if(flag == 1)
            count=(count+1)%100003;
            flag=0;
        }
        count = (count+1)%100003;
        printf("Case #%d: %d\n",one,count);
        ans[n]=count;
        one++;
        //cout<<"Case #"<<one++<<": "<<count+1<<endl;
        count=0;
    }
    return 0;
}
                   
                   
