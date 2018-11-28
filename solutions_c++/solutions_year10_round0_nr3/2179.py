#include <stdio.h>
#include <stdlib.h>
#include <deque>

#define INFILENAME "cs.in"
#define OUTFILENAME "cs.out"
using namespace std;

class Data{
public:
    int rotate;
    int seat;
    int group;
    int *people;
};

class Env{
public:
    int testcase;
    Data *data;
    char *inname, *outname;

    int init(char *, char *);
    int exec();
};

int Env::init(char *in, char *out){
    FILE *fin;

    inname = in;
    outname = out;

    fin = fopen(inname,"r");
    if(fin == NULL){
        printf("cant open\n");
        return 0;
    }

    fscanf(fin, "%d\n", &testcase);
    data = new Data[testcase];
    for(int i=0;i<testcase;i++){
        fscanf(fin, "%d %d %d\n", &data[i].rotate, &data[i].seat, &data[i].group);
        data[i].people = new int[data[i].group];
        for(int k=0;k<data[i].group;k++){
            fscanf(fin, "%d ", &data[i].people[k]);
        }
    }
    
    fclose(fin);
}

int Env::exec(){
    FILE *fout;
    int remain;
    int num;
    uint money;
    deque<int> que;

    fout = fopen(outname, "w");
    if(fout == NULL){
        printf("cant open\n");
        return 0;
    }

    for(int i=0;i<testcase;i++){
        //printf("[%d] %d %d %d\n", i,data[i].rotate, data[i].seat, data[i].group);
        for(int k=0; k<data[i].group; k++)
            que.push_back(data[i].people[k]);

        // for(int k=0; k<data[i].group; k++){
        //     printf("%d ", que.front());
        //     que.pop_front();
        // }

        
        money = 0;

        for(uint loop=0; loop<data[i].rotate; loop++){
            remain = data[i].seat;
            for(int j=0;j<data[i].group;j++){
                num = que.front();
                if( remain - num < 0 ) break;

                remain -= num;
                que.pop_front();
                que.push_back(num);
                money += num;
            }
        }

        //fprintf(stdout, "Case #%d: %d\n", i+1, money);
        fprintf(fout, "Case #%d: %u\n", i+1, money);
        que.clear();
    }
}

int main(void){
    
    Env *env;
    env = new Env;
    env->init((char *)INFILENAME, (char *)OUTFILENAME);
    env->exec();

    return 0;
}
