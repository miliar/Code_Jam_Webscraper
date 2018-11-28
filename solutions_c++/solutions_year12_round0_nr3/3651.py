#include <stdio.h>
#include <math.h>
#include <fstream>
#include <stdlib.h>
#include <ctype.h>
#include <conio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

void check(int,int,int);

int ctr = 0;
int past[1000000];
int ctr_tot = 0;

int main()
{
    string inp;
    string out;
    int i;
    int j;
    int n;
    int n1;
    int n2;
    int num;
    int k = 0;
    ifstream input ("C-small-attempt1.in-1.txt");
    ofstream output ("output.out");
    if(input.is_open())
    {
        getline(input,inp);
        n = atoi(inp.c_str());
        for(i = 1; i <= n; i++)
        {
            getline(input,inp);
            string in = inp;
            output << "Case #" << i << ": ";
            ctr = 0;
            sscanf(inp.c_str(),"%d %d",&n1,&n2);
            cout << "\n\n\n\n" << n1 << " " << n2 << "\n";
            int alpha = 0;
            for(alpha = 0 ; alpha < 1000000; alpha++)
            {
                past[alpha] = 0;
            }
            for(j = n1; j <= n2; j++)
            {
                check(j,n1-1,n2+1);
            }
            output << ctr/2;
            output << "\n";
        }
        input.close();
        output.close();
        getch();
    }
    else
    {
        cout << "Error!! No reading!!" ;
    }
    return 0;
};

//void insert(int n, int m)
//{
//    int flag = 0;
//    int i = 0;
//    for(i = 0; i < ctr; i++)
//    {
//        if(past[i] == n)
//        {
//            flag += 1;
//        }
//    }
//    past[ctr] = n;
//    cout << ctr << " " << n << "\n";
//    ctr = ctr + 1 - flag;
//}

