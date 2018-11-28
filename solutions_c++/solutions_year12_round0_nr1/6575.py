#include<stdio.h>
#include<string.h>
#include<fstream.h>
#include<iostream.h>
void translate( char * str, char table[])
{

    int len=strlen(str);
    int i;

    for(i=0;i<len;i++)
    {
        if(str[i]!=' ')
        str[i]=table[str[i]-97];
    }


}


main()
{
    ifstream inpfile("input1.in");
    ofstream outfile("output.txt");
    int caseno=1,count=0;
    char array[1000];
    char table[]={"yhesocvxduiglbkrztnwjpfmaq"};

     if (inpfile.is_open())
      {
        while ( inpfile.good())
        {

          inpfile.getline (array,1000);
          if (count!=0)
          {
              translate(array,table);
              outfile<<"Case #"<<caseno<<": "<<array<<endl;
              caseno++;
          }
          count++;
        }


      }



}
