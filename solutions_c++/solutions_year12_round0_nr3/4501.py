#include<iostream>
#include<fstream>
using namespace std;
int length(int n)
{
    int count = 0;
    while(n != 0)
    {
        count ++;
        n = n / 10;
    }
    return count;
}
int isrecycle(int a, int b)
{
    for(int i = 0 ; i < length(a); i ++)
    {
        if(a == b)
            return true;
        int d = a % 10;
        a = a / 10;
        int temp = 1;
        for(int j = 0 ; j < length(b)-1;j ++)
        {
            temp = temp * 10;
        }
        temp = temp * d;
        a = temp + a;
        //cout << a << endl;
    }
    return false;
}
int main()
{
   ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
   int cases;
   fin >> cases;
   for(int t = 1; t <= cases; t ++)
   {


    int a,b;
    fin >> a >> b;
    int count = 0;
    for(int i = a; i <=b ; i ++)
    {
        for(int j = a; j <= b; j ++)
        {
            if(i < j)
            {
                if(isrecycle(i,j))
                {
                    count ++;
                }
            }
        }
    }
    fout << "Case #"<< t << ": "<<count << endl;
   }
   fout.close();
   fin.close();
}