void check(int n, int num1, int num2)
{
    int num = 0, tmp = 0, n1 = 0, n2 = 0, n3 = 0, n4 = 0, n5 = 0, n6 = 0, n7 = 0;
    int count = 0;
    n1 = (int)(n/1000000);
    n2 = (int)((n - n1*1000000)/100000);
    n3 = (int)((n - n1*1000000 - n2*100000)/10000);
    n4 = (int)((n - n1*1000000 - n2*100000 - n3*10000)/1000);
    n5 = (int)((n - n1*1000000 - n2*100000 - n3*10000 - n4*1000)/100);
    n6 = (int)((n - n1*1000000 - n2*100000 - n3*10000 - n4*1000 - n5*100)/10);
    n7 = (int)((n - n1*1000000 - n2*100000 - n3*10000 - n4*1000 - n5*100 - n6*10)/1);
    tmp = n1*1000000 + n2*100000 + n3*10000 + n4*1000 + n5*100 + n6*10 + n7;
    int tp[6];
    if(n1 != 0)
    {
        if(tmp > num1 && tmp < num2)
        {
            count = 0;
            if(tmp >= num)
            {
                num = tmp;
                tp[0] = tmp;
            }
        }
        tmp = n2*1000000 + n3*100000 + n4*10000 + n5*1000 + n6*100 + n7*10 + n1;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
        }
        tmp = n3*1000000 + n4*100000 + n5*10000 + n6*1000 + n7*100 + n1*10 + n2;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1])
                {
                    count += 1;
                    tp[2] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1])
                {
                    count += 1;
                    tp[2] = tmp;
                }
            }
        }
        tmp = n4*1000000 + n5*100000 + n6*10000 + n7*1000 + n1*100 + n2*10 + n3;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2])
                {
                    count += 1;
                    tp[3] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2])
                {
                    count += 1;
                    tp[3] = tmp;
                }
            }
        }
        tmp = n5*1000000 + n6*100000 + n7*10000 + n1*1000 + n2*100 + n3*10 + n4;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3])
                {
                    count += 1;
                    tp[4] = tmp;
                }
            }
            if(tmp <= num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3])
                {
                    count += 1;
                    tp[4] = tmp;
                }
            }
        }
        tmp = n6*1000000 + n7*100000 + n1*10000 + n2*1000 + n3*100 + n4*10 + n5;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3] && tmp != tp[4])
                {
                    count += 1;
                    tp[5] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3] && tmp != tp[4])
                {
                    count += 1;
                    tp[5] = tmp;
                }
            }
        }
        tmp = n7*1000000 + n1*100000 + n2*10000 + n3*1000 + n4*100 + n5*10 + n6;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3] && tmp != tp[4] && tmp != tp[5])
                {
                    count += 1;
                    tp[6] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3] && tmp != tp[4] && tmp != tp[5])
                {
                    count += 1;
                    tp[6] = tmp;
                }
            }
        }
        ctr += count;
	}
    if(n2 != 0 && n1 == 0)
    {
        tmp = n2*100000 + n3*10000 + n4*1000 + n5*100 + n6*10 + n7;
    	if(tmp > num1 && tmp < num2)
        {
            count = 0;
            if(tmp >= num)
            {
                num = tmp;
                tp[0] = tmp;
            }
        }
        tmp = n3*100000 + n4*10000 + n5*1000 + n6*100 + n7*10 + n2;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
        }
        tmp = n4*100000 + n5*10000 + n6*1000 + n7*100 + n2*10 + n3;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1])
                {
                    count += 1;
                    tp[2] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1])
                {
                    count += 1;
                    tp[2] = tmp;
                }
            }
        }
        tmp = n5*100000 + n6*10000 + n7*1000 + n2*100 + n3*10 + n4;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2])
                {
                    count += 1;
                    tp[3] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2])
                {
                    count += 1;
                    tp[3] = tmp;
                }
            }
        }
        tmp = n6*100000 + n7*10000 + n2*1000 + n3*100 + n4*10 + n5;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3])
                {
                    count += 1;
                    tp[4] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3])
                {
                    count += 1;
                    tp[4] = tmp;
                }
            }
        }
        tmp = n7*100000 + n2*10000 + n3*1000 + n4*100 + n5*10 + n6;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3] && tmp != tp[4])
                {
                    count += 1;
                    tp[5] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3] && tmp != tp[4])
                {
                    count += 1;
                    tp[5] = tmp;
                }
            }
        }
        ctr += count;
	}
    if(n3 != 0 && n1 == 0 && n2 == 0)
    {
        tmp = n3*10000 + n4*1000 + n5*100 + n6*10 + n7;
        if(tmp > num1 && tmp < num2)
        {
            count = 0;
            if(tmp >= num)
            {
                num = tmp;
                tp[0] = tmp;
            }
        }
        tmp = n3*10000 + n4*1000 + n5*100 + n6*10 + n7;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
        }
        tmp = n4*10000 + n5*1000 + n6*100 + n7*10 + n3;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1])
                {
                    count += 1;
                    tp[2] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1])
                {
                    count += 1;
                    tp[2] = tmp;
                }
            }
        }
        tmp = n5*10000 + n6*1000 + n7*100 + n3*10 + n4;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2])
                {
                    count += 1;
                    tp[3] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2])
                {
                    count += 1;
                    tp[3] = tmp;
                }
            }
        }
        tmp = n6*10000 + n7*1000 + n3*100 + n4*10 + n5;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3])
                {
                    count += 1;
                    tp[4] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3])
                {
                    count += 1;
                    tp[4] = tmp;
                }
            }
        }
        tmp = n7*10000 + n3*1000 + n4*100 + n5*10 + n6;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3] && tmp != tp[4])
                {
                    count += 1;
                    tp[5] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2] && tmp != tp[3] && tmp != tp[4])
                {
                    count += 1;
                    tp[5] = tmp;
                }
            }
        }
            ctr += count;
	}
    if(n4 != 0 && n1 == 0 && n2 == 0 && n3 == 0)
    {
        tmp = n4*1000 + n5*100 + n6*10 + n7;
        if(tmp > num1 && tmp < num2)
        {
            count = 0;
            if(tmp >= num)
            {
                num = tmp;
                tp[0] = tmp;
            }
        }
        tmp = n5*1000 + n6*100 + n7*10 + n4;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
        }
        tmp = n6*1000 + n7*100 + n4*10 + n5;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1])
                {
                    count += 1;
                    tp[2] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1])
                {
                    count += 1;
                    tp[2] = tmp;
                }
            }
        }
        tmp = n7*1000 + n4*100 + n5*10 + n6;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2])
                {
                    count += 1;
                    tp[3] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1] && tmp != tp[2])
                {
                    count += 1;
                    tp[3] = tmp;
                }
            }
        }
            ctr += count;
	}
    if(n5 != 0 && n1 == 0 && n2 == 0 && n3 == 0 && n4 == 0)
    {
        tmp = n5*100 + n6*10 + n7;
        if(tmp > num1 && tmp < num2)
        {
            count = 0;
            if(tmp >= num)
            {
                num = tmp;
                tp[0] = tmp;
            }
        }
        tmp = n6*100 + n7*10 + n5;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
        }
        tmp = n7*100 + n5*10 + n6;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0] && tmp != tp[1])
                {
                    count += 1;
                    tp[2] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0] && tmp != tp[1])
                {
                    count += 1;
                    tp[2] = tmp;
                }
            }
        }
            ctr += count;
	}
    if(n6 != 0 && n1 == 0 && n2 == 0 && n3 == 0 && n4 == 0 && n5 == 0)
    {
        tmp = n6*10 + n7;
        if(tmp > num1 && tmp < num2)
        {
            count = 0;
            if(tmp >= num)
            {
                num = tmp;
                tp[0] = tmp;
            }
        }
        tmp = n7*10 + n6;
        if(tmp > num1 && tmp < num2)
        {
            if(tmp > num)
            {
                num = tmp;
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
            if(tmp < num)
            {
                if(tmp != tp[0])
                {
                    count += 1;
                    tp[1] = tmp;
                }
            }
        }
            ctr += count;
	}
    if(n7 != 0 && n1 == 0 && n2 == 0 && n3 == 0 && n4 == 0 && n5 == 0 && n6 == 0)
    {
            ctr += count;
	}
}
