#include<iostream>
#include<string>
#include<fstream>

using namespace std;
void check();

int main()
{
 check();
 return 0;
}

void check()
{
 int count;

  int L,D,N;
  ofstream fout;
 fout.open("output.txt");


 ifstream fin;
 fin.open("A-large.in");
 fin>>L>>D>>N;
 //cout<<"Enter the input";
 
 string s[D];  //it contains the dictionary words
 string s1[N];  // it contains the test cases
 
 for(int i=0;i<D;i++)
 fin>>s[i];
 for(int j=0;j<N;j++)
 fin>>s1[j];


 for(int i=0;i<N;i++) 
 {count=0;
  string temp[L];
  int m=0;
  
  for(int z=0;z<L;z++)
  {     if(s1[i][m]=='(')
    {
      for(m++;s1[i][m]!=')';m++)
      temp[z].push_back(s1[i][m]);
      m++;      
    }
    else
    temp[z].push_back(s1[i][m++]);
   //  cout<<temp[z];  
  }   

  for(int j=0;j<D;j++)
  {int flag=1;
   for(int k=0;k<L;k++)
   { int flag1=0;
      for(int u=0;u<temp[k].length();u++)
       if(temp[k][u]==s[j][k])
	flag1=1;
   if(!flag1)
  flag=0;
   }   
 if(flag)
count++;
  }
fout<<"Case #"<<i+1<<": "<<count<<"\n"; 
 }

}

