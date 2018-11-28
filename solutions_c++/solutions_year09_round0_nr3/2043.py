#define PSIZE 20
#define DSIZE 510
#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
char *pattern="welcome to code jam";
char data[510];
int occarray[PSIZE][DSIZE];

int get(int patternindex,int dataindex)
{
    int count=0;
    if(occarray[patternindex][dataindex]!=0)
                                             return occarray[patternindex][dataindex];
    else if(patternindex==strlen(pattern))
    {
                                     occarray[patternindex][dataindex]=1;
                                     return 1;
    }
    else
        {
                                     for(int i=dataindex;i<strlen(data);i++)
                                     {
                                             if(pattern[patternindex]==data[i])
                                             {
                                                                               count=(count+get(patternindex+1,i+1))%10000;
                                                                              // cout<<"\n"<<patternindex<<" "<<i<<" "<<count;
                                             }
                                     }
        occarray[patternindex][dataindex]=count%10000;
        //cout<<"\n"<<patternindex<<" "<<dataindex<<" "<<count;
        return occarray[patternindex][dataindex];
        }
}


int main()
{
 
    int i,j,N,k,n;
    ifstream input("input.txt");
    ofstream output("output.txt");
    input>>N;
    input.ignore();
    cout<<N;
    for(k=0;k<N;k++)
    {
    input.getline(data,502);
    for(i=0;i<PSIZE;i++)
    {
                        for(j=0;j<DSIZE;j++)
                        {
                                            occarray[i][j]=0;
                        }
    }
    int temp=get(0,0);
    output<<"Case #"<<(k+1)<<": ";
    if(temp<10)
    output<<"000";
    else if(temp<100)
    output<<"00";
    else if(temp<1000)
    output<<"0";
    output<<temp<<"\n";
    }
    input.close();
    output.close();
    return 0;
}
