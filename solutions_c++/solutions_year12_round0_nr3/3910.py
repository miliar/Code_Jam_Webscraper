#include<iostream>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<fstream>
using namespace std;

typedef pair< int,int > pii;
map <pair < int,int>,int >mp;

int main()
{
   freopen("C-large.in","r",stdin);
   freopen("C-large.out","w",stdout);

    int test;
    int cas=1;
    //scanf("%d",&test);
    cin>>test;
    while(test--)
    {
        int A,B;
        int i,j,k,l,count1=0;
        char str[10];
        char new_str[10];
        mp.clear();

        //scanf("%d %d",&A,&B);
        cin>>A>>B;
        //cout<<A<<" "<<B<<endl;
        for(i=A;i<=B;i++)
        {
            //memset(str,0,sizeof(str));
            sprintf(str,"%d",i);
            //printf("%s\n",str);
            int len=strlen(str);

            for(j=1;j<len;j++)
            {
                k=0;
                int idx=j;
                for(int l=j;l<len;l++)
                    new_str[k++]=str[l];
                for(int l=0;l<idx;l++)
                    new_str[k++]=str[l];
                new_str[k]='\0';

                int m=atoi(new_str);
                if(m>i && m<=B)
                {
                    pii p=make_pair(i,m);
                    if(mp.find(p)==mp.end())
                    {
                    mp[p]=i;
                    count1++;
                    //cout<<count1<<"  "<<i<<","<<m<<endl;
                    }
                }
            }
        }
        //printf("Case #%d: %d\n",cas,count1);
        cout<<"Case #"<<cas<<": "<<count1<<endl;
        cas++;
    }
    return 0;
}
