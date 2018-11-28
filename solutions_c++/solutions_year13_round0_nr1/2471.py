#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("test.txt");
    ofstream fout;
    fout.open("out.txt");
    int n;
    char p[4][4];
    fin >> n;
    bool flag = 0;
    for (int num=0; num<n; num++)
    {
        flag = 0;
        fout << "Case #" << num+1 << ": ";
        int sumt=0,sumx=0,sumo=0,sum=0;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                fin >> p[i][j];
        for (int i=0; i<4; i++)
        {
            sumo=sumx=sum=sumt=0;
            for (int j=0; j<4; j++)
                if (p[i][j]=='O') sumo++; else
                   if (p[i][j]=='X') sumx++; else
                       if (p[i][j]=='T') sumt++;
           
            if ((sumx==4)||(sumx==3)&&(sumt==1))
            {
                fout << "X won" <<endl;
                flag=1;
                break;
            } else
                if ((sumo==4)||(sumo==3)&&(sumt==1))
                {
                    fout << "O won" << endl;
                    flag=1;
                    break;
                }
        }
         if (flag) continue;
        for (int j=0; j<4; j++)
        {
            sumo=sumx=sumt=0;
            for (int i=0; i<4; i++)
                if (p[i][j]=='O') sumo++; else
                   if (p[i][j]=='X') sumx++; else
                       if (p[i][j]=='T') sumt++;
           
            if ((sumx==4)||(sumx==3)&&(sum==1))
            {
                fout << "X won" <<endl;
                flag=1;
                break;
            } else
                if ((sumo==4)||(sumo==3)&&(sum==1))
                {
                    fout << "O won" << endl;
                    flag=1;
                    break;
                }
        }
        if (flag) continue;
        sumo=sumx=sumt=0;
        for (int i=0; i<4; i++)
             if (p[i][i]=='O') sumo++; else
                   if (p[i][i]=='X') sumx++; else
                       if (p[i][i]=='T') sumt++;
         if ((sumx==4)||(sumx==3)&&(sumt==1))
            {
                fout << "X won" <<endl;
                flag=1;
            } else
                if ((sumo==4)||(sumo==3)&&(sumt==1))
                {
                    fout << "O won" << endl;
                    flag=1;
                }
        if (flag) continue;
         sumo=sumx=sumt=0;
        for (int i=0; i<4; i++)
             if (p[i][3-i]=='O') sumo++; else
                   if (p[i][3-i]=='X') sumx++; else
                       if (p[i][3-i]=='T') sumt++;
         if ((sumx==4)||(sumx==3)&&(sumt==1))
            {
                fout << "X won" <<endl;
                flag=1;
            } else
                if ((sumo==4)||(sumo==3)&&(sumt==1))
                {
                    fout << "O won" << endl;
                    flag=1;
                }
        if (flag) continue;
        sum=0;
        for (int i=0; i<4; i++)
            if (flag) break; else
            for (int j=0; j<4; j++)
            if (p[i][j]=='.')
                {
                    fout << "Game has not completed"<<endl;
                    flag=1;
                    break;
                }
        if (flag) continue;
        fout << "Draw"<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
