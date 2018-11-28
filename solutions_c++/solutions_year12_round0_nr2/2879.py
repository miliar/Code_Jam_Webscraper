#include <fstream>
#include <iostream>
using namespace std;
int main()
{
    ifstream in("1.in");
    ofstream out("1.out");
    int N;
    in>>N;
    int k=0;
    while(k!=N)
    {
        k++;
        int T,S,P;
        in>>T>>S>>P;
        int A[T];
        for(int i=0;i<T;i++)
            in>>A[i];
        long count=0;
        for(int i=0;i<T;i++)
        {
            if(A[i]%3==0)
            {
                if(A[i]/3>=P)
                    count++;
                else if(S)
                {
                    int m=(A[i]+3)/3;
                    if(m>=P && m-2>=0)
                    {
                        S--;
                        count++;
                    }

                }
            }
            else if( A[i]%3==2)
            {
                int m=(A[i]+1)/3;
                if(m>=P && m-1>=0 )
                    count++;
                else if(S)
                {
                    int m=(A[i]+4)/3;
                    if(m>=P && m-2>=0)
                    {
                        S--;
                        count++;
                    }
                }
            }

            else
            {
                int m=(A[i]+2)/3;
                if(m>=P && m-1>=0)
                    count++;

            }
        }
        out<<"Case #"<<k<<": "<<count<<endl;
    }

}
