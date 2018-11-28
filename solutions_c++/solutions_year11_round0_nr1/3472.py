//*** Problem A - Bot Trust
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int findNextBotInd(char);

int T,N, Pos[100];     
char Bot[100];
int O_at, O_ind, B_at, B_ind, s, ind, gotoNextInd;



int main()
{

string line;     
ifstream fin ("input.in");
ofstream fout ("output");

fin>>line; //No. of test cases
cout<<line;
T = atoi(line.c_str());
for (int i=0;i<T;i++)
{
  fin>>line; //No. of buttons to press
  N = atoi(line.c_str());
  for(int j=0; j<N ; j++)
  {
    fin>>Bot[j];
    cout<<"Bot: "<<Bot[j];//TODELETE  
    fin>>line;
    Pos[j]=atoi(line.c_str());
    cout<<" Button: "<<Pos[j]<<endl;//TODELETE
  }            
   
  s=0; ind=0; gotoNextInd=0;
  O_at=1; B_at=1;    
  
  O_ind = findNextBotInd('O');
  cout<<O_ind;
  B_ind = findNextBotInd('B');
  cout<<B_ind;  
  
  
  while (ind<N)
  {
   if (O_ind<100)     
    if (O_at!=Pos[O_ind]) O_at+=(Pos[O_ind]>O_at)?1:-1;  
    else if (O_ind == ind)
         {
           gotoNextInd=1;
           ind++;
           O_ind = findNextBotInd('O');
           ind--;
         }
   if (B_ind<100)             
    if (B_at!=Pos[B_ind]) B_at+=(Pos[B_ind]>B_at)?1:-1;
    else if (B_ind == ind)
         {
           gotoNextInd=1;
           ind++;
           B_ind = findNextBotInd('B');
           ind--;
         }
    
    if (gotoNextInd == 1) 
    {
      ind++;
      gotoNextInd=0;
    }

    s++;       
  }
  
   fout<<"Case #"<<i+1<<": "<<s<<endl;
   cout<<"SOLUTION: "<<s<<endl;
}

fin.close();
fout.close();

system("pause");

 }

int findNextBotInd(char c)
{
    for(int i=ind;i<N;i++)
    if (Bot[i] == c) return(i);
    return(100);//non existent number
}
