#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Q1out.txt","w",stdout);
    int i,t,j,found;
    char game[4][4];
    string str,X[5],O[5],result;
    bool flag,isgamecomplete;
    cin>>t;
    for(int k=1;k<=t;++k)
    {
        found=-1;
        isgamecomplete=true;
        flag=true;
        for(i=0;i<4;++i)
        {
            cin>>str;
            game[i][0]=str.at(0);
            game[i][1]=str.at(1);
            game[i][2]=str.at(2);
            game[i][3]=str.at(3);
            found = str.find(".");
            if(found!=-1)
                isgamecomplete=false;
        }
        /*for(i=0;i<4;++i)
        {
            for(j=0;j<4;++j)
                cout<<game[i][j];
            cout<<endl;
        }*/
        for(i=0;i<4 && flag;++i)
        {
            str.erase();
            for(j=0;j<4;++j)
            {
                str+=game[i][j];
            }
            //cout<<str<<endl;
            X[0]="XXXX";
            X[1]="TXXX";
            X[2]="XTXX";
            X[3]="XXTX";
            X[4]="XXXT";
            O[0]="OOOO";
            O[1]="TOOO";
            O[2]="OTOO";
            O[3]="OOTO";
            O[4]="OOOT";
            for(j=0;j<5;++j)
            {
                if(str.compare(X[j])==0)
                {
                    flag=false;
                    result="X won";
                }
                if(str.compare(O[j])==0)
                {
                    flag=false;
                    result="O won";
                }
            }
        }
        for(i=0;i<4 && flag;++i)
        {
            str.erase();
            for(j=0;j<4;++j)
            {
                str+=game[j][i];
            }
            //cout<<str<<endl;
            X[0]="XXXX";
            X[1]="TXXX";
            X[2]="XTXX";
            X[3]="XXTX";
            X[4]="XXXT";
            O[0]="OOOO";
            O[1]="TOOO";
            O[2]="OTOO";
            O[3]="OOTO";
            O[4]="OOOT";
            for(j=0;j<5;++j)
            {
                if(str.compare(X[j])==0)
                {
                    flag=false;
                    result="X won";
                }
                if(str.compare(O[j])==0)
                {
                    flag=false;
                    result="O won";
                }
            }
        }
        for(i=0;i<1 && flag;++i)
        {
            str.erase();
            for(j=0;j<4;++j)
            {
                str+=game[j][j];
            }
            //cout<<str<<endl;
            X[0]="XXXX";
            X[1]="TXXX";
            X[2]="XTXX";
            X[3]="XXTX";
            X[4]="XXXT";
            O[0]="OOOO";
            O[1]="TOOO";
            O[2]="OTOO";
            O[3]="OOTO";
            O[4]="OOOT";
            for(j=0;j<5;++j)
            {
                if(str.compare(X[j])==0)
                {
                    flag=false;
                    result="X won";
                }
                if(str.compare(O[j])==0)
                {
                    flag=false;
                    result="O won";
                }
            }
        }
        for(i=0;i<1 && flag;++i)
        {
            str.erase();
            for(j=0;j<4;++j)
            {
                str+=game[j][3-j];
            }
            //cout<<str<<endl;
            X[0]="XXXX";
            X[1]="TXXX";
            X[2]="XTXX";
            X[3]="XXTX";
            X[4]="XXXT";
            O[0]="OOOO";
            O[1]="TOOO";
            O[2]="OTOO";
            O[3]="OOTO";
            O[4]="OOOT";
            for(j=0;j<5;++j)
            {
                if(str.compare(X[j])==0)
                {
                    flag=false;
                    result="X won";
                }
                if(str.compare(O[j])==0)
                {
                    flag=false;
                    result="O won";
                }
            }
        }
        if(flag)
        {
            if(isgamecomplete)
                cout<<"Case #"<<k<<": Draw"<<endl;
            else
                cout<<"Case #"<<k<<": Game has not completed"<<endl;
        }
        else
        {
            cout<<"Case #"<<k<<": "<<result<<endl;
        }
    }
    return 0;
}
