#include <iostream>
#include <cstring>
using namespace std;


FILE* inputstream;
FILE* outputstream;
void init()
{
	inputstream = freopen("C-large.in", "r", stdin);
	outputstream = freopen("output.txt", "w", stdout);
}

int main ()
{
    init();
    int X, N, Ai, Bi, Ci, Di, kc, ans, ans0, ans1, ans2;
    char A[100]={""};
    char B[100]={""};
    char Cs[100]={""};
    char Ds[100]={""};
    
    
    cin >> N;
    
    for (int i=0; i<N; i++)
    {
        cin >> A >> B;
        Ai = atoi(A);
        Bi = atoi(B);
        Ci = (Ai+Bi)/2;
        ans = 0;
        ans0 = 0;
        ans1 = 0;
        ans2 = 0;
        
        for (int l=Ai ; l<=Bi ;l++)
        {
             itoa(l,Cs,10);
             for (int j=0; j<strlen(A)-1;j++)
             {
                 Ds[0] = Cs[0];
                 for (int k=0; k<strlen(A)-1; k++)
                 {
                     Cs[k] = Cs[k+1];
                 }
                 Cs[strlen(A)-1]=Ds[0];
                 Di=atoi(Cs);
   
                 if (Di>l&&Di<=Bi){ans=ans+1;}
                 
                 if (strlen(A)==4&&Cs[0]==Cs[2]&&Cs[1]==Cs[3]&&Di>l&&Di<=Bi){ans=ans-1;ans1=1;}
                 if (strlen(A)==6&&Cs[0]==Cs[2]&&Cs[2]==Cs[4]&&Cs[1]==Cs[3]&&Cs[3]==Cs[5]&&Di>l&&Di<=Bi){ans=ans-1;ans1=1;}
                 if (strlen(A)==6&&Cs[0]==Cs[3]&&Cs[1]==Cs[4]&&Cs[2]==Cs[5]&&Di>l&&Di<=Bi){ans=ans-1;ans0=ans0+1;ans1=1;}
             }
             if (ans0>=4){ans1=2;}
             ans2=ans1+ans2;
             ans1 = 0;
             ans0 = 0;
        }
        
        cout <<"Case #"<<i+1<<": "<<ans+ans2<<endl;
    }
    return 0;
}
