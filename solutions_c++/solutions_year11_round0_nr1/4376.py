#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

const int push_time = 1;

int
main()
{
    int t;
    scanf("%d",&t);
    for(int tc = 1; tc <= t; tc ++){
        int n;
        scanf("%d",&n);
        vector<pair<int,char> > a,b;
        for(int i = 0; i < n; i ++){
            char t1[2];
            int t2;
            scanf("%s %d",t1,&t2);
            a.push_back(make_pair(t2,*t1));
        }
        int otime = 0, btime = 0, oloc = 1, bloc = 1;
        for(int i = 0; i < a.size(); i ++){
            int loc = a[i].first;
            bool isblue = a[i].second == 'B';
            if(isblue){
                int dist = abs(bloc - loc);
                bloc = loc;
                btime = max(btime + dist + push_time, otime + 1);
            }else{
                int dist = abs(oloc - loc);
                oloc = loc;
                otime = max(otime + dist + push_time, btime + 1);
            }
        }
        printf("Case #%d: %d\n",tc,max(otime,btime));
    }
    return 0;
}
