#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  int n1,n2,n3;
  
  ifstream in;
  in.open("A-small-attempt3.in",ios::in);
  ofstream out;
  out.open("out",ios::out);

  in>>n1>>n2>>n3;
  
  char ch[n2][n1];
  for (int i=0; i<n2; i++)
    for (int j=0; j<n1; j++)
    in>>ch[i][j];
  
  int val[n3][n2][n1];
  for (int j=0;j<n3; j++)
    for (int k=0; k<n2; k++)
      for (int n=0; n<n1; n++)
	val[j][k][n]=0;
  
  for (int l=0; l<n3; l++){
  string s;
  in>>s;

  int i=0, loc=0;

   
   while (s[i]!='\0'){
     if (s[i] == '('){
       while (s[i]!=')'){
	 if (s[i] == '\0'){
	   out<<"error";
	   return 0;
	 }
       for (int j=0; j<n2; j++){
	 if (s[i]==ch[j][loc])
	   val[l][j][loc]=1;
       }
       i++;
     }
    }
    else{
      for (int j=0; j<n2; j++){
       if (s[i]==ch[j][loc])
	 val[l][j][loc]=1;
      }
    }
    i++;
    loc++;
   }
  }
  
  int output[n3];
  for (int i=0;i<n3;i++)
    output[i]=0;
  for (int i=0; i<n3; i++){
    for (int j=0; j<n2; j++){
      int cnt=0;
      for (int k=0; k<n1; k++)
	if (val[i][j][k]==1)
	  cnt++;
	if (cnt==n1)
	  output[i]++;
    }
    out<<"Case #"<<i+1<<": "<<output[i]<<endl;
  }

  return 0;
}