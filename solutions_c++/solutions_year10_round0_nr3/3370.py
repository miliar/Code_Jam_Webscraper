#include<iostream>
#include<queue>
using namespace std;
int save[20];
main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,T,j, r,n, k, p,pas, num, cnt, t;
    queue<int> q;
    cin>>T;
    for(t=1;t<=T;t++){
        scanf("%d%d%d", &r, &k, &n);
        q=queue<int>();
        int ans=0;
        for(i=0;i<n;i++){
            scanf("%d", &p);
            q.push(p);

        }
        for(i=0;i<r;i++){
            pas=0;
            cnt=0;
            while(q.size()>0 && pas+q.front()<=k){
                num = q.front();
                pas+=num;
                save[cnt++]=num;
                q.pop();
            }
            ans+=pas;
            for(j=0;j<cnt;j++){
                q.push(save[j]);
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }

}
