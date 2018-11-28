#include<iostream>
#include<fstream>
using namespace std;
long long N,K,T,cate;
int i;
ofstream fout("snaipar.out");
void mult()
{
    fout<<"Case #"<<i<<": ";
    cate=(1<<N)-1;
    if((K-cate)%(1<<N)==0)
    {fout<<"ON"<<'\n';
    }
    else
    {fout<<"OFF"<<'\n';
    }
}
void cit()
{
ifstream fin("A-large.in");
fin>>T;
for(i=1;i<=T;i++)
   {fin>>N>>K;
   mult();
   }
fin.close();

}

int main()
{
     cit();

    fout.close();
    return 0;

}
