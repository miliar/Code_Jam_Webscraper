#include <iostream>

using namespace std;

int main()
{
    int c;
    cin>>c;

    for(int k = 1; k <= c; k++)
    {
        bool flag = false;
        string mat[5];
        for(int i = 0; i < 4; i++)
                cin>>mat[i];

        char quiend = mat[0][0];
        int contd = 1;
        char quiend2 = mat[0][3];
        int contd2 = 1;
        int p2;
        for(int i = 0; i < 4; i++)
        {
            if(i != 0 && quiend != '.'&& (mat[i][i] == quiend || mat[i][i] == 'T') )
            {
                contd++;
            }
            if(i != 0 && quiend2 != '.' && (mat[i][3-i] == quiend2 || mat[i][3-i] == 'T'))
            {
                contd2++;
            }
            int p = 0;
            char quien = mat[i][0];
            char quien2 = mat[0][i];
            int cont=1;
            int cont2 =1;
            for(int e = 1; e < 4; e++)
            {
                if(quien != '.' && (mat[i][e] == quien  || mat[i][e] == 'T'))
                {
                    cont++;
                }
                if(mat[i][e] == '.')
                {
                    p++;
                }

                if(quien2 != '.' && (mat[e][i] == quien2  || mat[e][i] == 'T'))
                {
                    cont2++;
                }
            }
            if(cont == 4)
            {
                cout << "Case #"<<k<<": "<<quien<<" won"<<endl;
                flag = true;
                break;
            }
            if(cont2 == 4)
            {
                cout << "Case #"<<k<<": "<<quien2<<" won"<<endl;
                flag = true;
                break;
            }
            p2 = p;
        }
        if(contd == 4 && !flag)
        {
            cout << "Case #"<<k<<": "<<quiend<<" won"<<endl;
            flag = true;
        }
        else if(contd2 == 4 && !flag)
        {
             cout << "Case #"<<k<<": "<<quiend2<<" won"<<endl;
             flag = true;
        }
        if(!flag && p2 == 0)
        {
                cout<<"Case #"<<k<<": Draw"<<endl;
                flag = true;
        }
        if(!flag && p2 > 0)
        {
            cout<<"Case #"<<k<<": Game has not completed"<<endl;
        }
    }
}
