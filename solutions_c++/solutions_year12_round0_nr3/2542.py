#include <fstream>
#include <set>

using namespace std;

int digit(int m)
{
    int ret = 0;
    while(m > 0)
    {
        m/=10;
        ret ++;
    }
    return ret;
}

int rotate(int m, int j)
{
   int d = digit(m);
   int div = 1;
   for (int i=j; i<d; i++)
   {
       div *= 10;
   }
   int haha = 1;
   for (int i=0; i<j; i++)
       haha *= 10;

   int last = m % div;
   int first = m/div;
   return last*haha+first;
}
int main()
{
    ofstream output;
    ifstream input("C-large.in");
    output.open("C-large.out");

    //ifstream input("C-small-attempt0.in");
    //output.open("C-small-attempt0.out");
    int t;
    input >> t;

    for(int c = 0; c<t; c++)
    {
        output<<"Case #"<<c+1<<": ";

        int a,b;
        input>>a>>b;

        int ret = 0;

        for(int m=a; m<b; m++)
        {
            set<int> kuku;
            int leng = digit(m);
            for(int i=1; i<leng; i++)
            {
                int n = rotate(m,i);
                if (n<=m || n>b || kuku.count(n)) continue;
                kuku.insert(n);
                ret++;
            }
        }
        output<<ret<<endl;
    }
}

