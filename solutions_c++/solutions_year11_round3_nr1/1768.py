#include<iostream>

using namespace std;

int main()
{
    int num;
    cin>>num;
    for(int round=1;round<=num;round++)
    {
        int R,C;
        cin>>R;
        cin>>C;
        char table[R+20][C+20];
        int tableans[R+20][C+20];

        for(int i=10;i<R+10;i++)
        {
            for(int j=10;j<C+10;j++)
            {
                cin>>table[i][j];
            }
        }
        ///
        /*cout<<"----"<<endl;
        for(int i=10;i<R+10;i++)
        {
            for(int j=10;j<C+10;j++)
            {
                cout<<table[i][j];
            }
            cout<<endl;
        }*/
        //cout<<"fin"<<endl;
        int cnt=0;
        for(int i=10;i<R+10;i++)
        {
            for(int j=10;j<C+10;j++)
            {
                if(table[i][j]=='#'&&table[i][j+1]=='#'&&table[i+1][j]=='#'&&table[i+1][j+1]=='#')
                {
                    table[i][j]='/';
                    table[i][j+1]='\\';
                    table[i+1][j]='\\';
                    table[i+1][j+1]='/';
                    //cout<<"work"<<endl;

                }
                else cnt++;
            }
        }

        bool cando=true;
        for(int i=10;i<R+10&&cando;i++)
        {
            for(int j=10;j<C+10;j++)
            {
                if(table[i][j]=='#')
                {
                    cando=false;
                    break;
                }
            }
        }
        cout<<"Case #"<<round<<":"<<endl;
        if(cando)
        {
            for(int i=10;i<R+10;i++)
            {
                for(int j=10;j<C+10;j++)
                {
                    cout<<table[i][j];
                }
                cout<<endl;
            }
        }
        else
        cout<<"Impossible"<<endl;
    }
    return 0;
}
