#include <fstream>
using namespace std;

int main()
{
    fstream file1,file2;
    file1.open("A-large.in");
    file2.open("A-large.out");
    int T,casee=1;
    file1>>T;
    while(T>0)
    {
        int N;
        file1>>N;
        int *A,*B;
        A = new int [N];
        B = new int [N];
        for(int i=0; i<N; i++)
                file1>>A[i]>>B[i];
        int score=0;
        for(int i=0; i<N; i++)
        {
                for(int j=0; j<i; j++)
                {
                        if((A[i]>A[j]&&B[i]<B[j])||(A[i]<A[j]&&B[i]>B[j])) score++;
                }
        }
        file2<<"Case #"<<casee<<": "<<score<<endl;
        T--;
        casee++;
    }
    file1.close();
    file2.close();
    system("PAUSE");
    return 0;
}
