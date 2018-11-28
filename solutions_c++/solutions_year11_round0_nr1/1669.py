#include<iostream>
#include<math.h>
#include<string.h>
using namespace std;


int main()
{
    freopen("C:\\Users\\Administrator\\Downloads\\A-large.in", "r", stdin);
    freopen("C:\\Users\\Administrator\\Downloads\\out", "w", stdout);
    int N;
    cin>>N;
    int j;
    for(j=0;j<N;j++)
    {
        int n;
        cin>>n;
        int i;
        int pos[2]= {1,1},time[2]={0,0},ans=0;
        int pre;
        char tmp;
        int who;
        int where;
        for(i=0;i<n;i++)
        {
            cin>>tmp>>where;
            if(tmp=='O')
                who = 0;
            else who = 1;
            if(i==0)
            {
                pre = who;
                time[(who+1)%2] += abs(where-pos[who])+1;
                ans += abs(where-pos[who])+1;
                pos[who] = where;
                continue;
            }
            if(pre != who)
            {
                   time[pre] = 0;
                   pre = who;
            
                 if(time[who] >= abs(where-pos[who]))
                 {
                    time[who] -= abs(where-pos[who]);
                    time[who] = 0;
                    time[(who+1)%2]++;
                    ans += 1;
                 }
                 else
                 {
                     time[(who+1)%2] += abs(where-pos[who])+1-time[who];
                     ans += abs(where-pos[who])+1-time[who];
                     time[who] = 0;
                 }
            }
            else 
            {
                 time[who] = 0;
                 time[(who+1)%2] += abs(where-pos[who])+1;
                 ans += abs(where-pos[who])+1;
            }
            pos[who] = where;
        }
        cout << "Case #" << j+1 <<": "<<ans << endl;
    }
    return 0;
}
