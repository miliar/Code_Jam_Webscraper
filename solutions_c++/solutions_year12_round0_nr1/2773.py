#include <iostream>
#include <stdio.h>
#include <string.h>
/*

e, o
j, u
p, r
m, l
y, a
s, n
l, g
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand

rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities

de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
*/
static const char dict[] = {
    'y', //a
    'h', //b
    'e', //c
    's', //d
    'o', //e
    'c', //f
    'v', //g
    'x', //h
    'd', //i
    'u', //j
    'i', //k
    'g', //l
    'l', //m
    'b', //n
    'k', //o
    'r', //p
    'z', //q
    't', //r
    'n', //s
    'w', //t
    'j', //u
    'p', //v
    'f', //w
    'm', //x
    'a', //y
    'q', //z
};
int main(int argc, char *argv[])
{
    int N;
    scanf("%d\n", &N);
    for (int i = 1; i <= N; ++i) {
        printf("Case #%d: ", i);
        char buf[128];
        std::cin.getline(buf, 128);
        const int size = strlen(buf);
        for (int j = 0; j < size; j++) {
            if (buf[j] == ' ')
                printf(" ");
            else
                printf("%c", dict[buf[j]-'a']);
        }
        printf("\n");
    }
    return 0;
}
