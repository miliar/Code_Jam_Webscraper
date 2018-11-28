#include <iostream>
#include <stdlib.h>

using namespace std;

float p[3];

float keystrokes(int &pressed, int &L)
{
    if(pressed == 1)
    {
        float e = L*p[0] + (2*L + 1)*(1 - p[0]);
        if(e < L+2) return e;
        else return (float)(L+2);
    }
    if(pressed == 2)
    {
        float ekt = (L-1)*p[0]*p[1] + 2*L*(1-p[0])*(1-p[1]) + 2*L*p[0]*(1-p[1]) + 2*L*(1-p[0])*p[1];
        float eb1 = (L+1)*p[0]*p[1] + (L+1)*p[0]*(1-p[1]) + (2*L+2)*(1-p[0])*(1-p[1]) + (2*L+2)*(1-p[0])*p[1];
//        float eb2 = L+3;worse than epe
        float epe = L+2;
        float min1 = (ekt<eb1)?ekt:eb1;
        return (epe<min1)?epe:min1;
    }
    if(pressed == 3)
    {
        float ekt = (L-2)*p[0]*p[1]*p[2] + (2*L-1)*(
                                                     p[0]*p[1]*(1-p[2]) +
                                                     (1-p[0])*p[1]*p[2] +
                                                     p[0]*(1-p[1])*p[2] +
                                                     (1-p[0])*(1-p[1])*p[2] +
                                                     (1-p[0])*p[1]*(1-p[2]) +
                                                     p[0]*(1-p[1])*(1-p[2]) +
                                                     (1-p[0])*(1-p[1])*(1-p[2])
                                                   );
        float eb1 = L*p[0]*p[1]*p[2] + L*p[0]*p[1]*(1-p[2]) + 
                                           (2*L+1)*(
                                                     (1-p[0])*p[1]*p[2] +
                                                     p[0]*(1-p[1])*p[2] +
                                                     (1-p[0])*(1-p[1])*p[2] +
                                                     (1-p[0])*p[1]*(1-p[2]) +
                                                     p[0]*(1-p[1])*(1-p[2]) +
                                                     (1-p[0])*(1-p[1])*(1-p[2])
                                                   );
        float eb2 = (2+L)*( p[0]*p[1]*p[2] +
                            p[0]*p[1]*(1-p[2]) +
                            p[0]*(1-p[1])*p[2] +
                            p[0]*(1-p[1])*(1-p[2]) ) +
                            
                     (2*L+3)*(
                                   (1-p[0])*p[1]*p[2] +
                                   (1-p[0])*(1-p[1])*p[2] +
                                   (1-p[0])*p[1]*(1-p[2]) +
                                   (1-p[0])*(1-p[1])*(1-p[2])
                             );
        //float eb3 = L+4;worse than epe
        float epe = L+2;
        
        float min1 = (ekt<eb1)?ekt:eb1;
        float min2 = (epe<eb2)?epe:eb2;
        return (min1<min2)?min1:min2;
    }
    return (float)L+2;
}

int main (int argc, char *argv[])
{
    int T;
    cin >> T;

    int k = 0;
    while(k < T)    
    {
        int A, B;
        cin >> A; cin >> B;
        int i = 0;
        for(i = 0; i < 3; i++) p[i]=0;
        i=0;
        while(i < A)
        {
            cin >> p[i];
            i++;
        }
        char s[100];
        for(i = 0; i < 100; i++) s[i] = 0;
        sprintf(s, "Case #%d: %.6f", k+1, keystrokes(A, B));
        cout << s << endl;
        k++;
    }
    return 0;
}
