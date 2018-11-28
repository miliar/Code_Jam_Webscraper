#include <iostream>

using namespace std;

int main()
{
    int T, N, S,wynik;
    short *tab,p;
    cin >> T;
    for(int t =0;t<T;t++)
    {
        wynik=0;
        cin >> N;
        tab=new short[N];
        cin >> S;
        cin >> p;
        for(int i =0;i<N;i++)
        {
            cin >>tab[i];
        }
        for(int i =0;i<N;i++)
        {
            if(tab[i]<p)
                continue;
            else if(tab[i]>=3*p-2)
                wynik++;
            else if(tab[i]>=3*p-4&&S>0)
            {
                wynik++;
                S--;
            }
        }

        delete tab;
        cout << "Case #"<<t+1<<": "<< wynik<<endl;
    }
    return 0;
}
