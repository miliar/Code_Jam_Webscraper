#include <fstream>

using namespace std;

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.in");
    int t;
    fin>>t;
    int n,j;
    long int *a,*b;
    long long int count;
    for(int i=0;i<t;i++)
    {
        fin>>n;
        count=0;
        a=new long int[n];
        b=new long int[n];
        for(j=0;j<n;j++)
        {
            fin>>a[j]>>b[j];
        }

        for(j=0;j<n;j++)
        {
            for(int k=j+1;k<n;k++)
            {
                if((a[j]<a[k])&&(b[j]>b[k]))
                {
                    count++;
                }
                else if((a[j]>a[k])&&(b[j]<b[k]))
                {
                    count++;
                }
            }
        }

        fout<<"Case #"<<i+1<<": "<<count<<endl;
        delete[] a;
        delete[] b;
    }
    return 0;
}
