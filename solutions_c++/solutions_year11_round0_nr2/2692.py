#include <iostream>
using namespace std;

int t;
int c,d,n;
char com[36][4];
char opp[28][3];
char in[101],out[101];
int main()
{
    int casen;
    cin>>t;
    for (casen=1; casen<=t; casen++)
    {
        cin>>c;
        for (int i=0; i<c; i++)
            cin>>com[i];
        cin>>d;
        for (int i=0; i<d; i++)
            cin>>opp[i];
        cin>>n>>in;
        //cout<<in<<com[0]<<opp[0];
        out[0]=in[0];
        int p=1,q=0;
        while (p<n)
        {
            bool flag=false;
            for (int i=0; i<c; i++)
            {
                if (in[p]==com[i][0] && out[q]==com[i][1] || in[p]==com[i][1] && out[q]==com[i][0])
                {
                    out[q]=com[i][2];
                    p++;
                    flag=true;
                }
                if (flag) break;
            }
            if (flag) continue;
            flag=false;
            for (int i=0; i<d; i++)
            {
                if (in[p]==opp[i][0])
                {
                    for (int j=0; j<=q; j++)
                        if (out[j]==opp[i][1])
                        {
                            q=0;
                            if (p<n-1) 
                            {
                                p++;
                                out[q]=in[p];
                            }
                            else q=-1;
                            p++;
                            flag=true;
                        }
                    if (flag) break;
                }
                if (flag) break;
                if (in[p]==opp[i][1])
                {
                    for (int j=0; j<=q; j++)
                        if (out[j]==opp[i][0])
                        {
                            q=0;
                            if (p<n-1) 
                            {
                                p++;
                                out[q]=in[p];
                            }
                            else q=-1;
                            p++;
                            flag=true;
                        }
                    if (flag) break;
                }
                if (flag) break;
            }
            if (flag) continue;
            q++;
            out[q]=in[p];
            p++;
        }
        cout<<"Case #"<<casen<<": [";
        for (int i=0; i<=q-1; i++)
            cout<<out[i]<<", ";
        cout<<out[q]<<"]"<<endl;
    }
    return 0;
}

