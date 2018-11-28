#include<fstream>

using namespace std;

int func(int x)
{
    if(x>0) return x;
    else return 0;
}
int main()
{
    ifstream in("B-large.in");
    ofstream out("out.txt");
    int T;
    in>> T;
    for(int i=0;i<T;i++)
    {
        int n;
        in>>n;
        int s;
        in>>s;
        int m;
        in>>m;
        int above=0;
        for(int j=0;j<n;j++)
        {
            int x;
            in>>x;
            if(x>=func(m)+func(m-1)*2)
            {
                above++;
                continue;
            }
            else if(x>=func(m)+func(m-2)*2&&s!=0)
            {
                above++;
                s--;
                continue;
            }
        }
        out<<"Case #"<<i+1<<": "<<above<<endl;
    }
    return 0;
}
