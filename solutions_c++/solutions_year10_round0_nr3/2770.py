#include<iostream>
#include<queue>
#include<cstdio>
//#include<conio.h>
using namespace std;
/*void printq(queue<int> q)
{
    while(q.size()!=0)
    {   
        cout<<q.front()<<" ";
        q.pop();
    }
    cout<<endl;
}*/
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
    int t;
    cin>>t;
    int u=1;
    while(t-->0)
    {
        int y=0;
        queue<int> q;
        int r,k,n;
        cin>>r>>k>>n;
        for(int i=0;i<n;i++)
        {
            int x;
            cin>>x;
            q.push(x);
        }
        for(int i=0;i<r;i++)
        {
//            printq(q);
            int no=0;
            vector<int> f;
            while(no+q.front()<=k && q.size()!=0)
            {
                int x=q.front();
                no+=x;
                q.pop();
                f.push_back(x);
            }
            y+=no;
            for(int z=0;z<f.size();z++)
            {
                q.push(f[z]);
            }
        }
        cout<<"Case #"<<u<<": "<<y<<endl;
        u++;
    }
//    getch();
    return 0;
}
        
