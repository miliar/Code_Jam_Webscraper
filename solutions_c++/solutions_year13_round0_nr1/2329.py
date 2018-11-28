#include <cstdio>
#include <cstdlib>

char d[4][4];
char a[4];

char check() {
    char sym = 'T';
    for (int i = 0; i < 4; i++) {
        if (a[i] == '.')
            return 'Q';
            
        if (a[i] != sym)
            if (sym == 'T')
                sym = a[i];
            else
                if (a[i] != 'T')
                    return 'Q';
    }
    
    return sym;
}

bool judge(FILE *file, int t) {
    char res;
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++)
            a[j] = d[i][j];
        
        res = check();
        if (res != 'Q') {
            fprintf(file, "Case #%d: %c won\n", t + 1, res);
            return true;
        }
    }
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++)
            a[j] = d[j][i];
        
        res = check();
        if (res != 'Q') {
            fprintf(file, "Case #%d: %c won\n", t + 1, res);
            return true;
        }
    }
    
    for (int j = 0; j < 4; j++)
            a[j] = d[j][j];
        
    res = check();
    if (res != 'Q') {
        fprintf(file, "Case #%d: %c won\n", t + 1, res);
        return true;
    }
        
    for (int j = 0; j < 4; j++)
            a[j] = d[j][3 - j];
        
    res = check();
    if (res != 'Q') {
        fprintf(file, "Case #%d: %c won\n", t + 1, res);
        return true;
    }
    
    return false;
}

void dump() {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++)
            printf("%c", d[i][j]);
        printf("\n");
    }
}

int main() {
    int n;
    
    FILE *fi = fopen("A-large.in", "r");
    FILE *fo = fopen("output.txt", "w");
    
    fscanf(fi, "%d", &n);
    
    for (int t = 0; t < n; t++) {
        bool isfull = true;
        
        char c;
        int cnt = 0;
        while (cnt < 16) {
            if (fscanf(fi, "%c", &c) == 0)
                break;
            if (c == '.' || c == 'T' || c == 'O' || c == 'X') {
                d[cnt / 4][cnt % 4] = c;
                cnt++;
            }
            else
                continue;
            if (c == '.')
                isfull = false;
            
        }
                
        if (judge(fo, t))
            continue;
        else
            if (!isfull)
                fprintf(fo, "Case #%d: Game has not completed\n", t + 1);
            else
                fprintf(fo, "Case #%d: Draw\n", t + 1);
    }
    
    fclose(fi);
    fclose(fo);
    
    return 0;
}
