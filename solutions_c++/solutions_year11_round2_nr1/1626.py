#include <cstdio>

int N;
int res[100][100];
int tots[100];
double WP[100];
double OWP[100];
double OOWP[100];

int main(int argc, char** argv)
{
    int C;
    scanf("%d", &C);
    
    for(int c = 1; c <= C; ++c)
    {
        printf("Case #%d: \n", c);
        
        scanf("%d ", &N);
        
        for(int i = 0; i < N; ++i)
        {
            for(int j = 0; j < N; ++j)
            {
                char chr;
                scanf("%c", &chr);
                
                if(chr == '0')
                    res[i][j] = -1;
                else if(chr == '.')
                    res[i][j] = 0;
                else
                    res[i][j] = 1;
            }
            scanf(" ");
        }
        
        for(int i = 0; i < N; ++i)
        {
            WP[i] = 0;
            
            double win = 0;
            double total = 0;
            
            for(int j = 0; j < N; ++j)
            {
                if(res[i][j] == 1)
                {
                    win += 1.0;
                    total += 1.0;
                }
                else if(res[i][j] == -1)
                {
                    total += 1.0;
                }
            }
            
            WP[i] = win/total;
            tots[i] = total;
        }
        
        for(int i = 0; i < N; ++i)
        {
            OWP[i] = 0;
            
            double s = 0.0;
            double op = 0.0;
            
            for(int j = 0; j < N; ++j)
            {
                if(res[i][j] != 0)
                {
                    if(res[j][i] == 1)
                    {
                        double t = tots[j];
                        
                        s += (WP[j] - 1.0/t)*t/(t-1);
                        op += 1.0;
                    }
                    else if(res[j][i] == -1)
                    {
                        double t = tots[j];
                        s += WP[j]*t/(t-1);
                        op += 1.0;
                    }
                }
            }
            
            OWP[i] = s/op;
        }
        
        for(int i = 0; i < N; ++i)
        {
            OOWP[i] = 0;
            
            double s = 0.0;
            double op = 0.0;
            
            for(int j = 0; j < N; ++j)
            {
                if(res[i][j] != 0)
                {
                    s += OWP[j];
                    op += 1.0;
                }
            }
            
            OOWP[i] = s/op;
        }
        
        for(int i = 0; i < N; ++i)
        {
            double val = 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i];
            printf("%.10lf\n", val);
//             printf("%lf %lf %lf\n", WP[i], OWP[i], OOWP[i]);
        }
        
    }
    return 0;
}