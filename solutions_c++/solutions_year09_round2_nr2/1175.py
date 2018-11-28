#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream f;
    ofstream g;
    f.open("B-small.in");
    g.open("B-small.out");

    int T, cif, flag,flagx, buff, low;
    vector <int> X(30), Y(30);
    char c;

    f>>T; f.get();
    for(int i=1; i<=T; i++)
    {
        cif=0;
        while(f.peek()!=EOF && f.peek()!='\n')
        {
            cif++;
            f.get(c);
            X[cif]=c-48;
        }
        Y=X;

        flagx=0;
        for(int j=cif; j>1 && !flagx; j--)
        {
            if(Y[j]>Y[j-1])
            {
                flagx=1;
                low=j-1;
            }
        }


        if(flagx)
        {
        do
        {   flag=0;
            for(int j=low+1; j<cif; j++)
                if(Y[j]>Y[j+1])
                {
                    buff=Y[j];
                    Y[j]=Y[j+1];
                    Y[j+1]=buff;
                    flag=1;
                }

        }while(flag);



        flag=1;
        for(int j=low+1; j<=cif && flag; j++)
            if(Y[low]<Y[j])
            {
                buff=Y[low];
                Y[low]=Y[j];
                Y[j]=buff;
                flag=0;
            }
        do
        {   flag=0;
            for(int j=low+1; j<cif; j++)
                if(Y[j]>Y[j+1])
                {
                    buff=Y[j];
                    Y[j]=Y[j+1];
                    Y[j+1]=buff;
                    flag=1;
                }

        }while(flag);

        }
        else
        {
            cif++;
            Y[cif]=0;
            do
        {   flag=0;
            for(int j=1; j<cif; j++)
                if(Y[j]>Y[j+1])
                {
                    buff=Y[j];
                    Y[j]=Y[j+1];
                    Y[j+1]=buff;
                    flag=1;
                }

        }while(flag);

        buff=1;
        while(Y[buff]==0) buff++;
        Y[1]=Y[buff];
        for(int jk=2; jk<=buff; jk++)
            Y[jk]=0;
        }


        g<<"Case #"<<i<<": ";
        for(int j=1; j<=cif; j++)
            g<<Y[j];
        g<<endl;

        f.get();
    }



    f.close();
    g.close();
    return 0;
}
