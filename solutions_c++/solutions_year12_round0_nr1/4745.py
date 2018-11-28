#include <cstdlib>
#include <iostream>

using namespace std;

char mapp(char c)
{
    if(c == 'a')
    return 'y';
    if(c == 'b')
    return 'h';
    if(c == 'c')
    return 'e';
    if(c == 'd')
    return 's';
    if(c == 'e')
    return 'o';
    if(c == 'f')
    return 'c';
    if(c == 'g')
    return 'v';
    if(c == 'h')
    return 'x';
    if(c == 'i')
    return 'd';
    if(c == 'j')
    return 'u';
    if(c == 'k')
    return 'i';
    if(c == 'l')
    return 'g';
    if(c == 'm')
    return 'l';
    if(c == 'n')
    return 'b';
    if(c == 'o')
    return 'k';
    if(c == 'p')
    return 'r';
    if(c == 'q')
    return 'z';
    if(c == 'r')
    return 't';
    if(c == 's')
    return 'n';
    if(c == 't')
    return 'w';
    if(c == 'u')
    return 'j';
    if(c == 'v')
    return 'p';
    if(c == 'w')
    return 'f';
    if(c == 'x')
    return 'm';
    if(c == 'y')
    return 'a';
    //if(c == 'z')
    return 'q';
}


int main(int argc, char *argv[])
{
    FILE *fin  = fopen ("A-small-attempt0.in", "r");
	FILE *fout = fopen ("A-small-attempt0.out", "w"); 
	
	int t;
	int ll = 0;
    char c;
	fscanf(fin,"%d",&t);
	fscanf(fin,"%c",&c);
	//for(int i=0;i<t;i++)
	//{
        
        int bji = 1;
        int tt = 1;
        //fprintf(fout,"Case #%d: ",tt);
        
        while(1)
        {
            if(ll == t)
        break;
        fscanf(fin,"%c",&c);
        //printf("%c",c);
            if(bji == 1)
            {
                fprintf(fout,"Case #%d: ",tt);
                //cout<<"Case #%d: ";
                bji = 0;
            }
            
        
        if(c>='a' && c<='z')
        {
            char cc = mapp(c);
            fprintf(fout,"%c",cc);
            //printf("%c",cc);
        }
        if(c== ' ')
        {
            //char cc = mapp(c);
            fprintf(fout,"%c",c);
            //printf("%c",c);
        }
        if(c== '\n')
        {
            //printf("%c",c);
           // cout<<"ok"<<endl;
            ll++;
            //char cc = mapp(c);
            fprintf(fout,"%c",c);
            bji = 1;
            tt++;
            //fprintf(fout,"Case #%d: ",tt);
        }
    }
        
        
   // }
	
    //system("PAUSE");
    return EXIT_SUCCESS;
}
