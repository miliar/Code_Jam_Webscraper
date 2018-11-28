#include <stdio.h>

int num[19];
void add(int a, int b)
{
    num[a] = (num[a] + num[b]) % 10000;
}
int main()
{
    int T,casen,i,j,k;
    char c;
    
    FILE *in, *out;
    in = fopen("in.txt", "r");
    out = fopen("out.txt","w");
    
    fscanf(in, "%d\n", &T);
    for (casen = 1; casen <= T; casen++) {
        
        for (i=0; i<19; i++)
            num[i] = 0;
        while (EOF != (c = fgetc(in))) {
            if (c == '\n' || c == '\0')
                break;
            switch (c) {
                case 'w' :
                    num[0] = (num[0]+1)%10000; break;
                case 'e' :
                    add(1,0);
                    add(6,5);
                    add(14,13);  break;
                case 'l' :
                    add(2,1); break;
                case 'c' :
                    add(3,2);
                    add(11,10);
                    break;
                case 'o' :
                    add(4,3);
                    add(9,8);
                    add(12,11); 
                  /*  num[4] += num[3];
                    num[9] += num[8]; 
                    num[12] += num[11];*/ break;
                case 'm' :
                    add(5,4);
                    add(18,17); 
                  /*  num[5] += num[4]; 
                    num[18] += num[17];*/ break;
                case ' ' :
                    add(7,6);
                    add(10,9);
                    add(15,14); 
                 /*   num[7] += num[6];
                    num[10]+= num[9]; 
                    num[15] += num[14];*/ break;
                case 't' :
                    add(8,7); 
                    /*num[8] += num[7]; */break;
                case 'd':
                    add(13,12); 
                   /* num[13] += num[12];*/ break; 
                case 'j':
                    add(16,15); 
                    /*num[16] += num[15];*/ break;
                case 'a' :
                add(17,16);
                    /*num[17] += num[16];*/ break; 
            }
                     
                 
        }
        
        fprintf(out,"Case #%d: %04d\n",casen,num[18]);
    }
    
    fclose(in);
    fclose(out);
   // getchar();
}
