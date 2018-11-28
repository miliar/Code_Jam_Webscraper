#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("A-large.in",ios::in);

    ofstream fout;
    fout.open("A-large.out",ios::out);

    int no_cases,N,A[1000],B[1000],i,j,k,inter;
    fin>>no_cases;

    for(i = 0; i < no_cases; i++)
    {
        inter = 0;
        fin>>N;

        for(j = 0; j < N; j++)
        {
            fin>>A[j]>>B[j];
        }
        for (j=0;j<N ;j++ )
        {
        	for(k = j+1;k<N;k++)
        	{
        	    if(A[j] > A[k] && B[j] < B[k] )
                    inter++;

                else if(A[j] < A[k] && B[j] > B[k] )
                    inter++;
        	}
        }
        fout<<"Case #"<<i+1<<": "<<inter<<"\n";
    }
}
