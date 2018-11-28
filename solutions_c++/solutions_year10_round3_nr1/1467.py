# include<iostream.h>
# include <fstream.h>

int main()
{
  ifstream inputFile("A.in", ios::in);
  ofstream outputFile("A.out", ios::out);

int t,n;
  inputFile >> t;

    for ( int i = 1 ; i <= t ; i++ )
    {
       int min=1,max=1;
       int a,b;
       inputFile >> n;
       int count=0;
      for ( int j = 1 ; j <= n ; j++ )
    {
      inputFile >> a;
      inputFile >> b;
      if(j==1)
      {
          min =a;
          max =b;
      }
      else
      if(min < a && b < max )
      {
          ++count ;
      }
      else
       if(min > a && b < max )
      {
          count =2*count;
      }
      else
       if(min < a && b > max )
      {
          count = count *2;
      }
      else
       if(min > a && b > max )
      {
          count = count *2 +1;
      }
    }
    outputFile << "Case #" << i << ": " <<count <<"\n";
    }
     inputFile.close();
    outputFile.close();
}

