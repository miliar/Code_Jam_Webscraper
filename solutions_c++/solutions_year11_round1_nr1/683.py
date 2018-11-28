# include <iostream>
# include <vector>
# include <string>

using namespace std;

int main ()
{
    int test;
    cin>>test;
    for (int testid = 1; testid <=test;testid++)
    {
        long long N;
        int PD,PG;
        cin>>N>>PD>>PG;
        if ((PG == 100 && PD != 100) || (PG == 0 && PD != 0))
        {
           cout<<"Case #"<<testid<<": Broken"<<endl;
        }
        else
        {
            int min = 100;
            if (PD % 2 == 0)
            {
                   min = min/2;
            }
            if (PD % 4 == 0)
            {
                   min = min/2;
            }
            if (PD % 5 == 0)
            {
                   min = min/5;
            }
            if (PD % 25 == 0)
            {
                   min = min/5;
            }            
            if (min <= N)
            {
                   cout<<"Case #"<<testid<<": Possible"<<endl;
            }
            else
            {
                   cout<<"Case #"<<testid<<": Broken"<<endl;
            }
        }                      
    }
    return 0;
}            
        
