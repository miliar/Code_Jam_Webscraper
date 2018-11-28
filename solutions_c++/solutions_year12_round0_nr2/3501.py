#include<iostream>
using namespace std;

bool makeNoSeprinsingDes(int n,int des);
bool makeSeprinsingToMaximize(int n,int des);
int main()
{
    int i,j,k;
    int people,surpring,desire,testCase;
    int points[101];
    int totalHigh;
    cin>>testCase;
    for(int t=0;t<testCase;t++)
    {

        totalHigh=0;
        cin>>people>>surpring>>desire;
        for(i=0;i<people;i++)
        {
            cin>>points[i];
        }
        for(i=0;i<people;i++)
        {
            if(makeNoSeprinsingDes(points[i],desire))
            {
                totalHigh++;
            }
            else if(surpring)
            {
                if(makeSeprinsingToMaximize(points[i],desire))
                {
                    surpring--;
                    totalHigh++;
                }
            }
        }
        cout<<"Case #"<<t+1<<": "
        <<totalHigh<<endl;
    }

    return 0;
}

bool makeNoSeprinsingDes(int n,int des)
{
    if(n<des)
    return false;
    int rem=n%3;
    int res=n/3;
    if(rem==0)
    {
        if(res<des)
        return false;
    }
    else
    {
        if((res+1)<des)
        return false;
    }
    return true;
}

bool makeSeprinsingToMaximize(int n,int des)
{
    if((n<2) || (n<des))
    return false;
    int rem=n%3;
    int res=n/3;
    if(rem==1)
    {
        return false;
    }
    else if(rem==0)
    {
        if((res+1)<des)
        return false;
    }
    else
    {
        if((res+2)<des)
        return false;
    }
    return true;
}


