#include <string>
#include <iostream>
#include <vector>

using namespace std;






string get_line(void)
{
    const int N = 100;
    char buff[N];

    std::string str;

    for (;;) {
        if (fgets(buff, N, stdin) == NULL)
            break;

        int len = strlen(buff);
        if (buff[len - 1] == '\n') {
            str.append(buff, len - 1);
            break;
        } else if (len == N - 1) {
            str.append(buff);
        } else {
            str.append(buff);
            break;
        }
    }

    return str;
}


void calc(int z){
	string code = "welcome to code jam";
	
	string str;
	str = get_line();
	
	unsigned int score[20];
	for(int i=0;i<20;i++) score[i]=0;
	
	for(int i=0;i<str.size();i++){
	//	cout << str[i];
		for(int j=code.length()-1;j>=0;j--){
			if(str[i] == code[j]){
				if(j == 0) score[j]++;
				else score[j] += score[j-1];
			}
			//cout << score[j] << ",";
		}
		//cout << endl;
	}
	unsigned int ans = score[code.length()-1];
	
	cout << "Case #" << z+1 << ": ";
	if(ans < 1000) cout << "0";
	if(ans < 100) cout << "0";
	if(ans < 10) cout << "0";
	cout << ans << endl;
	
}

int main(){
	int all;
	cin >> all;
	
	for(int z=0;z<all;z++) calc(z);
	
	return 1;
}