#include <iostream>
#include <vector>

using namespace std;

int answer;

int solve(vector<int> &total, int S, int p)
{

    int value, remainder;
    for (int i = 0 ; i<total.size(); i++) {
        int point;

        point = total[i];
        value = point/3;
        remainder = point%3;
        
        if (point < p)  continue;
        if (p-value > 2)continue;
        
        if (value >= p) {
            answer +=1;
        }
        else {
            if (p - value == 1) {
                if (remainder == 0 && S) {
                    answer += 1; S -= 1;
                }
                else if (remainder == 1){
                    answer += 1;
                }
                else if (remainder == 2 ){
                    answer += 1;
                }  
            }
            if (p - value == 2) {
                if (remainder == 2 && S) {
                    answer += 1; S -= 1;
                }
            }
        }
        
    }
    return answer;
}
int main(void)
{
        /* Start Solving Problem */
    
    freopen("Input.txt", "r", stdin);
    //freopen("OutputText.txt", "w", stdout);
    
    int T;
    scanf("%d",&T);getchar();

    for (int i = 1; i<=T; i++) {
        answer = 0;
        int N,S,p;
        scanf("%d %d %d",&N,&S,&p);
        vector<int> total;

        //Taking Points of Googlers
        for (int j=0; j<N; j++) {
            int temp;
            cin>>temp;
            total.push_back(temp);
        }
        
        cout<<"Case #"<<i<<": "<<solve(total, S, p)<<endl;        
    }

    return 0;
}
