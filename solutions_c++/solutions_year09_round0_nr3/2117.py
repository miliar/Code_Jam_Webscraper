#include <stdio.h>
#include <string.h>

void filter_line(char *io)
{
    char *place = io;
    char *iter = io;

    while (*iter != 'w')
        ++iter;

    while (*iter) {
        switch (*iter) {
        case 'a':
        case ' ':
        case 'c':
        case 'e':
        case 'd':
        case 'j':
        case 'm':
        case 'l':
        case 'o':
        case 't':
        case 'w':
            *place = *iter;
            ++place;
            break;
        }
        ++iter;
    }
    *place = '\0';

    while (place >= io && *place != 'm') {
        *place = '\0';
        --place;
    }
}

/* 2m 9.458s at the first moment
 * 2m14.365s after adding line_end & pattern_end
 * 2m 7.782s after moving line_end & parrent_end to globals
 */
const char* line_end;
const char* pattern_end;

void count(const char* line,
           const char* pattern,
           int* accumulator)
{
    if (line_end - line < pattern_end - pattern)
        return;

    if (*pattern == '\0') {
        *accumulator += 1;
        return;
    }

    const char* next_line = line;
    while (next_line = strchr(next_line, pattern[0])) {
        count(next_line+1, pattern+1, accumulator);
        next_line++;
    }
}

int main(int, char**)
{
    int total_lines;
    scanf("%i\n", &total_lines);
    // TODO input validation?

    const char* pattern = "welcome to code jam";
    pattern_end = pattern+strlen(pattern);
    for (int iteration = 0; iteration < total_lines; ++iteration) {
        char line[512];

        fgets(line, sizeof(line), stdin);
        filter_line(line);

        line_end = line+strlen(line);
        int accumulator = 0;

        count(line, pattern, &accumulator);
        printf("Case #%i: %4.4i\n", iteration+1, accumulator % 10000);
    }
    return 0;
}

/* vim:set tabstop=4 softtabstop=4 shiftwidth=4 expandtab: */
