#include <iostream>
using namespace std;
typedef long long val;
int main()
{
    freopen("test.txt","r",stdin);
      freopen("test.out","w",stdout);
    int T; scanf("%d",&T);
    for(int times = 1; times<=T;++times){
        int R,k,N; scanf("%d%d%d",&R,&k,&N);
        int groups[2002];
        for(int i = 0; i < N; ++i)
        {
            cin>>groups[i];
            groups[i+N] = groups[i];
        }
        int totalEarnings[1002];
        int nextVal[1002];
        int curTotal=0;
        for(int i = 0,j=0; i < N;++i){
            while(j < i + N && curTotal + groups[j] <= k)curTotal+=groups[j++];
            totalEarnings[i] = curTotal;
            nextVal[i] = j%N;
            curTotal -= groups[i];
        }
        long long totals[1010]={0};
        int lastTimes[1010];
        //speed up below part
        long long cycleTotal = 0,total=0;
        for(int t = 0, curI = 0; t < R; ++t){

            total += totalEarnings[curI];
            if(totals[curI] > 0){
                int cyclesLeft = (R-t-1)/(t-lastTimes[curI]);
                if(cyclesLeft > 0){
                    R-=(t-lastTimes[curI])*cyclesLeft;
                    cycleTotal += (total-totals[curI]) * cyclesLeft;

                }
            }

            lastTimes[curI] = t;
            totals[curI] = total;
            curI = nextVal[curI];

        }
        total += cycleTotal;
        cout<<"Case #"<<times<<": "<<total<<endl;


    }

    return 0;
}
