#include <iostream>
#include <string>
using namespace std;


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t1,t,n,i,j,k;
    cin >> t;
    bool col[100];
    int pos[100];
    int time;
    int task1,task2,curtask,pos1,pos2;
    bool flag=0;
    bool act1,act2;
    char c;
    for(t1=0;t1<t;t1++)
    {
        cin >> n;
        for(i=0;i<n;i++)
        {
            cin >> c;
            cin >> pos[i];
            col[i]=(c=='O');
        }
        task1=0;
        task2=0;
        act1=1;
        act2=1;
        while(task2<n && col[task2]){task2++;}
        while(task1<n && (!col[task1])){task1++;}
        
        if(task2==n){act2=0;}
        if(task1==n){act1=0;}
        
        pos1=1;
        pos2=1;
        curtask=0;
        time=0;
        while(curtask<n)
        {
            flag=1;
            if(act1)
            {
                if(pos1!=pos[task1])
                {
                    if(pos1<pos[task1]){pos1++;} else {pos1--;}
                } else
                {
                    if(task1==curtask)
                    {
                        curtask++;flag=0;
                        task1++;
                        while(task1<n && (!col[task1])){task1++;}
                        if(task1==n){act1=0;}
                    }
                }
            }
            
            if(act2)
            {
                if(pos2!=pos[task2])
                {
                    if(pos2<pos[task2]){pos2++;} else {pos2--;}
                } else
                {
                    if(flag && task2==curtask)
                    {
                        task2++;
                        while(task2<n && col[task2]){task2++;}
                        if(task2==n){act2=0;}
                        curtask++;
                    }
                }
            }
            time++;
        }
        cout << "Case #" << t1+1 << ": "<< time << "\n";
    }
    return 0;
}
