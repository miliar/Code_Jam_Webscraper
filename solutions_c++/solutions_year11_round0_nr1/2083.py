#include <QtCore/QCoreApplication>
#include <cstdio>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    if(argc < 3)
        return 1;
    FILE* in = fopen(argv[1], "r");
    FILE* out = fopen(argv[2], "w");

    int T,N,time,saved,O,B,curBut;
    char last,curBot;
    fscanf(in, "%d", &T);
    for(int t=0; t<T; t++){
        fscanf(in, "%d", &N);
        time = 0;
        saved = 0;
        last = 'G';
        O = 1;
        B = 1;
        for(int n=0; n<N; n++){
            fscanf(in," %c %d", &curBot, &curBut);
            int dist = 0;
            if(curBot == 'O'){
                dist = qAbs(curBut - O);
                O = curBut;
            }else{
                dist = qAbs(curBut - B);
                B = curBut;
            }
            if(curBot != last){
                dist = qMax((dist - saved),0);
                saved = 0;
            }
            dist++;
            last = curBot;
            saved += dist;
            time += dist;
        }
        fprintf(out, "Case #%d: %d\n", t+1, time);
    }

    return 0;
}
