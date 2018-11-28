#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

string s;
int cnt;
int point_o;
int point_b;
int po;
int pb;
int o_button[105];
int b_button[105];
char char_order[210];
int order[210];
int ocnt;
int bcnt;
char c;
int pos;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int cc = 1;
    while(t--)
    {
        memset(o_button,-1,sizeof(o_button));
        memset(b_button,-1,sizeof(b_button));
        po =1;
        pb =1;
        ocnt= bcnt =0;
        point_o = point_b = 0;
        cin>>cnt;
        for(int i = 0;i<cnt;i++)
        {
            cin>>c>>pos;
            if(c=='O')
            {
                o_button[ocnt++] = pos;
                order[i] = pos;
                char_order[i] = 'O';
            }
            else
            {
                b_button[bcnt++] = pos;
                order[i] = pos;
                char_order[i] = 'B';
            }
        }
        int ti = 0;
        int temp = 0;
        while(temp<cnt)
        {
            //cout<<po<<' '<<pb<<endl;
            ti++;
            bool flag = true;
            if(point_o< ocnt && char_order[temp] == 'O' && po == order[temp])
            {
                //cout<<ti<<endl;
                point_o++;
                temp++;
                //continue;
                flag = false;
            }
            else if(point_o < ocnt && o_button[point_o] < po)
            {
                po--;
            }
            else if(point_o < ocnt && o_button[point_o] > po)
            {
                po++;
            }
            if(flag && point_b < bcnt && char_order[temp] == 'B' && pb == order[temp])
            {
                //cout<<ti<<endl;
                point_b++;
                temp++;
                //continue;
            }
            else if(point_b < bcnt && b_button[point_b] < pb)
            {
                pb--;
            }
            else if(point_b < bcnt && b_button[point_b] > pb)
            {
                pb++;
            }
        }
        cout<<"Case #"<<cc++<<": "<<ti<<endl;
    }
    return 0;
}
