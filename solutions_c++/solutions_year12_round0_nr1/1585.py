#include <fstream>
#include <iostream>

char map[] = {
    "yhesocvxduiglbkrztnwjpfmaq"
};

int main(int argc, char *argv[]) {
    FILE *f = fopen(argv[1], "r");
    FILE *fout = fopen("out.txt", "w");
    int count = 0;
    for (;;) {
        char ch;
        int len = fread(&ch, sizeof(ch), 1, f);
        if (len == 0) {
            break;
        }
        if (ch == '\r') {
            continue;
        }
        if (ch == '\n') {
            break;
        }
        count = count * 10 + (ch - '0');
    }
    for (int i = 1; i <= count; ++i) {
        fprintf(fout, "Case #%d: ", i);
        for (;;) {
            char ch;
            int len = fread(&ch, sizeof(ch), 1, f);
            if (len == 0) {
                break;
            }
            if (ch == '\r') {
                continue;
            }
            if (ch == '\n') {
                break;
            }
            if (ch != ' ') {
                ch = map[ch - 'a'];
            }
            fprintf(fout, "%c", ch);
        }
        fprintf(fout, "\r\n");
    }
    fclose(fout);
}
