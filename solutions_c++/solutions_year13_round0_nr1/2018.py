#include <iostream>
#include <vector>
#include <fstream>
using namespace std;


int mat[4][4];

string result()
{
    int i,j;
    vector <int> res;



    int k;

//    cout<<"mat is \n";
//    for(j=0;j<4;j++)
//       {cout<<"\n";
//        for(k=0;k<4;k++)
//            cout<<mat[j][k];
//        }


    res.push_back(mat[0][0]*mat[0][1]*mat[0][2]*mat[0][3]);
    res.push_back(mat[1][0]*mat[1][1]*mat[1][2]*mat[1][3]);
    res.push_back(mat[2][0]*mat[2][1]*mat[2][2]*mat[2][3]);
    res.push_back(mat[3][0]*mat[3][1]*mat[3][2]*mat[3][3]);

    res.push_back(mat[0][0]*mat[1][0]*mat[2][0]*mat[3][0]);
    res.push_back(mat[0][1]*mat[1][1]*mat[2][1]*mat[3][1]);
    res.push_back(mat[0][2]*mat[1][2]*mat[2][2]*mat[3][2]);
    res.push_back(mat[0][3]*mat[1][3]*mat[2][3]*mat[3][3]);

    res.push_back(mat[0][0]*mat[1][1]*mat[2][2]*mat[3][3]);
    res.push_back(mat[0][3]*mat[1][2]*mat[2][1]*mat[3][0]);


    for(i=0;i<res.size();i++)
    {
        if(res[i]==16 || res[i]==40) return "X won";
        if(res[i]==81 || res[i]==135) return "O won";
     }

    for(i=0;i<res.size();i++)
    {
        if(res[i]==0) return "Game has not completed";
    }

    return "Draw";

}

int getnum(char t)
{
    if(t=='X') return 2;
    if(t=='O') return 3;
    if(t=='.') return 0;
     if(t=='T') return 5;
}

int main()
{
    int tc,j,k,i;
    char tmp;
    ifstream Cin("inp.in");
    ofstream Cout("out.in");

    Cin>>tc;
    for(i=0;i<tc;i++)
    {
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {

                Cin>>tmp;
                mat[j][k]= getnum(tmp);

            }

        Cout<<"Case #"<<i+1<<": "<<result()<<"\n";


    }

}
