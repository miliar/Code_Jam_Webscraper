#include<iostream>
#include<list>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<math.h>
#include <sstream>

using namespace std;


bool verificar(char matriz[4][4],char a)
{

    for(int i = 0;i<4; i ++)
    {
        int conta1 = 0;
        int conta2 = 0;
        for(int j = 0; j < 4; j ++)
        {
            if(matriz[i][j] == a || matriz[i][j] == 'T')
            {
                conta1 ++;
            }
            if(matriz[j][i] == a|| matriz[j][i] == 'T')
            {
                conta2 ++;
            }
        }
        if(conta1 == 4 || conta2 == 4)
            return true;
    }
    int conta = 0;
    for(int i = 0;i < 4; i ++)
    {
        if(matriz[i][i] == a || matriz[i][i] == 'T')
            conta ++;
    }
    if(conta == 4)return true;

     conta = 0;
      int j = 3;
    for(int i = 0;i < 4;i ++,j--)
    {
        if(matriz[i][j] == a || matriz[i][j] == 'T')
            conta ++;
    }
    if(conta == 4)return true;

    return false;


}


int main()
{
    int caso = 1;

    int casos;
    cin>>casos;


    for(int i = 0; i< casos; i ++)
    {
                 char matriz[4][4];
                 long long int a,b;


                int conta = 0;
                bool completo = true;

                        for(int i = 0;i < 4; i ++)
                        {
                            for(int j = 0; j < 4; j ++)
                            {
                                cin>>matriz[i][j];
                                if(matriz[i][j] == '.')
                                    completo = false;
                            }
                        }

                        bool ganadorx = verificar(matriz, 'X');
                        bool ganadory = verificar(matriz, 'O');

                         cout<<"Case #"<<caso++<<": ";


                        if(ganadorx && !ganadory)
                            cout<<"X won"<<endl;
                        else if(!ganadorx && ganadory)
                            cout<<"O won"<<endl;
                        else if(ganadorx && ganadory)
                            cout<<"Draw"<<endl;
                        else if(!ganadorx && !ganadory && !completo)
                            cout<<"Game has not completed"<<endl;
                        else if(!ganadorx && !ganadory && completo)
                            cout<<"Draw"<<endl;







                 //cout<<conta<<endl;
    }




    return 0;
}


