#include <iostream>
using namespace std;
long long A,B;
int numOfRecycledPair(long long num)
{
    int retV=0;
    int div = 10;
    int maxDiv = 10;
    long long pNum = num/10;
    int presentValueOfNum = num;
    while(num/maxDiv)
    {
        maxDiv = maxDiv*10;
    }
    maxDiv=maxDiv/10;
    int remainder;
    while(pNum)
    {

        remainder = num%div;
        int recycledNum = remainder*maxDiv+pNum;
        if((recycledNum>num)&&(recycledNum>=A)&&(recycledNum<=B))
        {
            retV=retV+1;
        }
        div = div*10;
        maxDiv=maxDiv/10;
        pNum = num/div;
    }
    return retV;
}
int main()
{
    int testcases;
    cin >> testcases;
    for(int i = 0; i<testcases;i++)
    {
        int returnValue=0;
        cin>> A>> B;
        for(long long k =A; k<=B; k++)
        {
            int temp = numOfRecycledPair(k);
            returnValue = returnValue+temp;
        }
        cout<<"Case #"<<i+1<<": "<<returnValue<<endl;
    }
    return 0;
}
