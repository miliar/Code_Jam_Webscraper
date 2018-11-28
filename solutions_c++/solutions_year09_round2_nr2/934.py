#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <cmath>
#include <string>
#include <vector>

using namespace std;



typedef long long ll;//NOTES:int64
typedef unsigned long long ull;//NOTES:uint64

int main()
{
    // input output streams
    freopen ("B-large.in", "r", stdin);
    freopen ("output.txt", "w", stdout);


    // number of cases
    int N;
    scanf ("%d", &N);
    if (N < 1)
        printf ("Error: input file not found\n");

    // for each case
    for (int caseId=1; caseId<=N; caseId++)
    {
        char chS[25];
        scanf("%s", &chS);

        string s;
        s=chS;


        //digits
        vector<int> d(25);
        int last=s.length();
        for(int i=0; i<last; i++) {
            string s2 = s.substr(i,1);
            d[i] = atoi(s2.c_str());
            //printf ("%d", d[i]);


        }
        //printf("%d\n", last);

        int ptr=last-2;
        int prev=10;//INF
        // find last decreasing seq
        while(true)
        {
            if(d[ptr] >= d[ptr+1])
            {
                ptr--;
            }
            else
            {
                break;
            }
        }

        // if entire seq decreasing..
        if(ptr<0)
        {
            sort(d.begin(), d.begin()+last);
            for(int i=last; i>0; i--)
            {
                d[i]=d[i-1];
            }
            d[1]=0;
            last+=1;

            // if start with 0
            int zptr=0;
            while (true)
            {
                if(d[zptr]>0) break;
                zptr++;
            }
            if(zptr > 0)
            {
                d[0]=d[zptr];
                d[zptr] = 0;
            }
        }
        else{


        int comptr = ptr;
        int com = d[comptr];
        //printf ("t %d\n", com);
        //return 0;
        int min = 10;
        int minptr=-1;
        // find lowest num bigger than com to swap
        for(int i=ptr+1; i<last; i++)
        {
            if(d[i] > com)
            {
                //printf("%d \n", d[i]);
                if(d[i] < min)
                {min = d[i];
                minptr = i;
                }
            }
        }
        //return 0;
        assert(minptr>=0);
//printf("%d %d\n", comptr, last-1);
        // swap
        int temp = d[comptr];
        d[comptr] = d[minptr];
        d[minptr] = temp;

        // put seq increasing order
        sort(d.begin()+comptr+1, d.begin()+last);
        }

        //output
        printf("Case #%d: ", caseId);
        for(int i=0; i<last; i++)
        {
            printf("%d", d[i]);
        }
        printf("\n");
    }

    return 0;
}

