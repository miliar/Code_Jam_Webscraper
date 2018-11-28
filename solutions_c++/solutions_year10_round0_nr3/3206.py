#include<iostream>
#include<vector>
#include<string>
#include<queue>
#include<fstream>

#define FILE "input.txt"
#define OUTPUT_FILE "output.txt"

using namespace std;

ifstream in;
ofstream out(OUTPUT_FILE);

int main()
{
in.open(FILE);
int t;
in>>t;

for(int i=0;i<t;i++)
{
        int money = 0;
        
        int r,k,n;
        queue<int> Q;
        queue<int> Q_riding;
        
        in>>r; in>>k; in>>n;
        
        int temp;
        for(int j=0;j<n;j++)
                {
                            in>>temp;
                            Q.push(temp);
                }
        
        //Algorithm
                                
        for(int j=0;j<r;j++)
        {
                int left = k;
                
                while( !Q.empty() && left>=Q.front()){
                                   int next = Q.front();
                                   Q.pop();
                                   Q_riding.push(next); 
                                   
                                   left -= next;
                                   money += next;
                }
                
                while(!Q_riding.empty())
                                       {
                                         Q.push(Q_riding.front()); Q_riding.pop();
                                       }
        }
        
        out<<"Case #"<<i+1<<": "<<money<<endl;
        
}


system("Pause");
return 0;
}
