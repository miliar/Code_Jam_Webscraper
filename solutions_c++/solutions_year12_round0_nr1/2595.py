#include <stdio.h>
#include <stdlib.h>

int nbLignes;

char c;

inline char
translate(char c)
{
  if(c == 'y')
    return 'a';
  if(c == 'n')
    return 'b';
  if(c == 'f')
    return 'c';
  if(c == 'i')
    return 'd';
  if(c == 'c')
    return 'e';
  if(c == 'w')
    return 'f';
  if(c == 'l')
    return 'g';
  if(c == 'b')
    return 'h';
  if(c == 'k')
    return 'i';
  if(c == 'u')
    return 'j';
  if(c == 'o')
    return 'k';
  if(c == 'm')
    return 'l';
  if(c == 'x')
    return 'm';
  if(c == 's')
    return 'n';
  if(c == 'e')
    return 'o';
  if(c == 'v')
    return 'p';
  if(c == 'z')
    return 'q';
  if(c == 'p')
    return 'r';
  if(c == 'd')
    return 's';
  if(c == 'r')
    return 't';
  if(c == 'j')
    return 'u';
  if(c == 'g')
    return 'v';
  if(c == 't')
    return 'w';
  if(c == 'h')
    return 'x';
  if(c == 'a')
    return 'y';
  if(c == 'q')
    return 'z';
}

int
main()
{
  int countCar = 0;
  scanf("%d", &nbLignes);
  for(int ligne = 1; ligne <= nbLignes; ligne++)
    {
      countCar = 0;
      printf("Case #%d: ", ligne);
      
      while(scanf("%c", &c) == 1)
	{
	  if(c == '\n' && countCar != 0)
	    break;
	  if(c == ' ')
	    printf(" ");
	  
	  else if(c >= 'a' && c <= 'z')
	    printf("%c", translate(c));
	 
	  countCar++;
	}

      printf("\n");
      
    }
  

  return 0;
}
