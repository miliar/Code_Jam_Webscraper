#include <fstream>
#include <string>
#include <algorithm>


using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");


int tst;

void solve()
{
    int n, a[64],b[64], ret = 0;

    fin >> n;
    
    for (int i=0;i<n;++i)
    {
        string sir;
        
        fin >> sir;
        
        a[i] = 0;
        for (int j=0;j<(int)sir.length();++j)
            if (sir[j]=='1')
                a[i] = j;
    }
    
    for (int i=0;i<n;++i)
    {/*
        for (int j=0;j<n;++j)
            fout << a[j] << " ";
        fout << " - pt " << i << "\n";
*/
        // nu fac nimic ...
        if (a[i] <= i)
        {
        
        for (int j=i+1;j<n;++j)
            b[j] = a[j];
        sort(b+i+1,b+n);
        
        int ok = 1;
        for (int j=i+1;j<n;++j)
            if (b[j] > j)
                ok = 0;
        if (ok == 1)
            continue;
        }
        
        int ok;
        for (int j=i+1;j<n;++j)
        {
            if (a[j] > i)
                continue;
                
            for (int k=j;k>i;--k)
                swap(a[k],a[k-1]);
                
            for (int k=i+1;k<n;++k)
                b[k] = a[k];

            sort(b+i+1,b+n);

            ok = 1;
            
            for (int k=i+1;k<n;++k)
                if (b[k] > k)
                    ok = 0;

            if (ok == 1)
            {
                ret += j-i;
                break;
            }

            for (int k=i;k<j;++k)
                swap(a[k],a[k+1]);
        }
            

    }
    
    fout << "Case #" << ++tst << ": " << ret << "\n";
}
    

int main()
{
    int t;
    
    fin >> t;
    
    while (t--)
        solve();
        
        
    return 0;
}
