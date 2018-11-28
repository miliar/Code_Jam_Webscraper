#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    ifstream fil;
    ofstream dd;
    fil.open("E:\\google\\q1\\A-small-attempt0.in");
    dd.open("E:\\google\\q1\\abc.out");
     int n,i,j;
     string abc;
     char ch,str[103];
     fil>>n;
     fil.get(ch);
     for (j=0;j<n;j++)
     { abc="";
         fil.getline(str,102);
     for(i=0;str[i]!='\0';i++)
      { 
              if (str[i]=='a')
                  abc+="y";
               else if (str[i]=='b')
                    abc+="h";
               else if (str[i]=='c')
                    abc+="e";
               else if (str[i]=='d')
                    abc+="s";
               else if (str[i]=='e')
                    abc+="o";
               else if (str[i]=='f')
                    abc+="c";
               else if (str[i]=='g')
                    abc+="v";
               else if (str[i]=='h')
                    abc+="x";
     else if (str[i]=='i')
                    abc+="d";
     else if (str[i]=='j')
                    abc+="u";
     else if (str[i]=='k')
                    abc+="i";
     else if (str[i]=='l')
                    abc+="g";
     else if (str[i]=='m')
                    abc+="l";
     else if (str[i]=='n')
                    abc+="b";
     else if (str[i]=='o')
                    abc+="k";
     else if (str[i]=='p')
                    abc+="r";
     else if (str[i]=='q')
                    abc+="z";
     else if (str[i]=='r')
                    abc+="t";
     else if (str[i]=='s')
                    abc+="n";
     else if (str[i]=='t')
                    abc+="w";
     else if (str[i]=='u')
                    abc+="j";
     else if (str[i]=='v')
                    abc+="p";
     else if (str[i]=='w')
                    abc+="f";
     else if (str[i]=='x')
                    abc+="m";
     else if (str[i]=='y')
                    abc+="a";
     else if (str[i]=='z')
                    abc+="q";
     else
     abc+=" ";
}
dd<<"Case #"<<j+1<<": "<<abc<<endl;
}
    fil.close();
    dd.close();
    return 0;
    
}
    
