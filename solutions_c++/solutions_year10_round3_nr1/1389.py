#include<iostream>
#include<fstream>
using namespace std;
struct nod{
    int a;
    int b;
};
nod a[1005];
int N,T;
ofstream fout("date.out");
void cit()
{int no,i,j,ii,jj;

    ifstream fin("edit.in");
    fin>>T;
    for(i=1;i<=T;i++)
     {fin>>N;

     no=0;
     for(j=1;j<=N;j++)
       {fin>>a[j].a>>a[j].b;

       }

    for(ii=1;ii<=N;ii++)
    for(jj=1;jj<=N;jj++)
       if(ii!=jj)
        {
            if(((a[ii].a<a[jj].a)&&(a[ii].b>a[jj].b) )||((a[ii].a<a[jj].a)&&(a[ii].b>a[jj].b) ))

        no++;

        }

        fout<<"Case #"<<i<<": "<<no<<"\n";
     }


}

int main()
{

    cit();
    fout.close();
    return 0;

}
