#include <cstdio>

#define LEN 110

int total[LEN];
int best[LEN];
int s_best[LEN];

int main(){
    int T, i;
    FILE * fin = fopen("B-large.in", "r");
    FILE * fout = fopen("B-large.out", "w");


    fscanf(fin,"%d\n", &T);
    for(i=1;i<=T;++i){
        int s,n,p;
        fscanf(fin, "%d%d%d", &n, &s, &p);

        int j;
        for(j=0;j<n;++j){
            fscanf(fin, "%d", &total[j]);
        }


        int n_best_bigger_than_p = 0;
        int n_best_less_than_p_and_s_best_bigger_than_p = 0;
        for(j=0;j<n;++j){
            int t = total[j];
            if(t<3){
                if(t == 0)
                {
                    best[j] = 0;
                    s_best[j] = 0;
                }else if(t == 1)
                {
                    best[j] = 1;
                    s_best[j] = 1;
                }else
                {
                    best[j] = 1;
                    s_best[j] = 2;
                }
            }
            else if(t%3 == 0)
            {
                best[j] = t/3;
                s_best[j] = best[j] + 1;
            }else if(t%3 == 1)
            {
                best[j] = t/3 + 1;
                s_best[j] = best[j];
            }else// t%3 == 2
            {
                best[j] = t/3 + 1;
                s_best[j] = best[j] + 1;
            }

            if(best[j]>=p)
                n_best_bigger_than_p++;
            else if(best[j]<p && s_best[j]>=p)
                n_best_less_than_p_and_s_best_bigger_than_p++;
        }
        int r;
        if(s<=n_best_less_than_p_and_s_best_bigger_than_p)
            r = s + n_best_bigger_than_p;
        else
            r = n_best_less_than_p_and_s_best_bigger_than_p + n_best_bigger_than_p;
        fprintf(fout, "Case #%d: %d\n", i, r);

    }
    fclose(fin);
    fclose(fout);
    return 0;
}
