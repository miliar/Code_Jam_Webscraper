#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;
int digits(int num);

int main()
{
    ifstream stream("C:/C-small-attempt0.in");
    ofstream result("C:/result.txt");

if(stream && result)
{
    string line;
    int nb_cases, a, b, d, trois, deux, un, r;
    getline(stream, line);
    istringstream ss(line);
    ss >> nb_cases;
    for(int i=1; i<=nb_cases; i++)
    {
        r=0;
        stream >> a;
        stream >> b;
        d=digits(b);
        if(d==1)
        {
            r=0;
        }
        else if(d==2)
        {
            for(int j=a; j<=b; j++)
            {
                 deux=j%10;
                 un=j/10;
                 if(((deux*10)+un)>=a && ((deux*10)+un)<=b && un!=deux)
                 {
                     r++;
                 }
            }
        }
        else if(d==3)
        {
            for(int j=a; j<=b; j++)
            {
                trois=j%10;
                deux=(j%100)/10;
                un=j/100;
                int x=(trois*100)+(un*10)+deux;
                int y=(deux*100)+(trois*10)+un;
                if(x>=a && x<=b)
                {
                    if((un!=trois) || (deux!=trois) || (un!=deux))
                    {
                        r++;
                    }
                }
                if(y>=a && y<=b)
                {
                   if((un!=trois) || (deux!=trois) || (un!=deux))
                    {
                        r++;
                    }
                }
            }
        }
        result << "Case #" << i << ": " << r/2 << endl;
    }
}
else
{
    result << "ERREUR: Impossible d'ouvrir le fichier en lecture." << endl;
}
    return 0;
}
int digits(int num)
{
    int d=0;
    while(num > 0)
    {
        d++;
        num/=10;
    }
    return d;
}
