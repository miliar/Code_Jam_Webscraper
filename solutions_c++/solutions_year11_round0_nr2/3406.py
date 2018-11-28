#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
    int t,c,d,n;

    char base[] = "QWERASDF";

    char comb[36][3];
    char opp[28][2];
    char que[100];
    char out[100];
    bool combined = false;
    int idx=0;

    ifstream inputReader(argv[1]);
    inputReader>>t;

    for (int i =0;i<t;i++)
    {
        idx=0;
        combined =false;

        inputReader>>c;

        for(int k=0;k<c;k++)
        {
            string combs;
            inputReader>>combs;

            for(int m=0;m<3;m++)
            {
                comb[k][m] = combs[m];
            }
        }

        inputReader>>d;
        for(int k=0;k<d;k++)
        {
            string opps;
            inputReader>>opps;

            for(int m=0;m<2;m++)
            {
                opp[k][m] = opps[m];
            }
        }

        inputReader>>n;
        string queue;
        inputReader>>queue;

        for(int k=0;k<n;k++)
        {
            que[k] = queue[k];
        }

        for(int k=0;k<n;k++)
        {
            if(k==0)
            {
                out[idx++] = que[k];
                continue;
            }

            if(c==0)
            {
                combined = false;
            }
            else
            {
                for(int j=0;j<c;j++)
                {
                    if((out[idx-1]==comb[j][0] && que[k]==comb[j][1]) || (out[idx-1]==comb[j][1] && que[k]==comb[j][0]))
                    {
                        out[idx-1] = comb[j][2];
                        combined=true;
                        break;
                    }
                    else
                    {
                        combined = false;
                    }
                }
            }

            if(!combined)
            {
                out[idx++] = que[k];
                for(int m=0;m<idx;m++)
                {
                    for(int j=0;j<d;j++)
                    {
                        if(opp[j][0]==out[m])
                        {
                            if(opp[j][1]==que[k])
                                idx=0;
                        }
                        else if(opp[j][1]==out[m])
                        {
                            if(opp[j][0]==que[k])
                                idx=0;
                        }
                    }
                }
            }
            combined = false;
        }

        cout<<"Case #"<<(i+1)<<": [";

        for(int g=0;g<idx;g++)
        {
            if(g<idx-1)
                cout<<out[g]<<", ";
            else
                cout<<out[g];
        }
        cout<<"]"<<endl;
    }
    return 0;
}
