#include <stdio.h>
#include <algorithm>
#include <string>
using namespace std;

void clear0(string *s)
{
    string::iterator iter = (*s).begin();
    
    while (*iter == '0')
        iter++;

    (*s).erase((*s).begin(),iter);    
}
        

int main()
{
    FILE *in,*out;
    int T,casen,i,j,k,len;
    char c;
    string::iterator iter;
    
    in = fopen("in.txt","r");
    out = fopen("out.txt", "w");
    
    fscanf(in,"%d\n", &T);
    
    for (casen = 1; casen <= T; casen++) {
        string a;
        while (c = fgetc(in)) {
            if (c == '\n' || c == EOF)
                break;
            a.push_back(c);
        }
        
        string b = a;
        len = a.length();
        next_permutation(a.begin(),a.end());  
         
        clear0(&a);
       //clear0(&b);
        
        fprintf(out,"Case #%d: ", casen);
        
        if (a.compare(b) > 0) {
            for (iter = a.begin(); iter < a.end(); iter++)
                fprintf(out,"%c",*iter);
        }
        else {
            a.insert(1,len+1 - a.length(),'0');
            for (iter = a.begin(); iter < a.end(); iter++)
                fprintf(out,"%c",*iter);
            
                
        }
        fprintf(out,"\n");
    }
    
    fclose(in);
    fclose(out);
    //getchar();
}
