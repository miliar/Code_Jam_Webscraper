#include <stdio.h>
#include <iostream>
#include "math.h"
using namespace std;

int num(int *digits, int len)
{
    int res = 0;
    for (int i=0; i<len; i++)
    {
        res+=digits[i]*pow(10,i);

    }
    return res;
}


int main(int argc, char **argv) {
    int T;
    cin >> T;
    for (int i =0; i<T; i++)
    {
        int A,B;
        cin >>A>>B;
        int result = 0;
        int c = A;
        


        for (int k = A; k<=B; k++)
        {
            c = k;
            int j = 0;
            while (c>9)
            {
                c= c/10;
                j++;
            }
            j++;
            
            c=k;
            int digits[j];
            for (int p = 0; p<j; p++)
            {
                digits[p] = c-(c/10)*10;
                c = c/10;
            }
            for (int y = 0; y<j-1; y++)
            {
                int t=digits[0];
                for (int z =0; z<j-1; z++)
                    digits[z] = digits[z+1];
                digits[j-1] = t;
                
                int len = sizeof(digits)/sizeof(digits[0]);
                
                if (num(digits,len)>=A && num(digits,len) <=B 
                    && k>=A && k <=B 
                    && num(digits,len) > k)
                    result++;
            }
        }
        
        cout << "Case #" <<(i+1) <<": "<<result<< "\n";
        
    }
}

