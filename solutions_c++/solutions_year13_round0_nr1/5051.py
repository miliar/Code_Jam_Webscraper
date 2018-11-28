#include<iostream>
#include<string>

using namespace std;

int main()
{
    int tstcss,nt,i,j,ca,cb;
    bool bl,cop,wina,winb;
    string mp[4];
    
    cin>>tstcss;
    nt=0;
    while (tstcss--)
    {
        nt++;
        for (i=0;i<4;i++) cin>>mp[i];
        wina=false;winb=false;cop=true;
        for (i=0;i<4;i++)
        {
            ca=0;cb=0;bl=true;
            for (j=0;j<4;j++)
            {
                if (mp[i][j]=='X') ca++;
                if (mp[i][j]=='O') cb++;
                if (mp[i][j]=='.') bl=false;
            }
            cop=cop&&bl;
            if (bl&&(cb==0))
            {
                wina=true;
                break;
            }
            if (bl&&(ca==0))
            {
                winb=true;
                break;
            }
        }
        for (i=0;i<4;i++)
        {
            ca=0;cb=0;bl=true;
            for (j=0;j<4;j++)
            {
                if (mp[j][i]=='X') ca++;
                if (mp[j][i]=='O') cb++;
                if (mp[j][i]=='.') bl=false;
            }
            cop=cop&&bl;
            if (bl&&(cb==0))
            {
                wina=true;
                break;
            }
            if (bl&&(ca==0))
            {
                winb=true;
                break;
            }
        }
        for (i=1;i>=-1;i-=2)
        {
            ca=0;cb=0;bl=true;
            for (j=0;j<4;j++)
            {
                if (mp[j][(j*i+3*(i<0))%4]=='X') ca++;
                if (mp[j][(j*i+3*(i<0))%4]=='O') cb++;
                if (mp[j][(j*i+3*(i<0))%4]=='.') bl=false;
            }
            cop=cop&&bl;
            if (bl&&(cb==0))
            {
                wina=true;
                break;
            }
            if (bl&&(ca==0))
            {
                winb=true;
                break;
            }
        }
        cout<<"Case #"<<nt<<": ";
        if (wina)
        {
            cout<<"X won"<<endl;
            continue;
        }
        if (winb)
        {
            cout<<"O won"<<endl;
            continue;
        }
        if (!cop)
        {
            cout<<"Game has not completed"<<endl;
            continue;
        }
        cout<<"Draw"<<endl;
    }
    return 0;
}
