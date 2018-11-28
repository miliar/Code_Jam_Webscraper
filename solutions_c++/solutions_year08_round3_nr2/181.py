#include<string>
#include<fstream>
#include<iostream>
using namespace std;

bool isSeven(string x)
{
}

bool isTwo(string x)
{
}

bool isThree(string x)
{
}

bool isFive(string x)
{
}

long long num[20][20];
string x;
int n;
int L;
long long sum;

void Find(long long add,int start)
{
    if(start>=L){
        if(add<0)
            add *= -1;
        if(add%2==0)
            sum++;
        else if(add%3==0)
            sum++;
        else if(add%5==0)
            sum++;
        else if(add%7==0)
            sum++;
        return;
    }
    for(int i=start;i<L;i++)
    {
        Find(add+num[start][i],i+1);
        if(start!=0)
           Find(add-num[start][i],i+1);
    }
}


int main()
{
    ifstream FIN("input.txt");
    ofstream FOUT("output.txt");
    FIN >> n;
    for(int Case=1;Case<=n;Case++)
    {
        FIN >> x;
        L=x.length();
        for(int i=0;i<L;i++)
        {
            for(int j=i;j<L;j++)
            {
                num[i][j]=0;
                for(int k=i;k<=j;k++)
                    num[i][j] = num[i][j]*10 + x[k] - '0';
            }
        }
        /* for(int i=0;i<L;i++)
        {
            for(int j=0;j<L;j++)
                cout <<  num[i][j] << " ";
            cout << endl;
        } */
        sum=0;
        Find(0,0);
        FOUT << "Case #" << Case << ": " << sum << endl; 
        //cin >> L;
    }  
}
