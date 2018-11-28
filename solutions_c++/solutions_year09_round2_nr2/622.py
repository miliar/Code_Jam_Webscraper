#include<iostream>
#include<string>
#include<fstream>
#include<vector>

using namespace std;

int main(){
    int T;
    cin>>T;

    ofstream fout("number.out");

    //testcases
    for(int t = 0; t < T; ++t){
        string number;
        cin>>number;

        vector<bool> valid(10,false);
        vector<int> index(10,-1);

        bool ok = false;
        for(int i = number.size()-1; i >= 0 && !ok; --i){
            for(int k = number[i]-'0' + 1; k < 10; ++k){

                //valid change
                if(valid[k]){
                    number[index[k]] = number[i];
                    number[i] = k+'0';
                    sort(number.begin()+i+1,number.end());
                    ok = true;
                    break;
                }

            }

            if(!ok){
                valid[number[i]-'0'] = true;
                index[number[i]-'0'] = i;
            }
        }

        if(!ok){
            number.push_back('0');
            sort(number.begin(),number.end());
            int i = 0;
            while(number[i] == '0') ++i;
            char temp = number[i];
            number[i] = number[0];
            number[0] = temp;
        }

        fout<<"Case #"<<t+1<<": "<<number<<endl;
    }

    return 0;
}
