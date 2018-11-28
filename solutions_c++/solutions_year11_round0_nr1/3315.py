#include <cstdlib>
#include <iostream>

using namespace std;


typedef struct Block{
    char robot;
    int button;
    int estado;
}Block;


int res_seg(Block *b, int N){

    int b_atual = 1, o_atual = 1;
    int i_b = 1000, i_o = 1000;
    int counter = 0;
    int final_b = 0;
    int final_o = 0;
    int push_b;
    int push_o;


    for(int i = 0; i<N; i++){
        if(b[i].robot == 'O'){
            i_o = i;
            break;
        }
    }



    for(int i = 0; i<N; i++){
        if(b[i].robot == 'B'){
            i_b = i;
            break;
        }
    }

    while(true){

        if(i_o != 1000){
        if(o_atual != b[i_o].button){
            if(o_atual > b[i_o].button){
                o_atual --;
            }
            else if(o_atual < b[i_o].button){
                o_atual ++;
            }
        }

        else if(o_atual == b[i_o].button){
            if((i_o < i_b) || (final_b == 1)){
                push_o = 1;
            }
            else o_atual = o_atual;
        }
        }else final_o = 1;

        if(i_b != 1000){
        if(b_atual != b[i_b].button){
            if(b_atual > b[i_b].button){
                b_atual --;
            }
            else if(b_atual < b[i_b].button){
                b_atual ++;
            }
        }

        else if(b_atual == b[i_b].button){
            if((i_b < i_o) || (final_o == 1)){
                push_b = 1;
            }
            else b_atual = b_atual;
        }
        }else final_b = 1;

        if(push_o == 1){
            if(i_o != N-1){
                for(int i = i_o +1; i<N; i++){
                        if(b[i].robot == 'O'){
                            i_o = i;
                            break;
                        }
                        else if(i == N-1)final_o = 1;
                }
            }
            else final_o = 1;
                push_o = 0;
        }

        if(push_b == 1){
            if(i_b != N-1){
            for(int i = i_b + 1; i<N; i++){
                        if(b[i].robot == 'B'){
                            i_b = i;
                            break;
                        }
                        else if(i == N-1)final_b = 1;
                }
            }
            else final_b = 1;
            push_b = 0;
        }

      counter++;

      //printf("\n\nRobo: %c Botao: %d Final: %d\n", b[i_b].robot, b[i_b].button, final_b);
      //printf("\nRobo: %c Botao: %d Final: %d\n", b[i_o].robot, b[i_o].button, final_o);

      if(final_o == 1 && final_b == 1)return counter;

      }
}



int main(int argc, char *argv[]){

    Block b[100];

    int T, N, Tot = 0;
    FILE *in;
    FILE *out;
    int teste;


    in = fopen("A-large.in", "r");
    out = fopen("out.txt", "w");

    fscanf(in, "%d\n", &T);

    for(int i = 0; i<T; i++){
        fscanf(in, "%d ", &N);
        for(int j = 0; j<N; j++){
            fscanf(in, "%c %d ", &b[j].robot, &b[j].button);
            }
        Tot = res_seg(b, N);
        fprintf(out, "Case #%d: %d\n", i+1, Tot);
        //scanf("%d", &teste);
    }

    return 0;
}
