//welcome to code jam
//0123456789012345678
#include<iostream>
#include<fstream>
#include<string>

int mat[19];

void add(char c)
{
  switch(c)
  {
    case 'w':  mat[0]++;
               break;
    case 'e':  mat[1]+=mat[0];
               mat[6]+=mat[5];
               mat[14]+=mat[13];
               break;
    case 'l':  mat[2]+=mat[1];
               break;
    case 'c':  mat[3]+=mat[2];
               mat[11]+=mat[10];
               break;
    case 'o':  mat[4]+=mat[3];
               mat[12]+=mat[11];
               mat[9]+=mat[8];
               break;
    case 'm':  mat[5]+=mat[4];
               mat[18]+=mat[17];
               break;
    case ' ':  mat[7]+=mat[6];
               mat[10]+=mat[9];
               mat[15]+=mat[14];
               break;
    case 't':  mat[8]+=mat[7];
               break;
    case 'd':  mat[13]+=mat[12];
               break;
    case 'j':  mat[16]+=mat[15];
               break;
    case 'a':  mat[17]+=mat[16];
               break;
  }
  for(int i=0;i<=18;i++)
  {
    mat[i]=mat[i]%10000;
  }
}

using namespace std;
int main()
{ 
  int n;
  ifstream fin("input.in");
  ofstream fout("output.out");
  fin>>n;
  string line;
  getline(fin,line);
  for(int t=1;t<=n;t++)
  {
    memset(mat,0,sizeof(mat));
    getline(fin,line);
    for(int i=0;i<line.length();i++)
    {
      add(line[i]);
    }
    int ans[4];
    for(int i=0;i<4;i++)
    {
      ans[i]=mat[18]%10;
      mat[18]/=10;
    }
    fout<<"Case #"<<t<<": "<<ans[3]<<ans[2]<<ans[1]<<ans[0]<<endl;
  }
  system("pause");
  return 0;
}
