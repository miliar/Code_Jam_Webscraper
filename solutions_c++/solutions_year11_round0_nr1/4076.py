#include<iostream>

using namespace std;

int main(){
    int test, n, p;
    char r;
    cin >> test;
    for (int cs = 1; cs <= test; cs++)
    {
        cin >> n;
        int t1 = 1, t2 = 1, temp1 = 0, temp2 = 0, count = 0, c1, c2;    
        for (int i = 0; i < n; i++)
        {
            cin >> r >> p;
            if (r == 'O')
            {
                c1 = t1 - p;
                c1 = c1>0?c1:(-1*c1);
                if (temp1 >= c1)
                {
                    temp2++;
                    count++;
                    t1 = p;
                    temp1 = 0;
                }
                else
                {
                    c1 -= temp1;
                    temp2 += c1+1;
                    count += c1+1;
                    t1 = p;
                    temp1 = 0;
                }
            }
            else
            {
                c2 = t2 - p;
                c2 = c2>0?c2:(-1*c2);
                if (temp2 >= c2)
                {
                    temp1++;
                    count++;
                    t2 = p;
                    temp2 = 0;
                }
                else
                {
                    c2 -= temp2;
                    temp1 += c2+1;
                    count += c2+1;
                    t2 = p;
                    temp2 = 0;
                }
            }
        }
        cout << "Case #" << cs << ": " << count << endl;
    }
    return 0;
}
                
        
