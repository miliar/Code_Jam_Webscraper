#include <iostream>
#define INF 99999

using namespace std;

int main()
{
    char search_engine[101][101];
    char input_query[101];
    int query[1001];
    
    int min[2][101];
    int temp_min;
    int ans;
    
    int case_num, case_count;
    int search_engine_num;
    int query_num;

    int i, j, k;

    cin >> case_num;

    for(case_count=1; case_count<=case_num; case_count++) {
        
        temp_min = 0;        

        cin >> search_engine_num;
        cin.get();
        
        for(i=1; i<=search_engine_num; i++){
            cin.getline( search_engine[i], 100);

        }
        
        cin >> query_num;
        cin.get();
        
        if(query_num==0) {
            cout << "Case #" << case_count << ": " << 0 << endl; 
            continue;
        }
        
        for(i=1; i<=query_num; i++) {
            cin.getline( input_query, 100 );
            for(j=1; j<=search_engine_num; j++) {
                if(strcmp(input_query, search_engine[j]) == 0) {
                    query[i] = j;
                    break;
                }    
            }
        }
        
        for(i=1; i<=search_engine_num; i++){
            if(query[1] == i)
                min[1][i] = INF;
            else
                min[1][i] = 0;           
        }



        temp_min = INF;
        for(i=1; i<=search_engine_num; i++) {
            if(temp_min > min[1][i])
                temp_min = min[1][i];
        }

        
        for(i=2; i<=query_num; i++){
            if(query[i] == query[i-1]) {
                //cout << "hey" << endl;
                for(j=1; j<=search_engine_num; j++)
                    min[i%2][j] = min[(i+1)%2][j];
            }
            else {
                for(j=1; j<=search_engine_num; j++) {
                    if(j==query[i-1]){
                        //cout << "!" << endl;
                        //cout << temp_min << endl;
                        min[i%2][j] = temp_min+1;
                        //cout << min[i%2][j] << endl;
                        //cout << "!" << endl;
                    }
                    else if(j==query[i])
                        min[i%2][j] = INF;
                    else
                        min[i%2][j] = min[(i+1)%2][j];
                }
            }
            
            temp_min = INF;
            for(j=1; j<=search_engine_num; j++) {
                //cout << "min["<<i<<"]["<<j<<"] = " << min[i%2][j]<<endl;
                if(temp_min > min[i%2][j])
                    temp_min = min[i%2][j];
            }
            //cout << "temp_min[] = " << temp_min << endl;
        }
        
        
        cout << "Case #" << case_count << ": " << temp_min << endl;
        
    }
    
    //system("pause");
}
