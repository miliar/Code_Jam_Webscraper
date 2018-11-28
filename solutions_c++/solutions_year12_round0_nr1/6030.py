//David Israel García Alcázar
//ID_codeoverflow
//Speaking in tongues google code jam

#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

int main()
{
    char dict[25][2];
    dict[0][0] = 'a';
    dict[0][1] = 'y';
    
    dict[1][0] = 'b';
    dict[1][1] = 'h';
    
    dict[2][0] = 'c';
    dict[2][1] = 'e';
    
    dict[3][0] = 'd';
    dict[3][1] = 's';
    
    dict[4][0] = 'e';
    dict[4][1] = 'o';
    
    dict[5][0] = 'f';
    dict[5][1] = 'c';
    
    dict[6][0] = 'g';
    dict[6][1] = 'v';
    
    dict[7][0] = 'h';
    dict[7][1] = 'x';
    
    dict[8][0] = 'i';
    dict[8][1] = 'd';
    
    dict[9][0] = 'j';
    dict[9][1] = 'u';
    
    dict[10][0] = 'k';
    dict[10][1] = 'i';
    
    dict[11][0] = 'l';
    dict[11][1] = 'g';
    
    dict[12][0] = 'm';
    dict[12][1] = 'l';
    
    dict[13][0] = 'n';
    dict[13][1] = 'b';
    
    dict[14][0] = 'o';
    dict[14][1] = 'k';
    
    dict[15][0] = 'p';
    dict[15][1] = 'r';
    
    dict[16][0] = 'q';
    dict[16][1] = 'z';
    
    dict[17][0] = 'r';
    dict[17][1] = 't';
    
    dict[18][0] = 's';
    dict[18][1] = 'n';
    
    dict[19][0] = 't';
    dict[19][1] = 'w';
    
    dict[20][0] = 'u';
    dict[20][1] = 'j';
    
    dict[21][0] = 'v';
    dict[21][1] = 'p';
    
    dict[22][0] = 'w';
    dict[22][1] = 'f';
    
    dict[23][0] = 'x';
    dict[23][1] = 'm';
    
    dict[24][0] = 'y';
    dict[24][1] = 'a';
    
    dict[25][0] = 'z';
    dict[25][1] = 'q';
    
    ifstream in("texto.in");
    ofstream out("speaking_in_tongues.out");
    
    
    int cases = 0, i = 0, len = 0;
    char st[200];
    
    //scanf("%d",&cases);
    //fgets(st,100,stdin);
    in>>cases;
    in.getline(st,200);
    len = strlen(st);
          
    
    for(i = 0; cases > i; i++)
    {
		  //fgets(st,100,stdin);
		  in.getline(st,200);
		  len = strlen(st);	
          //printf("Case #%d: ",i+1);
          out<<"Case #"<<i+1<<": ";
          for(int j = 0; j < len; j++)
          {
                  if(st[j] != ' ')
                  {
                          for(int k = 0; k < 26; k++)
                          {
                                        if(dict[k][0] == st[j])
                                        {
                                                      //printf("%c",dict[k][1]);
                                                      out<<dict[k][1];
                                                      break;
                                        }
                          }
                  }
                  else
					  out<<" "; 	
                      //printf(" ");
          }
          //printf("\n");
          out<<"\n";
          
          
    }
    
    return 0;
}

