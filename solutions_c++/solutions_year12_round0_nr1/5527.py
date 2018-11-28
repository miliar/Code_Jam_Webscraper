    #include <iostream>
    #include <fstream>
    #include <string>
    #include <stdio.h>
    using namespace std;
    
    int main () {
      int i,count,x,pos,len;
      x=0;
      short int cases=0;
      pos=0;
      char line[101],text[101],arr[10000];
      ifstream myfile ("blah.txt");
      while(myfile)
      {
          myfile.get(arr[x]);
          //cout<<arr[x];
          x++;
      }
      while(arr[pos] != '\n')
    	{
    		cases=(cases*10) + (arr[pos] - '0');
    		pos++;
    	}
               count=1;
                       while(cases--)
                       {
                                     len=0;
    	                             if(arr[pos] == '\n')
    		                         pos++;
    	                             while(arr[pos] != '\n' && arr[pos] != '\0' && pos != x)
                                         text[len++] = arr[pos++];
    	                             text[len++] = '\0';
                             i=0;
                             while(text[i]!='\0')
                             {
                                                 switch(text[i])
                                                 {
                                                                
                                                         case 'a' : line[i]='y';
                                                                    i++;
                                                                    break;
                                                         case 'b' : line[i]='h';
                                                                    i++;
                                                                    break;
                                                         case 'c' : line[i]='e';
                                                                    i++;
                                                                    break;
                                                         case 'd' : line[i]='s';
                                                                    i++;
                                                                    break;
                                                         case 'e' : line[i]='o';
                                                                    i++;
                                                                    break;
                                                         case 'f' : line[i]='c';
                                                                    i++;
                                                                    break;
                                                         case 'g' : line[i]='v';
                                                                    i++;
                                                                    break;
                                                         case 'h' : line[i]='x';
                                                                    i++;
                                                                    break;
                                                         case 'i' : line[i]='d';
                                                                    i++;
                                                                    break;
                                                         case 'j' : line[i]='u';
                                                                    i++;
                                                                    break;
                                                         case 'k' : line[i]='i';
                                                                    i++;
                                                                    break;
                                                         case 'l' : line[i]='g';
                                                                    i++;
                                                                    break;
                                                         case 'm' : line[i]='l';
                                                                    i++;
                                                                    break;
                                                         case 'n' : line[i]='b';
                                                                    i++;
                                                                    break;
                                                         case 'o' : line[i]='k';
                                                                    i++;
                                                                    break;
                                                         case 'p' : line[i]='r';
                                                                    i++;
                                                                    break;
                                                         case 'q' : line[i]='z';
                                                                    i++;
                                                                    break;
                                                         case 'r' : line[i]='t';
                                                                    i++;
                                                                    break;
                                                         case 's' : line[i]='n';
                                                                    i++;
                                                                    break;
                                                         case 't' : line[i]='w';
                                                                    i++;
                                                                    break;
                                                         case 'u' : line[i]='j';
                                                                    i++;
                                                                    break;
                                                         case 'v' : line[i]='p';
                                                                    i++;
                                                                    break;
                                                         case 'w' : line[i]='f';
                                                                    i++;
                                                                    break;
                                                         case 'x' : line[i]='m';
                                                                    i++;
                                                                    break;
                                                         case 'y' : line[i]='a';
                                                                    i++;
                                                                    break;
                                                         case 'z' : line[i]='q';
                                                                    i++;
                                                                    break;
                                                         case ' ' : line[i]=' ';
                                                                    i++;
                                                                    break;
                                                 }
                             }
                             line[strlen(text)]='\0';
                             puts(line);
                             ofstream fout;
                             fout.open("output.txt",ios::app);
                             fout<<"Case #"<<count<<": "<<line<<"\n";
                             fout.close();
                             count++;
                       }
        myfile.close();
      
     
    //getch();
      return 0;
    }
