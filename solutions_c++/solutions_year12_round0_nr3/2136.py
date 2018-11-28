#include<iostream>
#include<fstream>

using namespace std;

ifstream fin("Clarge.in");
ofstream fout("Cout.txt");
int base10[15];
int found[15];

bool notfound(int count, int switched)
{
    for(int i=0;i<count;i++)
        if(found[i]==switched)
            return false;
    return true;
}

int main()
{
    int ten = 1;
    for(int i=0;i<15;i++)
    {
        base10[i]=ten;
        ten*=10;
    }
    int T;
    fin >> T;
    for(int i=1;i<=T;i++)
    {
        int ans = 0;
        int A,B;
        fin >> A >> B;
        for(int j=A;j<B;j++)
        {
            int temp = j;
            int count = 0;
            int b_10 = 1;
            while(temp>0)
            {
                count++;
                temp/=10;
            }
            int foundcount = 0;
            for(int k=1;k<count;k++)
            {
                int switched = (j%base10[k])*base10[count-k]+j/base10[k];
                if(switched>j&&switched<=B&&notfound(foundcount, switched))
                {
                    found[foundcount++]=switched;
                    ans++;
                }
            }
        }
        fout << "Case #" << i << ": " << ans << endl;
    }

}
