
#include<fstream>
#include<string>
#include<iostream>
#include<queue>
using namespace std;

ofstream outfile;
int T;
int main()
{
freopen("A-small.in","r",stdin);
outfile.open("sub.out");
cin>>T;

int res[T];
for(int i=0;i!=T;i++)
{
        queue<int> que;
        int R,K,N;
        cin>>R>>K>>N;
        int tmp;
        for(int j=0; j!=N;j++)
        {
                cin>>tmp;
                que.push(tmp);
                
        }
        res[i]=0;
        int data=0;
        
        for(int j=0;j!=R;j++)
        {
                tmp=0;
                for(int a=0;a!=N;a++)
                {
                        if(tmp+que.front()>K)
                        break;
                        tmp+=que.front();
                        que.push(que.front());
                        que.pop();
                }
                data+=tmp;
        }
        res[i]+=data;
}
for(int i=0; i!=T; i++)
{

outfile<<"Case #"<<i+1<<": "<<res[i]<<endl; 
}
outfile.close();
return 0;

}
