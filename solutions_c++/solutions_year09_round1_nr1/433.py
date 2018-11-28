#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cstdlib>

#define MAX 11814485
using namespace std;
unsigned short table[MAX+1],pwr[11];

/* Creates a table of numbers in which for each number the bases in which it is a happy number is saved*/
/* Saved to a file called Table.txt*/

bool isHappy(int n, int b)
{
    int dig,i,m;
    bool found;
    vector <int> rep;
    //cout << endl << n << " ";
    do
    {
        rep.push_back(n);
        m=n;n=0;
        while(m)
        {
            dig=m%b;
            n+=(dig*dig);
            m/=b;
        }
        //cout << n << " ";
        if(n==1)
            return true;
        for(i=0,found=false;i<rep.size() && !found;++i)
            found=(rep[i]==n);
    } while(!found);
    return false;
}

void buildTable()
{
    int i,j,b;
    pwr[0]=1;
    for(i=1;i<11;++i)
        pwr[i]=pwr[i-1]*2;

    for(i=2;i<=MAX;++i)
    {
        table[i]=0;
        for(b=2;b<=10;++b)
        {
            if(isHappy(i,b))
                table[i]+=pwr[b];
        }
        cout << table[i] << endl;
    }
}

int main()
{
	buildTable();
	return 0;
}
