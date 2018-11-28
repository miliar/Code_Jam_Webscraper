#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
using namespace std;


int main(int argc, char *argv[])
{
    FILE *inf = fopen("sma.in","r");
    FILE *of = fopen("out.out","w");
    int T, M, N;
    fscanf(inf,"%d\n",&T);
    for(int i=0;i<T;i++){
        map<string, bool> fs;
        fscanf(inf, "%d %d\n", &M, &N);
        char path[100];string p;
        int poz;
        for(int j=0; j < M; j++){
            fscanf(inf, "%[^\n]\n", path);
            p = string(path);
            string cp = "";
            p = p.substr(1);p+='/';
//            printf("%d\n", p.find('/'));
            poz = p.find('/');
            while(poz >= 0){
                cp += "/" + p.substr(0,poz);
                p = p.substr(poz+1,p.length()-poz+1);
//                printf("%s\n", cp.c_str());
                poz = p.find('/');
                fs[cp] = true;
            }
            
        }
        int res = 0;
        for(int j=0;j< N; j++){

            fscanf(inf, "%[^\n]\n", path);
            p = string(path);
            string cp = "";
            p = p.substr(1);p+='/';
//            printf("%d\n", p.find('/'));
            poz = p.find('/');
            while(poz >= 0){
                cp += "/" + p.substr(0,poz);
                p = p.substr(poz+1,p.length()-poz+1);
//                printf("%s\n", cp.c_str());
                poz = p.find('/');
                if(fs.find(cp) == fs.end()){
                     fs[cp] = true;
                     res++;
                }
            }
        }
        fprintf(of,"Case #%d: %d\n", i+1, res);
        
    }
    fclose(inf);fclose(of);
    return EXIT_SUCCESS;
}

