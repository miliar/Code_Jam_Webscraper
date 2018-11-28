

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
        int j = 0;
        while(_buffer[j] != 0) {
            unsigned int idx = (unsigned int)(_buffer[j] - 'a');
            if (idx < 26) _buffer[j] = _trans[idx];
            ++j;
        }
        
        _buffer[j] = 0;
        
        while (j > 0) {
            --j;
            if (_buffer[j] > 32) break;
            _buffer[j] = 0;
        }
        printf("Case #%d: %s\n", (i + 1), _buffer);
        
    }
    
    
    return 0;
}





