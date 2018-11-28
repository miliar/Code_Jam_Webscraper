#include <cstdio>

    char tab[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main2()
{
    while (true)
    {
        char caract = getchar();
        if (caract == '\n' || caract == '\0') break;
        if (caract == ' ') printf(" ");
        else printf("%c", tab[caract - 'a']);
    }
    printf("\n");
    return 0;
}

int main()
{
    int N;
    scanf("%d\n", &N);
    
    for (int i=0; i<N; i++)
    {
        printf("Case #%d: ", i+1);
        main2();
    }
}
