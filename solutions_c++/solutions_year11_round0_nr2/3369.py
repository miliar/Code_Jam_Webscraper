#include <cstdio>
#include <cassert>

char comb[255][255];
bool neg[255][255];

char skipgetc(FILE *f)
{
    char c = fgetc(f);
    while (c == ' ')
        c = fgetc(f);
    return c;
}

class Meduka
{
public:
    char a[100];
    size_t size;

    void reset()
    {
        size = 0;

        for (int i = 0; i < 255; i++)
            for (int j = 0; j < 255; j++)
                comb[i][j] = comb[j][i] = neg[i][j] = neg[j][i] = 0;
    }

    void push(size_t x)
    {
        a[size++] = x;

        if (size == 1)
            return;

        if (comb[a[size - 1]][a[size - 2]])
        {
            a[size - 2] = comb[a[size - 1]][a[size - 2]];
            size--;
        }
        else
            for (int i = 0; i < size - 1; i++)
                if (neg[a[i]][a[size - 1]])
                {
                    size = 0;
                    break;
                }

    }

    void please(FILE *f)
    {
        fprintf(f, "[");
        for (int i = 0; i < size; i++)
        {
            fputc(a[i], f);
            if (i != size - 1)
                fprintf(f, ", ");
        }
        fprintf(f, "]\n");
    }

    ~Meduka()
    {
        printf("Being Meguka is suffering\n");
    }
};

Meduka Meguka;

int main()
{
    FILE *f = fopen("in.txt", "r");
    FILE *fo = fopen("out.txt", "w");
//    FILE *fo = stdout;
    assert(f && fo);

    int n, m;
    fscanf(f, "%d\n", &n);

    for (int i = 0; i < n; i++)
    {
        fprintf(fo, "Case #%d: ", i+1);

        Meguka.reset();

        fscanf(f, "%d", &m);
        for (int j = 0; j < m; j++)
        {
            size_t a = skipgetc(f), b = getc(f);
            size_t c = getc(f);
            comb[a][b] = c;
            comb[b][a] = c;
        }

        fscanf(f, "%d", &m);
        for (int j = 0; j < m; j++)
        {
            size_t a = skipgetc(f), b = getc(f);
            neg[a][b] = neg[b][a] = true;
        }

        fscanf(f, "%d", &m);
        for (int j = 0; j < m; j++)
        {
            Meguka.push(skipgetc(f));
        }

        Meguka.please(fo);
    }

    return 0;
}
