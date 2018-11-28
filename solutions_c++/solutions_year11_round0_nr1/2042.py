#include <cstdio>
#include <cstdlib>
#include <cmath>


int main() {
    int c, n, ins, i, bufferB, bufferO, posB, posO, botao, time, dist;
    char quem;

    scanf("%d", &n);
    for(c=1;c<=n;c++) {
        scanf("%d", &ins);
        bufferB = 0; bufferO = 0;
        posO = 1; posB = 1;
        time = 0;

        for(i=0;i<ins;i++) {
            getchar();scanf("%c %d", &quem, &botao);
            if(quem=='O') {
                dist = posO - botao;
                if(dist < 0) dist = dist * (-1);
                dist-= bufferO;
                if(dist < 0) dist = 0;
                dist++;
                posO = botao;
                bufferO = 0;
                bufferB+= dist;
                time += dist;
            } else {
                dist = posB - botao;
                if(dist < 0) dist = dist * (-1);
                dist -= bufferB;
                if(dist < 0) dist = 0;
                posB = botao;
                dist++;
                bufferB = 0;
                bufferO+= dist;
                time += dist;
            }

        }
        printf("Case #%d: %d\n", c, time);

    }

    return 0;
}
