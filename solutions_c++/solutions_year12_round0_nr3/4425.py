#include <iostream>
#include <cmath>

#define DATASET 1001

using namespace std;

int getRecycled(int A, int B);
int getNumDigits(int num);

int main(int argc, char * argv)
{
    int T, A, B;
    cin >> T;
    
    for(int i = 0; i < T; i++)
    {
        cin >> A >> B;
        cout << "Case #" << i+1 << ": " << getRecycled(A, B) << endl;
    }
}

int getRecycled(int A, int B)
{
    int count = 0, num_digits = getNumDigits(A);
    int recycled[DATASET];
    
    memset(recycled, 0, DATASET * sizeof(int));
    
    for(int curr = A; curr < B; curr++)
    {
        int recycle = curr;
        for(int i = 0; i < num_digits; i++) {
            recycle = (recycle % (int) pow( (double) 10, num_digits-1)) * 10
                    + (recycle / (int) pow( (double) 10, num_digits-1));
            
            if(recycle > B || recycle <= curr || recycled[recycle] == 1) { 
                continue;
            }
            
            recycled[recycle] = 1;
            count++;
        }
        
        memset(recycled, 0, DATASET * sizeof(int));
    }
    
    return count;
}

int getNumDigits(int num) {
    int count = 0;
    
    do {
        num /= 10;
        count++;
    } while(num != 0);
    
    return count;
}