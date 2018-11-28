

#include <stdio.h>
#include <stdlib.h>


enum {
    BUF_LEN = (1024 * 1024)
};




char _buffer[BUF_LEN];

const char _trans[] = {
    'y',//a
    'h',//b
    'e',//c
    's',//d
    'o',//e
    'c',//f
    'v',//g
    'x',//h
    'd',//i
    'u',//j
    'i',//k
    'g',//l
    'l',//m
    'b',//n
    'k',//o
    'r',//p
    'z',//q
    't',//r
    'n',//s
    'w',//t
    'j',//u
    'p',//v
    'f',//w
    'm',//x
    'a',//y
    'q'//z
        
};

int 
main(int argc, const char **argv)
{
    FILE *f = fopen(argv[1], "r");
    
    fgets(_buffer, BUF_LEN, f);
    
    char *tmp;
    int tests = (int)strtol(_buffer, &tmp, 10);
    for (int i = 0; i < tests; ++i) {
        fgets(_buffer, BUF_LEN, f);
        
        int max_r = 0;
        int max_s = 0;
        
        int N = (int)strtol(_buffer, &tmp, 10);
        while (tmp[0] < 33) ++tmp;
        int s = (int)strtol(tmp, &tmp, 10);
        while (tmp[0] < 33) ++tmp;
        int p = (int)strtol(tmp, &tmp, 10);
        
        
        int j;
        
        for (j = 0; j < N; ++j) {
            while (tmp[0] < 33) ++tmp;
            int sc = (int)strtol(tmp, &tmp, 10);
            int l_r, l_s;
            
            if (sc > 28) {
                l_r = l_s = 10;
            } else if (0 == sc) {
                l_r = l_s = 0;
            } else {
                l_r = ((sc + 2) / 3);
                l_s = ((sc + 4) / 3);
            }
            if (l_r >= p) {
                ++max_r;
            } else if (l_s >= p) ++max_s;
        }
        
        if (max_s > s) max_s = s;
        
        
        printf("Case #%d: %d\n", (i + 1), (max_r + max_s));
        
    }
    
    
    return 0;
}





