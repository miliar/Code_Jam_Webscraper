#include <iostream>

using namespace std;

int main(){
    int numCases;
    cin>>numCases;
    for(int caseNum=0; caseNum<numCases; caseNum++){
        int length, surprising, p, answer=0;
        cin>>length>>surprising>>p;
        for(int n=0; n<length; n++){
            int sum;
            cin>>sum;
            if(sum%3==0){
                if(sum/3>=p)
                    answer++;
                else if(sum/3+1==p && surprising>0 && sum/3-1>=0){
                    surprising--;
                    answer++;
                }
            }
            else if(sum%3==1){
                if(sum/3+1>=p)
                    answer++;
            }
            else{
                if(sum/3+1>=p)
                    answer++;
                else if(sum/3+2==p && surprising>0){
                    surprising--;
                    answer++;
                }
            }
        }
        cout<<"Case #"<<caseNum+1<<": "<<answer<<endl;
    }
    return 0;
}
