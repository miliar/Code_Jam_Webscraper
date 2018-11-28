#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<cstdio>
#include<cstring>
using namespace std;
#define N 30
int n_case;
string str;
int mark[N][N];
vector <int> opp[N];
char res[103];
int check(int t);
int k;
int main()
{
    ofstream cout("out.txt");
    freopen("in.txt","r",stdin);
    int n_combine;
    int n_oppose;
    cin>>n_case;
    for(int t=0;t<n_case;t++)
    {
         for(int i=0;i<N;i++)
         opp[i].clear();
        memset(mark,-1,sizeof(mark));
        cin>>n_combine;
        for(int i=0;i<n_combine;i++)
        {
            cin>>str;
            int t1=str[0]-'A';
            int t2=str[1]-'A';
            int t3=str[2]-'A';
            mark[t1][t2]=mark[t2][t1]=t3;
        }
        cin>>n_oppose;
        for(int i=0;i<n_oppose;i++)
        {
            cin>>str;
            int t1=str[0]-'A';
            int t2=str[1]-'A';
            opp[t1].push_back(t2);
            opp[t2].push_back(t1);
        }
        int len;
         k=0;
        cin>>len;
        cin>>str;
        res[k++]=str[0];
        for(int i=1;i<len;i++)
        {
           // cout<<len<<endl;
         //   for(int n=1;n<k;n++)
            //   cout<<res[n];
           //  cout<<endl;
            if(k==0)
            {
                res[k++]=str[i];
                continue;
            }
            int t1=str[i]-'A';
            if(mark[t1][res[k-1]-'A']!=-1)
            {
               // cout<<"Yes";
                res[k-1]=mark[t1][res[k-1]-'A']+'A';
            }
            else {
                int done=0;
                for(int z=0;z<opp[t1].size();z++)
                {
                    if(check(opp[t1][z]) )
                            {
                                k=0;
                                done=1;
                            }
                }
                if(done==0)
                    res[k++]=t1+'A';

            }

        }
      //   cout<<k<<endl;
        cout<<"Case #"<<t+1<<": "<<"[" ;
         if(k!=0)
        {

            cout<<res[0];
            for(int i=1;i<k;i++)
            {
                cout<<", "<<res[i];
            }
        }
        cout<<']'<<endl;

    }
}

int check(int t)
{
    for(int i=0;i<k;i++)
    {
        if(res[i]==t+'A')
          return 1;
    }
    return 0;
}

