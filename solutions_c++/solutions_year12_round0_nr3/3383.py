#include <iostream>
#include <map>
#include <sstream>

using namespace std;
int answer;

long int ten[] = {0,10,100,1000,10000,100000,1000000,10000000} ;

int lengthOfNumber(long int number)
{
    stringstream buf; buf<<number; 
    string s = buf.str();
    return s.size();
}
int solve(long int number, long int A, long int B)
{
    int l = lengthOfNumber(number);
    map<long int, int> result;
    for (int i = 1 ; i < l ; i++) {
        if (number % ten[i] > ten[i-1]) {
           long cNumber = (number % ten[i])*ten[l-i] + number / ten[i];
            if (cNumber > number && (cNumber >= A) && (cNumber <= B)) {
                result[cNumber] = 1;;
            }
        }
    }
    return result.size();
}
int main(void)
{
    
    /* Start Solving Problem */
    
    freopen("Input.txt", "r", stdin);
    freopen("OutputText.txt", "w", stdout);
    
    int T;
    scanf("%d",&T);getchar();

    for (int i = 1; i<=T; i++) {
        
        int answer = 0;
        long int A,B;
        
        cin>>A>>B;
        
        for (long int i=A; i<=B; i++) {
            answer += solve(i, A, B);
        }
        //Show Result of Case:
        cout<<"Case #"<<i<<": "<<answer<<endl;        
    }

    return 0;
}
