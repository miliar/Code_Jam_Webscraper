#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

//const char hello[30]="welcome";
const char hello[30]="welcome to code jam";
unsigned len=strlen(hello);

unsigned count(const char*);

int main()
{
  unsigned num=0;
  cin >> num;
  char buf[1000];
  cin.getline(buf,31);

  for (unsigned i=0; i<num; i++)
  {
    cin.getline(buf,31);
//  cout << buf << endl;
    cout << "Case #" << i << ": ";
    printf("%04d\n",count(buf));
  }  
  return 0;
}

unsigned count(const char *buf)
{
    unsigned total=0, i=0, j=0, table[60][500];
    unsigned newlen=strlen(buf);

/*
    cout << endl;
    cout << hello << " " << len << endl;
    cout << buf << " " << newlen << endl;
*/

    for(i=0; i<newlen; i++)
    for(j=0; i<len; i++) table[i][j]=0;

    unsigned count=0;
    for(i=0; i<newlen; i++)
    {
      if (buf[i]==hello[0]) count++;
      table[0][i]=count;
    }

    for(j=1; j<len; j++) 
    for(i=j; i<newlen; i++)
    {
      table[j][i]=table[j][i-1];
      if (buf[i]==hello[j]) 
      table[j][i]+=table[j-1][i];
      table[j][i]%=1000;
    }

 /*   
    cout << endl << " ";
    for(j=0; j<len; j++) cout << " " << hello[j];

    cout << endl;
    for(j=0; j<newlen; j++)
    {
      cout << buf[j];
      for(i=0; i<len; i++) cout << " " << table[i][j];
      cout << endl;
    }
   
    exit(1);
*/
  
    return table[len-1][newlen-1];
}
