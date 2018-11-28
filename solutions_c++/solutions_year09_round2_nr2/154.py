#include <cstdio>
#include <cstddef>
#include <cstring>
#include <algorithm>


const char * processCase(char * line) {
        const size_t len = strlen(line);
        size_t i;
        for(i = len - 2; i > 0 && line[i] >= line[i + 1]; --i);
        
        const size_t k = i;
        size_t j = i + 1;
        for(i = j + 1; i < len; ++i) {
                if( line[k] < line[i] && line[i] <= line[j] )
                        j = i;
        }
        
        std::swap(line[k], line[j]);
        
        for(i = k + 1, j = len - 1; i < j; ++i, --j)
                std::swap(line[i], line[j]);
        
        if( line[0] == '0' )
                return line + 1;
        return line;
}


int main() {
        size_t T;
        scanf("%u\n", &T);
        
        char line[1024];
        for(size_t t = 0; t < T; ++t) {
                line[0] = '0';
                gets(line + 1);
                
                printf("Case #%u: %s\n", t + 1, processCase(line));
        }
        
        return 0;
}