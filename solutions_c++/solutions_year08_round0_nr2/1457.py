#include <iostream>
#include <stdlib.h>
#define INF 99999
using namespace std;

struct times {
    int start;
    int end;
};

int compare (const void * a, const void * b)
{
  return ( (*(struct times*)a).start - (*(struct times*)b).start );
}

int main()
{
    int N, T;
    int NA, NB;
    int case_num;
    
    char tmp[10];
    
    struct times *tripsA;
    struct times *tripsB;

    int i, j;
    int count_A, count_B;
    
    int train_in_A[1601];
    int train_in_B[1601];
    
    int total_train_num_A;
    int total_train_num_B;
    
    
    tripsA= new struct times[100];
    tripsB = new struct times[100];
    
    cin >> case_num;
    
    for(N=1; N<=case_num; N++) {
    
        cin >> T;
        cin >> NA >> NB;
        
        total_train_num_A = 0;
        total_train_num_B = 0;
        
        count_A = 0;
        count_B = 0;
    
        for(i=0; i<1600; i++) {
            train_in_A[i] = 0;
            train_in_B[i] = 0;
        }
        
        for(i=0; i<NA; i++){
            cin >> tmp;
            tripsA[i].start = (tmp[0]-'0')*600 + (tmp[1]-'0')*60 + (tmp[3]-'0')*10 + (tmp[4]-'0');
                     
            cin >> tmp;
            tripsA[i].end = (tmp[0]-'0')*600 + (tmp[1]-'0')*60 + (tmp[3]-'0')*10 + (tmp[4]-'0');
        }
        tripsA[i].start = INF;
        tripsA[i].end = INF;
        
        for(i=0; i<NB; i++){
            cin >> tmp;
            tripsB[i].start = (tmp[0]-'0')*600 + (tmp[1]-'0')*60 + (tmp[3]-'0')*10 + (tmp[4]-'0');
                     
            cin >> tmp;
            tripsB[i].end = (tmp[0]-'0')*600 + (tmp[1]-'0')*60 + (tmp[3]-'0')*10 + (tmp[4]-'0');
        }
        tripsB[i].start = INF;
        tripsB[i].end = INF;
        
        qsort(tripsA, NA, sizeof(struct times), compare);
        qsort(tripsB, NB, sizeof(struct times), compare);
        
        /*for(i=0; i<NA; i++)
            cout << tripsA[i].start << ' ' << tripsA[i].end << endl;
        cout << endl;
        
        for(i=0; i<NB; i++)
            cout << tripsB[i].start << ' ' << tripsB[i].end << endl;
        cout << endl;
        */
        for(i=0; i<=1440; i++) {


            while(i == tripsA[count_A].start) {  
                if(train_in_A[i] == 0)
                    total_train_num_A ++;
                else
                    train_in_A[i] --;
                
                train_in_B[tripsA[count_A].end+T] ++; 
                count_A++;
            }    
            
            while(i == tripsB[count_B].start) {
                if(train_in_B[i] == 0)
                    total_train_num_B ++;
                else
                    train_in_B[i] --;
                
                train_in_A[tripsB[count_B].end+T] ++; 
                count_B++;
            }
            
            train_in_A[i+1] += train_in_A[i];
            train_in_B[i+1] += train_in_B[i];
            
            //cout << i << ": "
              //   << train_in_A[i] << ' ' << total_train_num_A << ' '
                // << train_in_B[i] << ' ' << total_train_num_B << endl;
            
        }
        
        cout << "Case #" << N << ": " << total_train_num_A << ' ' << total_train_num_B << endl;
        
    }
    
}
