#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

main()
{
    freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
    int test,N;
    cin>>N;
    for(test=0; test<N; test++)
    {
        char table[4][4];
        int x=0,o=0;
        int i,j;
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                cin>>table[i][j];
        //check
        for(i=0; i<4; i++)
        {
            char temp=table[i][0];
            if(temp=='T') temp=table[i][1];
            int count=0;
            if(temp=='X'||temp=='O')
            {
                count++;
                for(j=1; j<4; j++)
                {
                    if(table[i][j]==temp||table[i][j]=='T')
                        count++;
                }

            }
            if(count==4) {
                if(temp=='X') x=1;
                else o=1;
            }
        }

        for(i=0; i<4; i++)
        {
            char temp=table[0][i];
            if(temp=='T') temp=table[1][i];
            int count=0;
            if(temp=='X'||temp=='O')
            {
                count++;

                for(j=1; j<4; j++)
                {
                    if(table[j][i]==temp||table[j][i]=='T')
                        count++;
                }

            }
            if(count==4) {
                if(temp=='X') x=1;
                else o=1;
            }
        }

        {

            char temp=table[0][0];
            if(temp=='T') temp=table[1][1];
            int count=0;
            if(temp=='X'||temp=='O')
            {
                count++;
                for(j=1;j<4;j++)
                if(table[j][j]==temp||table[j][j]=='T') count++;

            }
            if(count==4) {
                if(temp=='X'&&temp!='.') x=1;
                else o=1;
            }
    }

            {char temp=table[0][3];
            if(temp=='T') temp=table[1][2];
            int count=0;
            if(temp=='X'||temp=='O')
            {
                count++;


                if(table[1][2]==temp||table[1][2]=='T') count++;
                if(table[2][1]==temp||table[2][1]=='T') count++;
                if(table[3][0]==temp||table[3][0]=='T') count++;

            }
            if(count==4) {
                if(temp=='X') x=1;
                else o=1;
            }
            }
if(x==1&&o==0) cout<<"Case #"<<test+1<<": "<<'X'<<" won"<<endl;
else if(x==0&&o==1) cout<<"Case #"<<test+1<<": "<<'O'<<" won"<<endl;
else if(x==0&&o==0) {
    int is=0;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            {
                if(table[i][j]=='.') {
                    is=1;
                    cout<<"Case #"<<test+1<<": "<<"Game has not completed"<<endl;
                    i=4;
                    j=4;
                }
            }
    if(!is) cout<<"Case #"<<test+1<<": "<<"Draw"<<endl;
}
else cout<<"Case #"<<test+1<<": "<<"Draw"<<endl;

;
    }
}
