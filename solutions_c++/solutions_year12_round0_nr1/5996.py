#include <cstdio>

int main()
{
    // Googlereese mapping
    int googlereese[26];
    googlereese[24]=0;
    googlereese[13]=1;
    googlereese[5]=2;
    googlereese[8]=3;
    googlereese[2]=4;
    googlereese[22]=5;
    googlereese[11]=6;
    googlereese[1]=7;
    googlereese[10]=8;
    googlereese[20]=9;
    googlereese[14]=10;
    googlereese[12]=11;
    googlereese[23]=12;
    googlereese[18]=13;
    googlereese[4]=14;
    googlereese[21]=15;
    googlereese[25]=16;
    googlereese[15]=17;
    googlereese[3]=18;
    googlereese[17]=19;
    googlereese[9]=20;
    googlereese[6]=21;
    googlereese[19]=22;
    googlereese[7]=23;
    googlereese[0]=24;
    googlereese[16]=25;

    int numT;
    int i=1;
    scanf("%d", &numT);    
    char c;
        
    while((c=getchar()) != '\n');

    while(i <= numT)
    {
        printf("Case #%d: ", i);
        
        // Reading every character until the linefeed is met
        while( (c=getchar()) != '\n')
        {
            if(c != ' ')
            {
                putchar('a'+googlereese[c -'a']);
            }
            else
                putchar(' ');
        }
        putchar('\n');
        ++i;
    }
   
    return 0;
}

