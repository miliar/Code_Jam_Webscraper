#include <iostream>
#include <fstream>
using namespace std;

unsigned long ebob(unsigned long *a,int n,int max_index)
{
    int flag=0;
    unsigned long ebob=1, div=2;
    while (div<=a[max_index])
    {
        if (a[0]%div==0)
        {
            for (int i=1;i<n;i++)
            {
                if (a[i]%div!=0) flag=1;
            }
            if (flag==1)
            {
                div++;
                flag=0;
            }
            else
            {
                for (int i=0;i<n;i++)
                {
                    a[i]/=div;
                }
                ebob*=div;
            }
        }
        else div++;
    }
    return ebob;
}

int main()
{
    ifstream inp;
    ofstream op;
    inp.open("B-small-attempt1.in");
    op.open("B-small.out");
    
    int C;
    inp >> C;
    for (int i=0;i<C;i++)
    {
        int N;
        inp >> N;
        unsigned long *numbers,*diff;
        numbers=new unsigned long[N];
        diff=new unsigned long[N];
        for (int j=0;j<N;j++) {
            inp >> numbers[j];
            cout << "num" << numbers[j] << "\n"; }
        unsigned long min=numbers[0],max=numbers[0];
        int min_index=0,max_index=0;
        for (int j=1;j<N;j++)
        {
            if (numbers[j]<min) 
            {
                min=numbers[j];
                min_index=j;
            }
            if (numbers[j]>max)
            {
                max=numbers[j];
                max_index=j;
            }
        }
        for (int j=0;j<N;j++)
        {
            diff[j]=numbers[j]-min;
        }
        unsigned long eb=ebob(diff,N,max_index);
        unsigned long res=eb;
        int k=2;
        cout << "ebob" << eb << "\n";
        while (res<max)
        {
            res=k*eb;
            k++;
        }
        res-=max;
        op << "Case #" << i+1 << ": " << res << "\n";
    }
    op.close();
    inp.close();
    return 0;
}
    