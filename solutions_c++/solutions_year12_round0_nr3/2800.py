#include <iostream>
#include <fstream>

using namespace std;

int get_string(int A, char str[])
{
    int len, rem;
    for(len = 0; A > 0; len++)
    {
        rem = A%10;
        A = A/10;
        str[len] = (char)(rem + '0');
    }
    str[len] = '\0';
    for(int i=0; i < (len/2); i++)
    {
        char temp = str[i];
        str[i] = str[len-i-1];
        str[len-i-1] = temp;
    }
    return len;
}

int get_dec(char str[])
{
    int num = 0;
    for(int i=0; str[i] != '\0'; i++)
    {
        num = num*10 + ((int)(str[i] - '0'));
    }
    return num;
}

int count_recycle(int A, int B)
{
    int count = 0, x, len, flag;
    char num1[10], num2[10];

    int check_arr[50];

    for(int i=A; i<=B; i++)
    {
        int f=0;
        for(int j=0; j<50; j++)
            check_arr[j] = 0;

        len = get_string(i, num1);
        for(int j=1; j<len; j++)
        {
            int k, l;

            for(k=j, l=0; k<len; k++, l++)
                num2[l] = num1[k];
            for(k=0; k<j;k++, l++)
                num2[l] = num1[k];
            num2[l] = '\0';
            x = get_dec(num2);
            if((i<x) && (x <= B))
            {
                flag = 0;
                for(int m=0; m<f; m++)
                    if(x == check_arr[m])
                    {
                        flag = 1;
                    }
                if(!flag)
                {
                    count++;
                    check_arr[f] = x;
                    f++;
                }
            }
        }
    }
    return count;
}

int main()
{
    int T, A, B;
    ifstream file_in("C-large.in");
    ofstream file_out("output2.txt");
    file_in>>T;

    for(int i=1; i<=T; i++)
    {
        file_in>>A>>B;
        file_out<<"Case #"<<i<<": "<<count_recycle(A, B);
        if(i != T)
            file_out<<endl;
    }
    return 0;
}
