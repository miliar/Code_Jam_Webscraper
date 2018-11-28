#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
int main()
{
    fstream in("B-large.in");
    fstream out("output2.txt");
    int T,n,s,p,y=0,score;
    in>>T;
    for(int b=1; b<=T; b++)
   {
        in>>n>>s>>p;
        for(int a=0; a<n; a++)
        {
            in>>score;
            if(p==0||score==28||score==29||score==30)
            {
                y++;
            }
            else if(score-p>=fabs(2*(p-1)))
            {
                y++;
            }
            else if(s!=0)
            {
                if(score-p>=fabs(2*(p-2)))
                {
                    y++;
                    s--;
                }

            }

        }
        out<<"Case #"<<b<<": "<<y<<endl;
        y=0;
    }


}
