#include <iostream>

using namespace std;

int main()
{
    int t;
    char w;
    char ca;
    int cont;
    bool win;
    bool comp;
    cin>>t;
    char ch[4][5];

    for (int i=0; i<t; i++)
    {

        cin>>ch[0];
        cin>>ch[1];
        cin>>ch[2];
        cin>>ch[3];
        win=false;


///////////////////////====>

        for (int j=0; j<4; j++)
        {
            if (win)
                break;
            cont=0;
            w=ch[j][0];
            if (w=='T')
                w=ch[j][1];
            if (w=='.')
                continue;
            for (int k=0; k<4; k++)
                if ((ch[j][k]==w)||(ch[j][k]=='T'))
                    cont++;
            if (cont==4)
            {
                win=true;
                ca=w;
                break;
            }
        }

///////////////////////////////////////////VVVVV

        for (int j=0; j<4; j++)
        {
            if (win)
                break;
            cont=0;
            w=ch[0][j];
            if (w=='T')
                w=ch[j][1];
            if (w=='.')
                continue;
            for (int k=0; k<4; k++)
                if ((ch[k][j]==w)||(ch[k][j]=='T'))
                    cont++;
            if (cont==4)
            {
                win=true;
                ca=w;
                break;
            }
        }

/////////////////////////////////////////////////
//test b win

        cont=0;
        w=ch[0][0];
        if (w=='T')
            w=ch[1][1];
        cont=0;
        if (w=='.')
            w=0;
        for (int j=0; j<4; j++)
            if ((ch[j][j]==w)||(ch[j][j]=='T'))
                cont++;
        if (cont==4)
        {
            win=true;
            ca=w;
        }


        //////////////////////
        cont=0;
        w=ch[3][0];
        if (w=='T')
            w=ch[2][1];
        if (w=='.')
            w=0;
        cont=0;
        for (int j=0; j<4; j++)
            if ((ch[3-j][j]==w)||(ch[3-j][j]=='T'))
                cont++;
        if (cont==4)
        {
            win=true;
            ca=w;
        }

//////////////////////
        if (!win)
        {
            comp=true;
            for (int j=0; j<4; j++)
                for (int k=0; k<4; k++)
                    if (ch[j][k]=='.')
                        comp=false;
        }
        //////////////////////////

        cout<<"Case #"<<i+1<<": ";
        if (win)
            cout<<ca<<" won"<<endl;
        else if (comp)
            cout<<"Draw"<<endl;
        else
            cout<<"Game has not completed"<<endl;

    }

    return 0;
}
