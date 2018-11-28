#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Pattern{
    vector<int> chars;        
                
    bool test(string & str){
        if (str.size() != chars.size())
            return false;
        for (int i = 0; i < str.size(); i++){
            if (!(chars[i] & (1 << (str[i]-'a'))))
                return false;
        }        
        return true;
    }
    void init(string & str){
        int i = 0;
        while (i < str.size()){
            if (str[i] == '('){
                int num = 0;
                int j;
                for (j = i + 1; str[j] != ')'; j++){
                    num = num | (1 << (str[j] - 'a'));
                }
                chars.push_back(num);                
                i = j + 1;
            }else{
                chars.push_back(1 << (str[i] - 'a'));
                i++;
            }            
        }
    }    
};

string strs[1024 * 1024];

int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);

    int L,D,N;
    scanf("%d %d %d",&L,&D,&N);
    for (int i = 0; i < D; i++)
        cin >> strs[i];
    for (int j = 0; j < N; j++){
        string str; cin >> str;
        Pattern p; p.init(str);
        int count = 0;
        for (int i = 0; i < D; i++)
            if (p.test(strs[i]))
                count++;
        printf("Case #%d: %d\n",j+1,count);
    }

    return 0;
}