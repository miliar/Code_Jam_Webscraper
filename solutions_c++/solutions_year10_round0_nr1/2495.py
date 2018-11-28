using namespace std;

#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<fstream>


int main()
{
    int N,K,state[30],cc=0,num,k,round,i;       
    ofstream myfile;
    ifstream myin;
    myin.open("Alarge.in");
    myfile.open("biganswern.txt");
    myin>>num;
    while(num>0)
    {           
                for(i=0;i<30;i++)
                state[i]=0;                
                ++cc;
                myin>>N>>K;
                k=K;
                round=0;
                while(round<N)
                {
                           state[round++]=k%2;
                           k=k/2;
                           }
                           for(i=0;((i<N)&&(state[i]==1));i++);
                           if(i==N)
                           myfile<<"Case #"<<cc<<": ON"<<endl;
                           else
                           myfile<<"Case #"<<cc<<": OFF"<<endl;
                           num--;
                           
                    }
                    myin.close();
                    myfile.close();
    getch();
    return 0;
}
