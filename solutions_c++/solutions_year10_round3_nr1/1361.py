#include <cstdlib>
#include <iostream>
#include<fstream.h>
using namespace std;

int main(int argc, char *argv[])
{
    int i,j,n,total,cno,count,a[10000],b[10000],c[10000];
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    for(fin>>count,cno=0;cno<count;cno++)
    {
                                         total=0;
                                         for(fin>>n,i=0;i<n;i++)
                                         {
                                                                fin>>a[i]>>b[i];
                                                                c[i]=0;
                                         }
                                         for(i=0;i<n;i++)
                                         {
                                                         for(j=0;j<n;j++)
                                                         {
                                                                         if(j==i)
                                                                                 continue;
                                                                         if((a[j]>a[i])&&(b[j]<b[i]))
                                                                                                    c[i]++;
                                                                         if((a[j]<a[i])&&(b[j]>b[i]))
                                                                                                     c[i]++;
                                                         }
                                         }
                                         for(i=0;i<n;i++)
                                                         total+=c[i];
                                         cout<<total/2<<endl;
                                         fout<<"Case #"<<cno+1<<": "<<total/2<<endl;
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
