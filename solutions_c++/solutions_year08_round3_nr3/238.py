#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char **argv)
{
	fstream fp;
	unsigned int N, i;
	unsigned int m, k;
	unsigned long long n, X, Y, Z, j, *c, tc, *a, *num, p, md = 1000000007;
	
	fp.open(argv[1], fstream::in);

	fp>>N;
	

	for (i=0; i<N; ++i)
	{
		cout<<"Case #"<<i+1<<": ";
		//////////////////////////
		fp>>n>>m>>X>>Y>>Z;
		
		a = new unsigned long long[m];
		c = new unsigned long long[n];
		num = new unsigned long long[n];
	
		for (k=0; k<m; ++k)
		{
            fp>>a[k];
        }
        
        tc = 0;
        
        for (j=0; j<n; ++j)
        {
            num[j] = a[j % m];
            a[j % m] = ( X * a[j % m] + Y * (j + 1)) % Z;

            c[j] = 1;
            for (p=0; p<j; ++p)
            {
                if (num[p] < num[j])
                    c[j] = (c[j] + c[p]) % md;
            }
            tc = (tc + c[j]) % md;
        } 
        
        cout<<(tc);
				
		delete []a;
		delete []c;
		delete []num;		
		//////////////////////////		
		cout<<endl;
	} // i
	fp.close();

	return 0;
}
