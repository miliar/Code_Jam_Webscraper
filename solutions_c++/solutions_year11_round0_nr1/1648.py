#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

struct step{
    char color;
    int num;
};

int main()
{
    int t, count, n, result;
    cin >> t;
    count=0;
    
    while (count<t)
    {
        count++;
        result = 0;
        cin >> n;
        vector<step> seq;
        vector<int> Oseq(1,1), Bseq(1,1);

        for (int i=0; i<n; i++)
        {
            char c;
            int butt;
            cin >> c >> butt;
            struct step s;
            s.color=c;  s.num=butt;
            seq.push_back(s);
            if (c=='O') Oseq.push_back(butt);
            if (c=='B') Bseq.push_back(butt);
        }

        int op=0, bp=0;
        int td=0, result=0, diff;
        for (int i=0; i<n; i++)
        {
            if (i==0 || seq[i].color==seq[i-1].color)
            {
                if (seq[i].color=='B')
                {
                    diff=abs(Bseq[bp+1]-Bseq[bp]);
                    bp++;
                }
                else
                {
                    diff=abs(Oseq[op+1]-Oseq[op]);
                    op++;
                }
                result+=diff+1;
                td+=diff+1;
            }
            else
            {
                if (seq[i].color=='B')
                {
                    diff=abs(Bseq[bp+1]-Bseq[bp]);
                    bp++;
                }
                else
                {
                    diff=abs(Oseq[op+1]-Oseq[op]);
                    op++;
                }
                if (td>=diff)
                {
                    result+=1;
                    td=1;
                }
                else
                {
                    result+=diff+1-td;                    
                    td=diff+1-td;
                }
            }
        }
        
        cout << "Case #" << count << ": " << result <<endl;
    }
    
}

