#include <stdio.h>
#include <iostream>
using namespace std;

int main(int argc, char **argv) {
    int T;
    cin >> T;
    for (int i =0; i<T; i++)
    {
        int result = 0;
        int tmpTr = 0;
        int N, S, p;
        cin >> N>> S>> p;
        int googlers[N];
        for (int j = 0; j<N; j++)
            cin >> googlers[j]; 
        
        for (int j = 0; j< N; j++)
        {
            int a = googlers[j]/3;
            int b = googlers[j]/3;
            int c = googlers[j]/3;
            
            if (a+b+c == googlers[j])
            {
                if (a>=p)
                {
                    tmpTr++;
                    result ++;
                }
                else
                    if (a+1>=p && S>0 && a>0)
                {
                    S--;
                    result++;
                }
                else
                    tmpTr++;
                continue;
            }
            
            if (a+b+c+1 == googlers[j])
            {
                a++;
                if (a>=p)
                {
                    result++;
                }
                tmpTr++;
                continue;
            }
            
            if (a+b+c+2 == googlers[j])
            {
                a++;
                if (a>=p)
                {
                    tmpTr++;
                    result++;
                }
                else if (S>0)
                {
                    if (a+1>=p)
                    {
                        S--;
                        result++;
                    }
                }
                else
                {
                    tmpTr++;
                }
            }
        }
        cout << "Case #" <<(i+1) <<": "<<result<< "\n";
        
    }
}