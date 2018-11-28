/*Problem C. Recycled Numbers
Confused? Read the quick-start guide.
Small input
10 points
You may try multiple times, with penalties for wrong submissions.
Large input
15 points
You must solve the small input first.
You will have 8 minutes to solve 1 input file. (Judged after contest.)
Problem

Do you ever become frustrated with television because you keep seeing the same things, recycled over and over again? Well I personally don't care about television, but I do sometimes feel that way about numbers.

Let's say a pair of distinct positive integers (n, m) is recycled if you can obtain m by moving some digits from the back of n to the front without changing their order. For example, (12345, 34512) is a recycled pair since you can obtain 34512 by moving 345 from the end of 12345 to the front. Note that n and m must have the same number of digits (excluding leading zeros) in order to be a recycled pair.

Given integers A and B with the same number of digits, how many distinct recycled pairs (n, m) are there with A ≤ n < m ≤ B?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line containing the integers A and B.
Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1), and y is the number of recycled pairs (n, m) with A ≤ n < m ≤ B.
Limits

1 ≤ T ≤ 50.
A and B have the same number of digits.
Small dataset

1 ≤ A ≤ B ≤ 1000.
Large dataset

1 ≤ A ≤ B ≤ 2000000.
Sample

Input

Output

4
1 9
10 40
100 500
1111 2222
	Case #1: 0
Case #2: 3
Case #3: 156
Case #4: 287
*/

#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

unsigned long int power (int x,int y)
{
    if (y==1)
        return x;
    else
        return x*power(x,y-1);
}
int main()
{
    ifstream in3("in3.txt");
    ofstream ot3("ot3.txt");
    unsigned long int ctr,A,B,digit,r;
    in3>>ctr;
    for ( int i = 0; i < ctr;i++)
    {

        in3>>A;in3>>B;
        r = 0;
        unsigned long int temp =  A;
        digit = 0;

        while (temp !=0)
        {
            digit++;
            temp/=10;
        }
        if (digit ==1)
        {
            ot3<<"Case #"<<i+1<<": "<<"0"<<'\n';
            continue;
        }
        for ( unsigned long int x = A;x<=B;x++)
        {

            vector<unsigned long int> tt;

                for ( int i = 1; i<digit;i++)
                {
                    unsigned long int y = x;
                    unsigned long int p = power(10,i);
                    unsigned long int s = y % p;
                    //if (s ==0)
                       //continue;
                    y /=p;
                    bool repeat = false;
                    y = s*power(10,digit-i) + y;
                    for ( int i =0;i< tt.size();i++)
                    {
                        if (y == tt.at(i))
                        {
                            repeat = true;
                            break;
                        }
                    }

                    if ( y>=A && y <=B && y>x && !repeat)
                    {
                        r++;
                        tt.push_back(y);
                        //flag[y] = true;
                       // ot3<<x<<' '<<s<<' '<<y<<' '<<'\n';
                    }
                }

        }
        ot3<<"Case #"<<i+1<<": "<<r<<'\n';
    }
}
