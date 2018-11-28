#include<iostream>
#include<fstream>
using namespace std;


long oran[104][3]={0};
long blue[104][3]={0};
char color;
long total, n, button;
long main()
{
   
    ifstream fin("input.in");
    ofstream fout("output.out");
    fin >> total;
    for(long i=1; i<=total; i++)
    {
        fin >> n;
        long ora_cnt = 0;
        long blu_cnt = 0;
        long cnt = 0;
        for(long j=0; j!=n; j++)
        {
            fin >> color >> button;
            if(color=='O')
            {
                oran[ora_cnt][0] = button;
                oran[ora_cnt++][1] = cnt++;
            }
            if(color=='B')
            {
                blue[blu_cnt][0] = button;
                blue[blu_cnt++][1] = cnt++;
            }

        }
        long oraPos=1;
        long bluPos=1;
        long oraCur=0;
        long bluCur=0;
        long pressed=0;
        long res=0;
        while(pressed!=cnt)
        {
            long target;
            long times;
            if(oraCur<ora_cnt && oran[oraCur][1]==pressed)
            {
                target = oran[oraCur++][0];
                times=abs(target-oraPos)+1;
                res+=times;
                pressed++;
                oraPos = target;
                for(long j=0; j<times; j++)
                { 
                    if(bluPos<blue[bluCur][0])
                        bluPos++;
                    if(bluPos==blue[bluCur][0])
                        break;
                    if(bluPos>blue[bluCur][0])
                        bluPos--;
                }
            }
            if(bluCur<blu_cnt &&blue[bluCur][1]==pressed)
            {
                target = blue[bluCur++][0];
                times=abs(target-bluPos)+1;
                res+=abs(target-bluPos)+1;

                bluPos = target;
                ++pressed;
                for(long j=0; j!=times; j++)
                {
                    if(oran[oraCur][0]>oraPos)
                        oraPos++;
                    if(oran[oraCur][0]==oraPos)
                        break;
                    if(oran[oraCur][0]<oraPos)
                        oraPos--;
                }
            }
        }
        fout<< "Case #"<< i << ": " << res << endl;
    }
    fin.close();
    fout.close();
}