#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
    freopen ("in.in","r",stdin);
    freopen ("out.out","w",stdout);
    int n,c=1;
    scanf("%d\n",&n);
    string s;
    while(n-- )
    {
        vector<string> x(4,"");
        for(int i=0; i<4; cin>>x[i++]);
        string ans="";
        bool nocom =false;
        for(int i=0; i<4; i++)
        {
            nocom |= count(x[i].begin(),x[i].end(),'.');
            int tc = count(x[i].begin(),x[i].end(),'T');
            int tx = count(x[i].begin(),x[i].end(),'X');
            int to = count(x[i].begin(),x[i].end(),'O');
            //  cout<<tx<<tc<<endl;
            if((tc==1 && tx==3) || tx==4) ans="X won";
            if((tc==1 && to==3) || to==4) ans="O won";
        }
        //cout<<ans<<endl;

        for(int i=0; i<4; i++)
        {
            int tc,tx,to;
            tc=tx=to = 0;
            for(int j=0; j<4; j++)
                if(x[j][i]=='.')continue;
                else if(x[j][i]=='T')tc++;
                else if(x[j][i]=='X')tx++;
                else if(x[j][i]=='O')to++;
            if((tc && tx==3) || tx==4) ans="X won";
            if((tc && to==3) || to==4) ans="O won";
        }
        int tc,tx,to;
        tc=tx=to = 0;
        for(int i=0; i<4; i++)
        {


            if(x[i][i]=='.')continue;
            else if(x[i][i]=='T')tc++;
            else if(x[i][i]=='X')tx++;
            else if(x[i][i]=='O')to++;

        }
        if((tc && tx==3) || tx==4) ans="X won";
        if((tc && to==3) || to==4) ans="O won";
        tc=tx=to = 0;
        int j=3;
        for(int i=0; i<4; i++)
        {



            if(x[j][i]=='T')tc++;
            else if(x[j][i]=='X')tx++;
            else if(x[j][i]=='O')to++;
            j--;
        }
        if((tc && tx==3) || tx==4) ans="X won";
        if((tc && to==3) || to==4) ans="O won";
        if(nocom && ans=="")
        {
            printf("Case #%d: Game has not completed\n",c++);
            continue;
        }
        if(ans=="") printf("Case #%d: Draw\n",c++);
        else printf("Case #%d: %s\n",c++,ans.c_str());
    }
}
