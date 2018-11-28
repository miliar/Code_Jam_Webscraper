#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
int main()
{
    FILE *fpr,*fpw;
    fpr=fopen("A-small-attempt1.in","rb");
    fpw=fopen("out.txt","wb");

    int T,Case,i;
    char m[120];
    fscanf(fpr,"%d",&T);
    fgetc(fpr);
    cout<<T<<endl;
    for(Case=1;Case<=T;Case++)
    {
        //cout<<Case<<endl;
        fgets(m,102,fpr);
        //cout<<m;
        i=0;
        char te;
        fprintf(fpw,"Case #%d: ",Case);
        while(m[i]!='\0')
        {
            te=m[i];
            //ÒÑÆÆÒëµÄÖÃ»»±í
            if     (te=='e'){fprintf(fpw,"o");}
            else if(te=='p'){fprintf(fpw,"r");}
            else if(te=='m'){fprintf(fpw,"l");}
            else if(te=='y'){fprintf(fpw,"a");}
            else if(te=='s'){fprintf(fpw,"n");}
            else if(te=='l'){fprintf(fpw,"g");}
            else if(te=='j'){fprintf(fpw,"u");}
            else if(te=='c'){fprintf(fpw,"e");}
            else if(te=='k'){fprintf(fpw,"i");}
            else if(te=='d'){fprintf(fpw,"s");}
            else if(te=='x'){fprintf(fpw,"m");}
            else if(te=='v'){fprintf(fpw,"p");}
            else if(te=='n'){fprintf(fpw,"b");}
            else if(te=='r'){fprintf(fpw,"t");}
            else if(te=='i'){fprintf(fpw,"d");}
            else if(te=='b'){fprintf(fpw,"h");}
            else if(te=='t'){fprintf(fpw,"w");}
            else if(te=='a'){fprintf(fpw,"y");}
            else if(te=='h'){fprintf(fpw,"x");}
            else if(te=='w'){fprintf(fpw,"f");}
            else if(te=='f'){fprintf(fpw,"c");}
            else if(te=='o'){fprintf(fpw,"k");}
            else if(te=='u'){fprintf(fpw,"j");}
            else if(te=='g'){fprintf(fpw,"v");}
            else if(te=='z'){fprintf(fpw,"q");}
            else if(te=='q'){fprintf(fpw,"z");}
            else fprintf(fpw,"%c",te);
            i++;
        }
    }
    fclose(fpr);
    fclose(fpw);
    return 0;
}
