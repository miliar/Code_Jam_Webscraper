#include <iostream>
#include <fstream>
#include <stdlib>
using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("A.out");
    char SE[100][101];
    char query[101];
    char temp[101];
    int OK[100];
    int number;
    int N,S,Q,X,Y;
    int i,j,k;
    
    in.getline(temp,101);
    N=atoi(temp);
    for (X=1; X<=N; X++)
    {
        number=0;
        Y=0;
        in.getline(temp,101);
        S=atoi(temp);        
        for (i=0; i<S; i++)
        {
            in.getline(SE[i],101);
            OK[i]=0;
        }
        in.getline(temp,101);
        Q=atoi(temp);
        for (i=0; i<Q; i++)
        {
            in.getline(query,101);
            for (j=0; j<S; j++)
            {
                if (strcmp(query,SE[j])==0)
                {
                    if (OK[j]==0)
                    {
                        OK[j]=1;
                        number++;
                        if (number==S)
                        {
                            for (k=0; k<S; k++)
                                OK[k]=0;
                            OK[j]=1;
                            number=1;
                            Y++;
                        }
                    }
                    break;
                }
            }
        }        
        out<<"Case #"<<X<<": "<<Y<<endl;
    }
	return 0;
}