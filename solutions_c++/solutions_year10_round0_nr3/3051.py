#include<iostream>
#include<queue>
using namespace std;
int main()
{
    freopen("jam.in","r",stdin);
    freopen("jam.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i=0;i<t;++i)
    {
        int r,k,n,uang=0;;
        queue<int> q,temp;
        scanf("%d %d %d",&r,&k,&n);
        for (int j=0;j<n;++j)
        {
            int x;
            scanf("%d",&x);
            q.push(x);
        }
        int total=k;
        for (int j=0;j<r;++j)
        {
            while (total>=q.front())
            {
                  total-=q.front();
                  uang+=q.front();
                  //cout << q.front()<< endl;
                  temp.push(q.front());
                  q.pop();
                  if (q.empty()) {break;}
            }
            total=k;
            //cout << endl;
            while (!temp.empty())
            {
                  q.push(temp.front());
                  temp.pop();
            }
        }
        printf("Case #%d: %d\n",i+1,uang);
    }
    return 0;
}
