#include <iostream>
#include <cstring>
using namespace std;

FILE* inputstream;
FILE* outputstream;
void init()
{
	inputstream = freopen("A-small-attempt4.in", "r", stdin);
	outputstream = freopen("output.txt", "w", stdout);
}
int main ()
{
    init();
    int N1;
    char N[4];
    cin.getline(N, sizeof(N)-1);
    N1 = atoi(N);
    
    for (int i=0; i<N1; i++)
    {
        char A[200]={""};
        char B[200]={""};
        cin.getline (A, sizeof(A)-1);
        for (int j=0; j<sizeof (A)-1;j++)
        {
            if (A[j]=='a'){B[j]='y';}
            if (A[j]=='b'){B[j]='h';}
            if (A[j]=='c'){B[j]='e';}
            if (A[j]=='d'){B[j]='s';}
            if (A[j]=='e'){B[j]='o';}
            if (A[j]=='f'){B[j]='c';}
            if (A[j]=='g'){B[j]='v';}
            if (A[j]=='h'){B[j]='x';}
            if (A[j]=='i'){B[j]='d';}
            if (A[j]=='j'){B[j]='u';}
            if (A[j]=='k'){B[j]='i';}
            if (A[j]=='l'){B[j]='g';}
            if (A[j]=='m'){B[j]='l';}
            if (A[j]=='n'){B[j]='b';}
            if (A[j]=='o'){B[j]='k';}
            if (A[j]=='p'){B[j]='r';}
            if (A[j]=='q'){B[j]='z';}
            if (A[j]=='r'){B[j]='t';}
            if (A[j]=='s'){B[j]='n';}
            if (A[j]=='t'){B[j]='w';}
            if (A[j]=='u'){B[j]='j';}
            if (A[j]=='v'){B[j]='p';}
            if (A[j]=='w'){B[j]='f';}
            if (A[j]=='x'){B[j]='m';}
            if (A[j]=='y'){B[j]='a';}
            if (A[j]=='z'){B[j]='q';}
            if (A[j]==' '){B[j]=' ';}
        }
        cout << "Case #"<<i+1<<": "<<B<<endl;
    }
    return 0;
}
