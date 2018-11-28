/*
ID: kishwarshafin
PROG:
LANG: C++
*/
/*
Timus JI: 119454XP
*/
#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 2147483647
#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
bool color[1001][1001];
int main()
{
//    #ifndef ONLINE_JUDGE
//	in("in.txt");
//	out("out.txt");
//    #endif

    int t,caseno=1;
    cin>>t;
    while(t--)
    {
        printf("Case #%d: ",caseno++);
        int A,B;
        scanf("%d %d",&A,&B);
        memset(color,0,sizeof(color));
        int count=0;
        for(int i=A;i<=B;i++)
        {
            int num=i;
            int t=10;
            while(t<=1000)
            {
                int part1=num%t;
                int part2=num/t;
                if(t>num)break;
                int new_num;
                if(part2<10)
                    new_num=part1*10+part2;
                else if(part2<100)
                    new_num=part1*100+part2;
                else if(part2<1000)
                    new_num=part1*1000+part2;

                if(new_num>=A && new_num<=B && new_num!=num)
                {
                    if(color[num][new_num]==false && color[new_num][num]==false)
                    {
                        color[num][new_num]=true;
                        color[new_num][num]=true;
                        count++;
                    }
                }
                t*=10;
            }
        }
        cout<<count<<endl;
    }
	return 0;
}
