#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std ;

double judge_score[200] ;

int main()
{
    int T ;
    cin >> T ;
    for( int count_case = 0 ; count_case < T ; ++ count_case )
    {
        int N ; 
        cin >> N ; 
        double sum = 0 ;
        for( int i = 0 ; i < N ; ++ i )
        {
            cin >> judge_score[i] ; 
            sum += judge_score[i] ; 
        }
        
        double sum_temp = sum ;
        sum += sum ;
        double avg_score = sum / N ;
        int count_avg = N ;
        for( int i = 0 ; i < N ; ++ i )
            if( judge_score[i] > avg_score )
            { 
                sum -= judge_score[i] ;
                count_avg -- ;
            }
        
        avg_score = sum / count_avg ;
        printf("Case #%d:",count_case+1) ;
        for( int i = 0 ; i < N ; ++ i )
        {
            if( judge_score[i] < avg_score )
            printf(" %.6lf",(avg_score - judge_score[i]) * 100 / sum_temp) ;
            else 
                printf(" 0.000000") ;
        }
        cout << endl ;
    }
    return 0 ;
}
