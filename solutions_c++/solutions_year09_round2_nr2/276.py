#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>


using namespace std;

class comp{
    public:
bool operator()(char a, char b){
    return a>b;
}
};

int main(){
    int ncases;
    cin >> ncases;
    for(int x=1;x<=ncases;x++){
        string num;
        cin >> num;
        if(num.size()==1){
            cout << "Case #" << x << ": " << num << "0" << endl;
            continue;
        }
        priority_queue<char,vector<char>,comp> q;
        q.push(num[num.size()-1]);
        bool found = false;
        for(int i=num.size()-2;i>=0;i--){
            if(num[i+1]>num[i]){
                string back = "";
                cout << "Case #" << x << ": " << num.substr(0,i);
                q.push(num[i]);
                while(q.top()<=num[i]){
                    back+=q.top();
                    q.pop();
                }
                cout << q.top() << back;
                q.pop();
                while(!q.empty()){
                    cout << q.top();
                    q.pop();
                }
                cout << endl;
                found = true;
                break;
            }
            q.push(num[i]);
        }
        if(!found){
            vector<char> numeros;
            int zeros = 1;
            for(int i=0;i<num.size();i++){
                if(num[i] != '0') numeros.push_back(num[i]);
                else zeros++;
            }
            sort(numeros.begin(),numeros.end());
            cout << "Case #" << x << ": " << numeros[0];
            for(int i=0;i<zeros;i++) cout << 0;
            for(int i=1;i<numeros.size();i++) cout << numeros[i];
            cout << endl;
        }
    }
}

        